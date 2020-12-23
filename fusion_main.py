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
    I1 = cv2.imread(img1)
    I2 = cv2.imread(img2)

    ## Fusion algo
    iR1 = I1.copy()
    iR1[:,:,1] = iR1[:,:,2] = 0

    iR2 = I2.copy()
    iR2[:,:,1] = iR2[:,:,2] = 0

    # First: Do wavelet transform on each image
    wavelet = 'db1'
    cooef1 = pywt.dwt2(iR1, 'db5', mode = 'periodization')
    cooef2 = pywt.dwt2(iR2, 'db5', mode = 'periodization')
    cA1, (cH1, cV1, cD1) = cooef1
    cA2, (cH2, cV2, cD2) = cooef2

    cA = (cA1+cA2)/2
    cH = (cH1 +cH2)/2
    cV = (cV1+cV2)/2
    cD = (cD1+cD2)/2
    fincoR = cA, (cH,cV,cD)
    outImageR = pywt.idwt2(fincoR, 'db5', mode = 'periodization')


    iG1 = I1.copy()
    iG1[:,:,0] = iG1[:,:,2] = 0
    iG2 = I2.copy()
    iG2[:,:,0] = iG2[:,:,2] = 0

    cooef1 = pywt.dwt2(iG1, 'db5', mode = 'periodization')
    cooef2 = pywt.dwt2(iG2, 'db5', mode = 'periodization')
    cA1, (cH1, cV1, cD1) = cooef1
    cA2, (cH2, cV2, cD2) = cooef2

    cA = (cA1+cA2)/2
    cH = (cH1 +cH2)/2
    cV = (cV1+cV2)/2
    cD = (cD1+cD2)/2
    fincoG = cA, (cH,cV,cD)
    outImageG = pywt.idwt2(fincoG, 'db5', mode = 'periodization')

    iB1 = I1.copy()
    iB1[:,:,0] = iG1[:,:,1] = 0
    iB2 = I2.copy()
    iB2[:,:,0] = iG2[:,:,1] = 0


    cooef1 = pywt.dwt2(iB1, 'db5', mode = 'periodization')
    cooef2 = pywt.dwt2(iB2, 'db5', mode = 'periodization')
    cA1, (cH1, cV1, cD1) = cooef1
    cA2, (cH2, cV2, cD2) = cooef2

    cA = (cA1+cA2)/2
    cH = (cH1 +cH2)/2
    cV = (cV1+cV2)/2
    cD = (cD1+cD2)/2
    fincoB = cA, (cH,cV,cD)
    outImageB = pywt.idwt2(fincoB, 'db5', mode = 'periodization')

    outImage = I1.copy()
    outImage[:,:,0] = outImage[:,:,1] = outImage[:,:,2] = 0
    outImage[:,:,0] = outImageR[:,:,0]
    outImage[:,:,1] = outImageG[:,:,1]
    outImage[:,:,2] = outImageB[:,:,2] 

    outImage = np.multiply(np.divide(outImage - np.min(outImage),(np.max(outImage) - np.min(outImage))),255)
    outImage = outImage.astype(np.uint8)

    '''kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
    im = cv2.filter2D(outImage, -1, kernel)'''

    x = random.randint(1000, 2000)
    loc = 'demo/out'+str(x)+'.jpg'
    cv2.imwrite(loc,outImage)

    return loc
