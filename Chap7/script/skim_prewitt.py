from skimage.io import imread
from skimage.io import imshow
from skimage.io import imsave
from skimage.io import show
from skimage.color import rgb2gray
import numpy as np


def normalisation(img, maxi, mini):
    img = np.divide((img-mini), (maxi-mini))
    img *= 255

    return img


if __name__ == '__main__':

    im_a = imread("./save0.jpeg")
    im_b = imread("./save1.jpeg")
    im_a_nv = rgb2gray(im_a)
    im_b_nv = rgb2gray(im_b)

    im_res = np.abs(im_a_nv - im_b_nv)
    val_max = np.max(np.max(im_res))
    val_min = np.min(np.min(im_res))
    val_mean = np.mean(np.mean(im_res))

    print("Valeur mini : ", val_min)
    print("Valeur maxi : ", val_max)
    print("Valeur moyenne : ", val_mean)

    im_norma = normalisation(im_res, val_max, val_min)

    imshow(im_norma)
    show()

    imsave("./mean_sk.png", im_norma.astype(int))
