
'''
Цифрова обробка зображень: фільтрація

'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('Image.JPG')

if img is None:
    print("Image not found")
    exit()

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# 1. Усереднення (Convolution)
kernel = np.ones((5, 5), np.float32) / 25
blur1 = cv2.filter2D(img, -1, kernel)

# 2. Blur
blur2 = cv2.blur(img, (5, 5))

# 3. Gaussian Blur
blur3 = cv2.GaussianBlur(img, (5, 5), 0)

# 4. Median Blur
blur4 = cv2.medianBlur(img, 5)

# 5. Bilateral Filter
blur5 = cv2.bilateralFilter(img, 9, 75, 75)

# показ результатів
titles = ['Original', 'Averaging', 'Blur', 'Gaussian', 'Median', 'Bilateral']
images = [
    img,
    blur1,
    blur2,
    blur3,
    blur4,
    blur5
]

for i in range(6):
    plt.subplot(2, 3, i+1)
    plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.tight_layout()
plt.savefig("result.JPG")
plt.show()

# збереження результатів
cv2.imwrite('image_2026_filter2D.jpg', blur1)
cv2.imwrite('image_2026_blur.jpg', blur2)
cv2.imwrite('image_2026_GaussianBlur.jpg', blur3)
cv2.imwrite('image_2026_medianBlur.jpg', blur4)
cv2.imwrite('image_2026_bilateralFilter.jpg', blur5)

