from imageio import imread

fname = 'beach.jpeg'

# load an RGB image
data = imread(fname)


red = data[..., 0]
green = data[..., 1]
blue = data[..., 2]


# Average
gray = (red + green + blue) / 3.
print(gray)


# Luminocity
gray2 = 0.21 * red + 0.72 * green + 0.07 * blue

from pylab import figure, title, imshow, hist, grid, show

figure()
title('Original color image')
imshow(data)

figure()
title('Gray image by averaging')
imshow(gray, cmap='gray')

figure()
title('Gray image by luminocity formula')
imshow(gray2, cmap='gray')


# How would you take a patch or region of interest
# (ROI) from an image?

# How would you segment (separate) the sky from the rest?

mask = gray2 < 100
figure()
title('Showing binary mask')
imshow(mask, cmap='gray')


gray3 = gray2.copy()
gray3[mask] = 0
figure()
imshow(gray3, cmap='gray')

gray4 = gray2.copy()
mask2 = blue > 240
gray4[mask2] = 0
figure()
imshow(gray4, cmap='gray')

# Lets get the histogram

figure()
n, bins, patches = hist(gray2.ravel(), 50, alpha=0.75)
grid()

show()













