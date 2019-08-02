from PIL import Image
import os
import matplotlib.pyplot as plt

basedir = os.path.dirname(__file__)
filename_1='C:/Users/Joel/Desktop/Python/1.jpg'

img=Image.open(filename_1)
plt.figure("1")

plt.imshow(img)

plt.show()