import cv2
import numpy

def main():
    print("""
        SELECT
       1. accept and load a colored image
       2. Output a pixel value
       3. Modify a pixel value
       4. Image dimensions
       5. Image total pixel count.
       6. Image data type
       0. Exit
       """)

    opt = int(input("Select: "))
  
    if opt == 1:
        Grayscale()    
    elif opt == 2:
       OutputVal() 
    elif opt == 3:
        ModifyVal()
    elif opt == 4:
        ImgDim()
    elif opt == 5:
        Pcount()
    elif opt == 6:
        ImgDataType()
    elif opt == 0:
        exit()
    else:
        print("invalid input")
        main()   

def Grayscale():
        img = cv2.imread('Yelan.jpg')
       
        print("accept and load a colored image")
        imgLen = len(img.shape)
        if imgLen >= 3:
            cv2.imshow("colored")
            cv2.waitKey(0)
            main()
        else:
            print("Grayscale")
            main()
def OutputVal():
        img = cv2.imread('Yelan.jpg')
        print("Output a pixel value.")
        x = int(input("for X axis: "))
      
        y = int(input("for Y axis: "))
        color = int(input("Blue - Green - Red "))
        print(img.item(x, y, color))
        cv2.waitKey(0)
        main()

def ModifyVal():
        img = cv2.imread('Yelan.jpg')
        print(" Modify a pixel value.")
        x = int(input("for x axis: "))
      
        y = int(input("for y axis: "))
        print(img[x, y])
        for i in range(0, 3, 1):
            if i == 0:
                print("blue")
                OutputValue = int(input("Pixel Value: "))
            elif i == 1:
                print("green")
                OutputValue = int(input("Pixel Value: "))
            elif i == 2:
                print("red")
                OutputValue = int(input("Pixel Value: "))
        
            img.itemset((x, y, i), OutputValue)
        print(img[x, y])
        cv2.imshow("Colored",img)
        cv2.waitKey(0)
        main()  
def ImgDim():
        img = cv2.imread('Yelan.jpg')
        print(" Image dimensions")
        x = 300
       
        y = 250
        print(img.shape)
        print(f"""
        Total Pixel (X-axis): {img.shape[0]}
        Total Pixel (Y-axis): {img.shape[1]}
        Compared Value in X-axis: {x}
        Compared Value in Y-axis: {y}
        """)
        if x <= img.shape[0] and y <= img.shape[1]:
            print("Within boundaries")
        else:
            print("Out of boundaries")
        cv2.waitKey(0)
        main()

def Pcount():
        img = cv2.imread('Yelan.jpg')
        print("Image total pixel count.")
        x = 300
        
        y = 250
        fixedValue = x * y
        totalPixel = img.shape[0] * img.shape[1]
        print("""
        Total fixed variable: {fixedValue}
        Total image pix: {totalPixel}
        """)
        if fixedValue > totalPixel:
            print("high")
        elif fixedValue < totalPixel:
            print("low")
        else:
            print("equal")
        main()

def ImgDataType():
        img = cv2.imread('Yelan.jpg')
        print("Image data type")
        print("Image data type is: {img.dtype}")
        main()
if __name__  == ("__main__"):
    main()