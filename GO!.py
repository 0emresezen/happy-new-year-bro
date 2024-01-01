#modüller
import pyautogui
import time

#değişkenler



#mesaj kutusu koordinatı
msg_coordinate = (256, 947)
#en alttaki kullanıcının koordinatı
user_coordinate = (500, 986)

time.sleep(5)
#sonsuz döngü
while(True):
    
    #mouse u en alttaki kullanıcıya getir(1.mönitörü baz alarak koordinatlar girilir)
    pyautogui.moveTo(user_coordinate)
    time.sleep(0.2)
    #tıkla
    pyautogui.click()
    
    time.sleep(0.2)
    #mesaj kutusuna tıkla
    pyautogui.moveTo(msg_coordinate)
    pyautogui.click()
    time.sleep(0.1)
    #mesajı yaz
    pyautogui.typewrite("Happy new year bro!!!!")
    time.sleep(0.1)
    #enter a bas
    pyautogui.press('enter')
    time.sleep(0.1)
    #mouse u aşağı inmek için barın konumuna al
    pyautogui.moveTo(user_coordinate)
    time.sleep(0.1)
    #en aşağı in
    pyautogui.scroll(-9999999)
    time.sleep(0.1)
   



