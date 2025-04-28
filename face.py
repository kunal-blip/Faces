import cv2

a = cv2.CascadeClassifier("Resource/haarcascade_frontalface_default.xml")

b = cv2.VideoCapture(0)

while True:
       c_rectangale, d_img = b.read()
       e = cv2.cvtColor(d_img, cv2.COLOR_BGR2GRAY)
       f = a.detectMultiScale(e, 1.3,6)

       for (x_axis,y_axis,width,height) in f:
              cv2.rectangle(d_img,(x_axis,y_axis),(x_axis+width, y_axis+height), (255,0,0),7)

       cv2.imshow('img',d_img)
       h = cv2.waitKey(10) & 0xff
       if h == 10:
              break

b.release()
cv2.destroyAllWindows()