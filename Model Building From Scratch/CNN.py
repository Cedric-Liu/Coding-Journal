import numpy as np
from functools import reduce


class Conv2D(object):
    def __init__(self, shape, output_channels, ksize=3, stride=1, method='VALID'):
        self.input_shape = shape
        self.output_channels = output_channels
        self.input_channels = shape[-1]
        self.batchsize = shape[0]
        self.stride = stride
        self.ksize = ksize
        self.method = method
        self.weights = np.random.standard_normal(
            (ksize, ksize, self.input_channels, self.output_channels))

        if method == 'VALID':
            self.eta = np.zeros((shape[0], (shape[1] - ksize + 1) //
                                 self.stride, (shape[1] - ksize + 1) // self.stride,
             self.output_channels))

        if method == 'SAME':
            self.eta = np.zeros((shape[0], shape[1]//self.stride,
                                 shape[2]//self.stride,self.output_channels))

        self.output_shape = self.eta.shape


    def forward(self, x):
        col_weights = self.weights.reshape([-1, self.output_channels])
        if self.method == 'SAME':
            x = np.pad(x, (
                (0, 0), (self.ksize // 2, self.ksize // 2),
                (self.ksize // 2, self.ksize // 2), (0, 0)),
                             'constant', constant_values=0)

        self.col_image = []
        conv_out = np.zeros(self.eta.shape)
        for i in range(self.batchsize):
            img_i = x[i][np.newaxis, :]
            self.col_image_i = im2col(img_i, self.ksize, self.stride)
            conv_out[i] = np.reshape(np.dot(self.col_image_i,
                                            col_weights),
                                     self.eta[0].shape)
            self.col_image.append(self.col_image_i)
        self.col_image = np.array(self.col_image)
        return conv_out



def im2col(image, ksize, stride):
    # image is a 4d tensor([batchsize, width ,height, channel])
    image_col = []
    for i in range(0, image.shape[1] - ksize + 1, stride):
        for j in range(0, image.shape[2] - ksize + 1, stride):
            col = image[:, i:i + ksize, j:j + ksize, :].reshape([-1])
            image_col.append(col)
    image_col = np.array(image_col)

    return image_col


class Relu(object):
    def __init__(self, shape):
        self.eta = np.zeros(shape)
        self.x = np.zeros(shape)
        self.output_shape = shape

    def forward(self, x):
        self.x = x
        return np.maximum(x, 0)


class MaxPooling(object):
    def __init__(self, shape, ksize=2, stride=2):
        self.input_shape = shape
        self.ksize = ksize
        self.stride = stride
        self.output_channels = shape[-1]
        self.index = np.zeros(shape)
        self.output_shape = [shape[0], shape[1] // self.stride,
                             shape[2] // self.stride, self.output_channels]


    def forward(self, x):
        out = np.zeros([x.shape[0], x.shape[1] // self.stride, x.shape[2] //
                        self.stride, self.output_channels])

        for b in range(x.shape[0]):
            for c in range(self.output_channels):
                for i in range(0, x.shape[1], self.stride):
                    for j in range(0, x.shape[2], self.stride):
                        out[b, i // self.stride, j // self.stride, c] = np.max(
                            x[b, i:(i + self.ksize), j:(j + self.ksize), c])
                        index = np.argmax(x[b, i:i + self.ksize, j:j + self.ksize, c])
                        self.index[b, i+index//self.stride, j + index % self.stride, c] = 1
        return out


class DenselyConnect(object):
    def __init__(self, shape, output_num=2):
        self.input_shape = shape
        self.batchsize = shape[0]

        input_len = reduce(lambda x, y: x * y, shape[1:])

        self.weights = np.random.standard_normal((input_len, output_num))

        self.output_shape = [self.batchsize, output_num]


    def forward(self, x):
        self.x = x.reshape([self.batchsize, -1])
        output = np.dot(self.x, self.weights)
        return output


class Softmax(object):
    def __init__(self, shape):
        self.softmax = np.zeros(shape)
        self.eta = np.zeros(shape)
        self.batchsize = shape[0]


    def predict(self, prediction):
        exp_prediction = np.zeros(prediction.shape)
        self.softmax = np.zeros(prediction.shape)
        for i in range(self.batchsize):
            prediction[i, :] -= np.max(prediction[i, :])
            exp_prediction[i] = np.exp(prediction[i])
            self.softmax[i] = exp_prediction[i]/np.sum(exp_prediction[i])
        return self.softmax


if __name__ == "__main__":
    img = np.ones((1, 28, 28, 1))
    conv1 = Conv2D(img.shape, 3, 3, 1)
    layer1 = conv1.forward(img)
    assert layer1.shape == (1, 26, 26, 3)
    print('The shape of conv1 layer is:', layer1.shape)

    relu1 = Relu(layer1.shape)
    layer2 = relu1.forward(layer1)
    assert layer2.shape == (1, 26, 26, 3)
    print('The shape of relu1 layer is:', layer2.shape)

    maxpooling1 = MaxPooling(layer2.shape, 2, 2)
    layer3 = maxpooling1.forward(layer2)
    assert layer3.shape == (1, 13, 13, 3)
    print('The shape of maxpooling1 layer is:', layer3.shape)

    conv2 = Conv2D(layer3.shape, 5, 4, 1)
    layer4 = conv2.forward(layer3)
    assert layer4.shape == (1, 10, 10, 5)
    print('The shape of conv2 layer is:', layer4.shape)

    relu2 = Relu(layer4.shape)
    layer5 = relu1.forward(layer4)
    assert layer5.shape == (1, 10, 10, 5)
    print('The shape of relu2 layer is:', layer5.shape)

    maxpooling2 = MaxPooling(layer5.shape, 2, 2)
    layer6 = maxpooling2.forward(layer5)
    assert layer6.shape == (1, 5, 5, 5)
    print('The shape of maxpooling2 layer is:', layer6.shape)

    dense1 = DenselyConnect(layer6.shape, 125)
    layer7 = dense1.forward(layer6)
    assert layer7.shape == (1, 125)
    print('The shape of flaten layer is:', layer7.shape)

    dense2 = DenselyConnect(layer7.shape, 10)
    layer8 = dense2.forward(layer7)
    assert layer8.shape == (1, 10)
    print('The shape of output layer is:', layer8.shape)

    softmax = Softmax(layer8.shape)
    layer9 = softmax.predict(layer8)
    assert layer9.shape == (1, 10)
    print('The shape of softmax layer is:', layer9.shape)

    img = np.array([[-11, 4, 1, -1, 12, 9],
                    [1, -4, 3, 0, 1, 10],
                    [9, 2, -5, -7, -10, -8],
                    [8, -2, 1, -11, -5, 7],
                    [-5, 0, -5, -1, -5, 3],
                    [-8, 2, 6, 5, -3, -4]])

    img = np.pad(img, (1,1), 'reflect')
    print(img)
    img = img.reshape(1, 8, 8, 1)
    conv = Conv2D(img.shape, 1, 3, 1)
    conv.weights = np.array([[2,8,11],
                    [-7,-6,-6],
                    [1,-9,-11]])
    conv.weights = conv.weights.reshape(3,3,1,1)
    print(conv.weights.shape)
    output = conv.forward(img)
    print(output)