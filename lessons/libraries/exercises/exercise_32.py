import scipy


def splitter():
    img = scipy.datasets.face()
    R = img.copy()
    G = img.copy()
    B = img.copy()
    for i in range(768):
        for j in range(1024):
            R[i][j][1] = 0
            R[i][j][2] = 0
            G[i][j][0] = 0
            G[i][j][2] = 0
            B[i][j][1] = 0
            B[i][j][0] = 0

    return [R, G, B]
