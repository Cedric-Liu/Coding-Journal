# We have a list of points on the plane.
# Find the K closest points to the origin (0, 0).
def kClosest(points, K):
    def cal_square_dis(point):
        return point[0] ** 2 + point[1] ** 2

    square_dis = [cal_square_dis(point) for point in points]
    max_heap = [i for i in range(K)]
    curr_max = max([square_dis[i] for i in max_heap])
    curr_max_idx = square_dis.index(curr_max)
    for i in range(K, len(points)):
        if square_dis[i] < curr_max:
            max_heap = [i for i in max_heap if i != curr_max_idx]
            max_heap.append(i)
            curr_max = max([square_dis[j] for j in max_heap])
            curr_max_idx = square_dis.index(curr_max)
    return [points[i] for i in max_heap]


# faster version:
def kClosest(points, K):
    def cal_square_dis(point):
        return point[0] ** 2 + point[1] ** 2

    square_dis = [cal_square_dis(point) for point in points]
    max_heap = [i for i in range(K)]
    curr_max = max([square_dis[i] for i in max_heap])
    curr_max_idx = square_dis.index(curr_max)
    curr_max_idx_heap = max_heap.index(curr_max_idx)
    for i in range(K, len(points)):
        if square_dis[i] < curr_max:
            max_heap[curr_max_idx_heap] = i
            curr_max = max([square_dis[i] for i in max_heap])
            curr_max_idx = square_dis.index(curr_max)
            curr_max_idx_heap = max_heap.index(curr_max_idx)
    return [points[i] for i in max_heap]


# sort version(much faster):
def kClosest(points, K):
    def cal_square_dis(point):
        return point[0] ** 2 + point[1] ** 2

    square_dis = [cal_square_dis(point) for point in points]
    hash_dic = dict((key, value) for key, value in
                    zip(list(range(len(points))), square_dis))
    sorted_dic = sorted(hash_dic.items(), key=lambda x: x[1])
    index_k = [sorted_dic[k][0] for k in range(K)]
    return [points[k] for k in index_k]

kClosest([[-95,76],[17,7],[-55,-58],[53,20],[-69,-8],[-57,87],[-2,-42],
          [-10,-87],[-36,-57],[97,-39],[97,49]],5)