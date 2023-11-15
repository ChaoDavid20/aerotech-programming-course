import scipy


def splitter():
    """Split a RGB image in its three color channels.

    This function splits a RGB image ins its three color channels. First it
    imports an image. Then, it makes 3 copies of it. After, it isolates 1
    differente channel in every copy. Finally, it returns a list with the 3
    isolated channels.

    Args:_
        none

    Returns_
        [R, G, B]: the list with the 3 isolated channels.

    """
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
