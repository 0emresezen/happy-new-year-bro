#modüller
import pyautogui
import time

#değişkenler

#mesaj kutusu koordinatı
msg_coordinate = (416, 817)
#en alttaki kullanıcının koordinatı
user_coordinate = (182, 741)


#sonsuz döngü
while(True):
    #mouse u en alttaki kullanıcıya getir(1.mönitörü baz alarak koordinatlar girilir)
    pyautogui.moveTo(user_coordinate)
    time.sleep(0.1)
    #tıkla
    pyautogui.click()
    time.sleep(0.1)
    #mesaj kutusuna tıkla
    pyautogui.moveTo(msg_coordinate)
    pyautogui.click
    time.sleep(0.1)
    time.sleep(0.1)
    #mesajı yaz
    pyautogui.typewrite("Happy new year bro")
    time.sleep(0.1)
    #enter a bas
    pyautogui.press('enter')
    time.sleep(0.1)
    #en aşağı in
    pyautogui.scroll(-9999999)
    # mouse u en alttaki kullanıcıya getir
    pyautogui.moveTo(user_coordinate)
    time.sleep(0.1)
    # 1 kullanıcı aşağı tekerleği kullanarak in
    pyautogui.scroll(-80)
    time.sleep(0.1)


