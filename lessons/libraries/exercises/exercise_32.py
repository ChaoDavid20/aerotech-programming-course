import scipy


def splitter():
    img = scipy.datasets.face()
    R = img.copy()
    G = img.copy()
    B = img.copy()
    R[:, :, 1] = 0
    R[:, :, 2] = 0
    G[:, :, 0] = 0
    G[:, :, 2] = 0
    B[:, :, 1] = 0
    B[:, :, 0] = 0

    return [R, G, B]
