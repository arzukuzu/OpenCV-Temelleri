""""
BU PROJENİN AMACI :
1-Ekranda "Merhaba Mühendis!" yazsın.
2-Kronometre kur.
3-Bu kodda farklı koordinatlarda 2 adet dairen olsun biri sol üst köşede daha büyük, biri sağ altta daha küçük. 
belirlediğin 2 harf bunların renklerini değiştirebilsin. 
4-Işık koşullarının kötü olduğu bir ortamda görüntüyü ters çevir. 
5- pencerede göster , ardından kamerayı serbest bırak ve tüm pencereleri kapat. 

"""

import cv2
import time 

kamera = cv2.VideoCapture(0)
print("Kamera açılıyor, kapatmak için 'q' tuşuna basınız.")

baslangıc = time.time()
renk = (0 , 165 , 255)
mod = "normal"

while True:
  ret,  kare = kamera.read()
  su_an = time.time()
  gecen_zaman= int(su_an - baslangıc)

  cv2.putText(kare, "Merhaba Muhendis!" , (50, 50) , 
              cv2.FONT_HERSHEY_SIMPLEX , 1 , (0, 255, 0) , 2)
  cv2.putText(kare, f"Sure : {gecen_zaman} sn." , (50,85) , 
              cv2.FONT_HERSHEY_SIMPLEX , 1 , (0, 255 ,0), 2)
  
  cv2.circle(kare, (150 , 200) , 50 , (255, 0, 0) , -1)
  cv2.circle(kare, (400 , 400) , 25, renk , -1)



  tus = cv2.waitKey(1) & 0XFF

  if tus == ord('a'):
    renk = (0, 255 , 0)
  elif tus == ord('b'):
    renk = (0 , 0 ,255) 
  elif tus == ord('m'):
    mod = 'negatif'
  elif tus == ord('n'): 
    mod = 'normal'
  elif tus == ord('q'):
    break
  
  if mod == 'negatif':
    kare = cv2.bitwise_not(kare)
    cv2.putText(kare, "Gece surusu aktif!" , (50,110) , 
                cv2.FONT_HERSHEY_SIMPLEX , 1 , (0,255,0), 2)

  cv2.imshow("Modlu Takip",kare )

kamera.release()
cv2.destroyAllWindows()