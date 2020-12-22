# Imfusion

An Open Source image fusion desktop app. It supports image fusion using Discrete wavelet transformation. 

### What is Image Fusion

Image fusion combines the information of two or more images which are of the same time ans same scene to generate more detailed image than the individual images. For example,combining two photos of the same scene with each photo having different things on focus, if in first photo one or more objects are in focus and in second image other objects.The MRI and the CT scans are based on this. The CT scan just reveals the bone structure and hard tissues and the MRI reveals the soft tissues of brain which is used to detect disease affecting the skull base.Since these both scans provide different information individually each of them are not as useful as they are when they combined. The full potential of these scans can be used when the important features of each scan can be fused using image fusion which generates a better result containing of best features of both the scan.

<table>

<tr>
    <td><img height="250" src="https://github.com/robustTechie/ImageX/blob/main/screenshot/Screenshot%20from%202020-12-01%2002-14-21.png?raw=true"  /><br /><center><b>CT scan</b></center></td>
    <td><img height="250" src="https://github.com/robustTechie/ImageX/blob/main/screenshot/Screenshot%20from%202020-12-01%2002-14-16.png?raw=true" /><br /><center><b>MRI scan </b></center></td> <td><img height="250" src="https://github.com/robustTechie/ImageX/blob/main/screenshot/Screenshot%20from%202020-12-01%2002-13-59.png?raw=true" /><br /><center><b>Fused Image</b></center></td>
    </td>
</tr>

</table>

### What is Discrete Wavelet Transformation

Wavelet is a component which is used to divide a function into various scale components. Each scale can be studied to provide some deeper information regarding the actual information. The DWT is based on sub-band which yields fast computation for transformation. It has so many applications in Digital Image processing like image compression, fusion, recognition, denoising, etc. Wavelets are powerful tool and they are now being adopted for vast number of applications. Extracting more information from the image is an important task which we can do to get maximum from an image. It is used to improve resolution of the images, here first the images are decomposed into its sub-images using various coefficients and with different frequency. After processing and applying the desired operation we again reconstruct the image to get more plentiful information. 

<table>

<tr>
    <td><img height="250" src="https://github.com/robustTechie/ImageX/blob/main/screenshot/Screenshot%20from%202020-12-01%2002-14-21.png?raw=true"  /><br /><center><b>CT scan</b></center>
    </td>
</tr>
</table>

### Tech stack and libraries used - 
* PyQt5
* Python3
* Pywt
* Matplotlib
* Cv2
* NumPy

### How to build
For builidng this you need to run `python3 imfusion_main.py`. This will open a desktop app which will provide you to select various features like `image restoration`, `image mixing`, `face morphing` and then ask you to insert the image in which it will work on. Make sure you installed all the required libraries. You can install the libraries by running requirements.txt - `pip3 install -r requirements.txt`.

### Screenshots

<table>
    <tr>
          <td><img height="250" src="https://raw.githubusercontent.com/robustTechie/ImageX/main/screenshot/Screenshot%20from%202020-12-01%2001-58-13.png" /><br /><center><b>Desktop app</b></center></td>
    </tr>
</table>


<table>
Image Restoration
<tr>
    <td><img height="250" src="https://github.com/robustTechie/ImageX/blob/main/screenshot/Screenshot%20from%202020-12-01%2002-14-21.png?raw=true"  /><br /><center><b>Faulty Image 1</b></center>
    <td><img height="250" src="https://github.com/robustTechie/ImageX/blob/main/screenshot/Screenshot%20from%202020-12-01%2002-14-26.png?raw=true" /><br /><center><b>Faulty Image 2</b></center></td><td><img height="250" src="https://github.com/robustTechie/ImageX/blob/main/screenshot/Screenshot%20from%202020-12-01%2002-14-16.png?raw=true" /><br /><center><b>Fused image</b></center></td>
    </td>
    </tr>
</table>

<table>
Image Mixing
    <tr>
    <td><img height="250" src="https://github.com/robustTechie/ImageX/blob/main/screenshot/Screenshot%20from%202020-12-01%2002-15-02.png?raw=true"  /><br /><center><b>Image 1</b></center>
    <td><img height="250" src="https://github.com/robustTechie/ImageX/blob/main/screenshot/Screenshot%20from%202020-12-01%2002-15-09.png?raw=true" /><br /><center><b>Image 2</b></center></td><td><img height="250" src="https://github.com/robustTechie/ImageX/blob/main/screenshot/Screenshot%20from%202020-12-01%2002-14-55.png?raw=true" /><br /><center><b>Fused image</b></center></td>
    </tr>
</table>

<table>
Face Morphing
    <tr>
    <td><img height="250" src="https://github.com/robustTechie/ImageX/blob/main/screenshot/Screenshot%20from%202020-12-01%2002-15-02.png?raw=true"  /><br /><center><b>Face 1</b></center>
    <td><img height="250" src="https://github.com/robustTechie/ImageX/blob/main/screenshot/Screenshot%20from%202020-12-01%2002-15-09.png?raw=true" /><br /><center><b>Face 2</b></center></td><td><img height="250" src="https://github.com/robustTechie/ImageX/blob/main/screenshot/Screenshot%20from%202020-12-01%2002-14-55.png?raw=true" /><br /><center><b>Fused image</b></center></td> 
    </tr>
</table>