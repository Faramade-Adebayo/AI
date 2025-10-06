import cv2
import numpy as np
import matplotlib.pyplot as plt

def show_image(title,image):
    plt.imshow(image, cmap='gray')
    plt.title(title)
    plt.axis('off')
    plt.show()

image = cv2.imread('sept29.jpeg')
if image is None:
    print('Erroe:Imahe not Found!')
else:
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    show_image("Originally Grayscale Image", gray)

    print("Choose an option.")
    print("1.Sobel Edge Detector")
    print("2. Canny Edge Detector")
    print("Gaussian Blur(Smoothing)")
    print("4. Exit")
 
    while True:
        choice=input("Enter your choice:")
         
        if choice == '1':
           sobelx=cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
           sobely=cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
           sobel_combined=cv2.bitwise_or(sobelx.astype(np.uint8),sobely.astype(np.uint8))
           show_image("Sobel Edge Detection", sobel_combined)

        elif choice=='2':
            print("Enter threshold {defult 100 and 200}")
            t1=int(input('Lower Threshold:'))
            t2=int(input('Upper Threshold:'))
            edges=cv2.Canny(gray,t1,t2)
            show_image("Canny edges Detection ", edges)
        elif choice=="3":
            print("Enter Kernel size {odd humber,e.g, 5}")
            k=int(input('Kernel size:'))
            edges=cv2.GaussianBlur(gray,(k,k),0)            
            show_image("Gaussian Blurred Image ", blurred)
        
        elif choice == '4':
             print("Exiting.........")
             break
        else :
            print("Invalid choice.Enter 1-4")


