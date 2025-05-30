import matplotlib.pyplot as plt
import numpy as np

#low-pass filter (looked this up online)
def box_filter(image, size=5):
    # Reflect-pad the image so we index neighbors near borders
    pad = size // 2
    padded = np.pad(image, pad_width=pad, mode='reflect')
    
    out = np.zeros_like(image)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            # Extract local 
            region = padded[i : i+size, j : j+size]
            out[i, j] = region.mean()
    return out


img = plt.imread('/Users/merterol/Desktop/iMac27_github/uzh/Computational Science/Sem 4/PHY124/Exercise 7/21.png')
img2 = plt.imread('/Users/merterol/Desktop/iMac27_github/uzh/Computational Science/Sem 4/PHY124/Exercise 7/holbein.png')

# end up with a 2D version of the image
if img.ndim == 3:
    gray = img[..., :3].mean(axis=2) # grab RGB and average it into (height, width)
else:
    gray = img

blurred = box_filter(gray, size=35)  # try different sizes (5,9,15,...)

plt.figure(figsize=(6, 6))
plt.imshow(blurred, cmap='gray')
plt.title('Blurred Image')
plt.axis('off')
plt.show()
