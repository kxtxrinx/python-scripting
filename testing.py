import pyautogui
import datetime
import time

#hardcoded datastamps to check it works
startHour = 19
startMin = 52

hora_fin = datetime.time(8, 40, 0)  #08:40:00

active = False

#if it's the correct hour...
def clickIt():
    pyautogui.click(470,1000)
    time.sleep(1)
    pyautogui.click(1240,500)
    
#endless loop
while "true" == "true":
    #time.sleep(29)
    print(pyautogui.position())
    currentHour = datetime.datetime.now()
    
    
    if currentHour.hour == startHour and startMin == currentHour.minute:
        if active == False:
            active = True
            clickIt()
            print("test")
        else:
            active = False
            time.sleep(60)
            print("minute's gone")
    
    
    
    
            


         
        
        
        
        





