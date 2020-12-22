import pywt
import numpy as np
import matplotlib.pyplot as plt
import random
from PIL import Image
from PIL import ImageFilter

import cv2

# This function does the coefficient fusing according to the fusion method
def fuseCoeff(cooef1, cooef2, method):

    if (method == 'mean'):
        cooef = (cooef1 + cooef2) / 2
    elif (method == 'min'):
        cooef = np.minimum(cooef1,cooef2)
    elif (method == 'max'):
        cooef = np.maximum(cooef1,cooef2)
    else:
        cooef = []

    return cooef

def fusion(img1, img2):
    # Params
    FUSION_METHOD = 'mean' # Can be 'min' || 'max || anything you choose according theory

    # Read the two image
    I1 = cv2.imread(img1,0)
    I2 = cv2.imread(img2,0)

    x = I1.shape
    invX= x[::-1] 
    # We need to have both images the same size
    I2 = cv2.resize(I2,invX) # I do this just because i used two random images

    ## Fusion algo

    # First: Do wavelet transform on each image
    wavelet = 'db1'
    cooef1 = pywt.dwt2(I1, 'db5', mode = 'periodization')
    cooef2 = pywt.dwt2(I2, 'db5', mode = 'periodization')
    cA1, (cH1, cV1, cD1) = cooef1
    cA2, (cH2, cV2, cD2) = cooef2

    cA = (cA1+cA2)/2
    cH = (cH1 +cH2)/2
    cV = (cV1+cV2)/2
    cD = (cD1+cD2)/2
    finco = cA, (cH,cV,cD)
    outImage = pywt.idwt2(finco, 'db5', mode = 'periodization')
    outImage = np.multiply(np.divide(outImage - np.min(outImage),(np.max(outImage) - np.min(outImage))),255)
    outImage = outImage.astype(np.uint8)

    '''kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
    im = cv2.filter2D(outImage, -1, kernel)'''

    x = random.randint(1000, 2000)
    loc = 'demo/out'+str(x)+'.jpg'
    cv2.imwrite(loc,outImage)

    return loc
