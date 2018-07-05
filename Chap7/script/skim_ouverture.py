from skimage.io import imread
from skimage.io import imshow
from skimage.io import imsave
from skimage.io import show
from skimage.filters import rank
from skimage.morphology import disk
from skimage.color import rgb2gray


if __name__ == '__main__':

    selem = disk(20)
    mon_image = imread("./test_ng.png")
    mon_image_nv = rgb2gray(mon_image)
    im_mean = rank.mean(mon_image_nv, selem=selem)

    imshow(im_mean)
    show()

    imsave("./mean_sk.png", im_mean)
