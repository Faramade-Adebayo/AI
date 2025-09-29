
import cv2

image = cv2.imread("SEPTEMBER29.jpg")

cv2.namedWindow("Loaded Image", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Loaded Image", 800,500)

cv2.imshow("Loaded Image", image)

print(f"Image Dimensions: {image.shape}")

cv2.waitKey(0)
cv2.destroyAllWindows()
