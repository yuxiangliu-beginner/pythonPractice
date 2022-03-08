import cv2


img = cv2.imread("galaxy.jpg",0)

print(type(img))
print(img)
print(img.shape)
print(img.ndim)


#resize image (image object, tuple(height,width)), height and width must be integer
resized_img = cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))

#write image into new file
cv2.imwrite("galaxy_resized.jpg",resized_img)

# #show image
# cv2.imshow("galaxy",resized_img)
# # 0 means user press any to close the window
# # other is the time in millioseconds
# cv2.waitKey(0)
# cv2.destroyAllWindows()


import glob
images = glob.glob("sample_images/*.jpg")
print(images)
for image in images:
    # print(image)
    imag = cv2.imread(image,0)
    rz = cv2.resize(imag,(100,100))
    # cv2.imshow("hey",rz)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    cv2.imwrite("resized_"+image,rz)
