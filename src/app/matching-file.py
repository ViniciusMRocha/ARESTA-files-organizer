from PIL import Image
import imagehash
hash0 = imagehash.average_hash(Image.open('../data/Flag-Page.jpg'))
hash1 = imagehash.average_hash(Image.open('../data/Flag-Page2.jpg'))
cutoff = 5

print(hash0)
print(hash1)

if hash0 - hash1 < cutoff:
    print('images are similar')
else:
    print('images are not similar')

# import cv2
# import numpy as np
# from matplotlib import pyplot as plt

# img = cv2.imread('../data/Flag-Page.jpg', 0)
# img2 = img.copy()
# template = cv2.imread('../data/Flag-Simbole.jpg', 0)
# w, h = template.shape[::-1]

# # All the 6 methods for comparison in a list
# methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
#            'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

# for meth in methods:
#     img = img2.copy()
#     method = eval(meth)

#     # Apply template Matching
#     res = cv2.matchTemplate(img, template, method)
#     min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

#     # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
#     if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
#         top_left = min_loc
#         print(top_left)
#     else:
#         top_left = max_loc
#         print(top_left)
#     bottom_right = (top_left[0] + w, top_left[1] + h)

#     cv2.rectangle(img, top_left, bottom_right, 255, 2)

#     plt.subplot(121), plt.imshow(res, cmap='gray')
#     plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
#     plt.subplot(122), plt.imshow(img, cmap='gray')
#     plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
#     plt.suptitle(meth)

#     plt.show()


# import cv2

# method = cv2.TM_SQDIFF_NORMED

# # Read the images from the file
# small_image = cv2.imread('../data/Flag-Simbole.jpg')
# large_image = cv2.imread('../data/Flag-Page.jpg')

# result = cv2.matchTemplate(small_image, large_image, method)

# # We want the minimum squared difference
# mn, _, mnLoc, _ = cv2.minMaxLoc(result)

# # Draw the rectangle:
# # Extract the coordinates of our best match
# MPx, MPy = mnLoc

# # Step 2: Get the size of the template. This is the same size as the match.
# trows, tcols = small_image.shape[:2]

# # Step 3: Draw the rectangle on large_image
# cv2.rectangle(large_image, (MPx, MPy), (MPx+tcols, MPy+trows), (0, 0, 255), 2)

# # Display the original image with the rectangle around the match.
# cv2.imshow('output', large_image)

# # The image is only displayed if we call this
# cv2.waitKey(0)

# import cv2
# import numpy as np
# small_image = cv2.imread('../data/Flag-Simbole.jpg')
# large_image = cv2.imread('../data/Flag-Page.jpg')
# img_rgb = cv2.imread('../data/Flag-Page.jpg')
# template = cv2.imread('../data/Flag-Simbole.jpg')
# w, h = template.shape[:-1]

# res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)

# threshold = .9
# loc = np.where(res >= threshold)
# print(loc)
# for pt in zip(*loc[::-1]):  # Switch collumns and rows
#     cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

# cv2.imwrite('result.png', img_rgb)
