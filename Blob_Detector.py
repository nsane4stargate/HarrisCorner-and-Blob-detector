import numpy as np
import cv2
import array
from math import sqrt
from skimage import data, exposure
from skimage.feature import blob_dog, blob_log, blob_doh
from skimage.color import rgb2gray
import matplotlib.pyplot as plt

# Load images
img_1 = cv2.imread("C:/Users/nsane/Documents/Spring '19/CSC528 Computer Vision/Pictures/Assignment_2/Problem_3/butterfly.jpg",cv2.IMREAD_GRAYSCALE)
img_2 = cv2.imread("C:/Users/nsane/Documents/Spring '19/CSC528 Computer Vision/Pictures/Assignment_2/Problem_3/einstein.jpg",cv2.IMREAD_GRAYSCALE)
img_3 = cv2.imread("C:/Users/nsane/Documents/Spring '19/CSC528 Computer Vision/Pictures/Assignment_2/Problem_3/fishes.jpg",cv2.IMREAD_GRAYSCALE)
img_4 = cv2.imread("C:/Users/nsane/Documents/Spring '19/CSC528 Computer Vision/Pictures/Assignment_2/Problem_3/sunflowers.jpg",cv2.IMREAD_GRAYSCALE)

tup1 =(img_1,"Butterfly",30,15,.1)
tup2 =(img_2,"Einstein",30,10,.03)
tup3 =(img_3,"Fishes",30,10,.02)
tup4 =(img_4,"Sunflowers",30,10,.1)

image_list = [tup1,tup2,tup3,tup4]                 

for tup in image_list:
    max_sig = tup[2]
    print(max_sig)
    num_sig = tup[3]
    print(num_sig)
    tolerance = tup[4]
    print(tolerance)
    blobs_log = blob_log(tup[0], max_sigma=max_sig, num_sigma=num_sig, threshold=tolerance)
    title = tup[1]
    fig, ax = plt.subplots()
    ax.set_title(title)
    ax.imshow(tup[0], cmap = 'gray')
    
    for blob in blobs_log:
        y, x, r = blob
        c = plt.Circle((x, y), r, color='red', linewidth=1.5, fill=False)
        ax.add_patch(c)
        ax.set_axis_off()
        
plt.tight_layout()
plt.show()
  


