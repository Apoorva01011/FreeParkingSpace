import cv2
cap=cv2.VideoCapture(0);
fourcc=cv2.VideoWriter_fourcc('X','V','I','D')
out=cv2.VideoWriter("output.avi",fourcc,20,(640,480))
print(cap.isOpened())
while(cap.isOpened()):
  ret,frame=cap.read()
  if ret==True:
      grey=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
      print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
      print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
      out.write(frame)
      cv2.imshow("frame",grey)
  if cv2.waitKey(1) &  0xFF==ord('q'):
    break
cap.release()
out.release()
cv2.destroyAllWindows()
