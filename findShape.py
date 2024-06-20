import cv2
import numpy as np
print("package imported")

def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if area > 500:
            cv2.drawContours(imgContour,cnt,-1,(143,0,255),3)
            peri= cv2.arcLength(cnt, True)
            #print(peri)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            #print(approx)
            print(len(approx))
            objCor = len(approx)
            x,y,w,h = cv2.boundingRect(approx)
            if objCor ==3: objectType = "Triangle"
            elif objCor ==4:
                aspRatio = w/float(h)
                if aspRatio > 0.95 and aspRatio < 1.05 : objectType ="Square"
                else: objectType ="Rectangle"
            elif objCor == 5: objectType = "Pentagon"
            elif objCor == 6: objectType = "Hexagon"
            elif objCor == 10: objectType = "Star"
            elif objCor == 8: objectType = "Circle"
            else: objectType ="None"
            #cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(imgContour,objectType,(x+(w//2)-25,y+(h//2+10)),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),2)

img = cv2.imread("Resources/shapes.jpg")
#imgResize = cv2.resize(img,(400,250))
#img = imgResize
imgContour = img.copy()

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)
imgCanny = cv2.Canny(imgBlur,50,50)

getContours(imgCanny)

imgBlank = np.zeros_like(img)

#imgStack = stackImages(([img,imgGray,imgBlur],[imgCanny,imgContour,imgBlank]), 0.6)

cv2.imshow("Contour Image",imgContour)

#cv2.imshow("original",img)
#cv2.imshow("Gray Img",imgGray)
#cv2.imshow("Blur img",imgBlur)

cv2.waitKey(0)