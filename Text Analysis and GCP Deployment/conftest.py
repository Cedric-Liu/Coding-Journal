import os

import pytest


@pytest.fixture
def rootdir():
    return os.path.dirname(os.path.abspath(__file__))


@pytest.fixture
def datadir(rootdir):
    return os.path.join(rootdir, 'data')
