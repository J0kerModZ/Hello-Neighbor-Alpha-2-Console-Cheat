import pyautogui
import keyboard
import time

def toggle_debug_camera():
    pyautogui.typewrite('`')
    time.sleep(0.1)
    pyautogui.typewrite("ToggleDebugCamera")
    time.sleep(0.1)
    pyautogui.press('enter')

def fly():
    pyautogui.typewrite('`')
    time.sleep(0.1)
    pyautogui.typewrite("Fly")
    time.sleep(0.1)
    pyautogui.press('enter')

def ghost():
    pyautogui.typewrite('`')
    time.sleep(0.1)
    pyautogui.typewrite("Ghost")
    time.sleep(0.1)
    pyautogui.press('enter')    

def PlayersOnly():
    pyautogui.typewrite('`')
    time.sleep(0.1)
    pyautogui.typewrite("PlayersOnly")
    time.sleep(0.1)
    pyautogui.press('enter')

def TP():
    pyautogui.typewrite('`')
    time.sleep(0.1)
    pyautogui.typewrite("Teleport")
    time.sleep(0.1)
    pyautogui.press('enter')
    
def ShowNav():
    pyautogui.typewrite('`')
    time.sleep(0.1)
    pyautogui.typewrite("Show Navigation")
    time.sleep(0.1)
    pyautogui.press('enter')
    
def Grow():
    pyautogui.typewrite('`')
    time.sleep(0.1)
    pyautogui.typewrite("ChangeSize 5")
    time.sleep(0.1)
    pyautogui.press('enter')
    
def Srink():
    pyautogui.typewrite('`')
    time.sleep(0.1)
    pyautogui.typewrite("ChangeSize 0.5")
    time.sleep(0.1)
    pyautogui.press('enter')
    
def FixSize():
    pyautogui.typewrite('`')
    time.sleep(0.1)
    pyautogui.typewrite("ChangeSize 1")
    time.sleep(0.1)
    pyautogui.press('enter')

def walk():
    pyautogui.typewrite('`')
    time.sleep(0.1)
    pyautogui.typewrite("Walk")
    time.sleep(0.1)
    pyautogui.press('enter')

def restart():
    pyautogui.typewrite('`')
    time.sleep(0.1)
    pyautogui.typewrite("RestartLevel")
    time.sleep(0.1)
    pyautogui.press('enter')

def main():
    TopBanner = r"""
    /$$$$$  /$$$$$$  /$$                           /$$      /$$                 /$$ /$$$$$$$$
   |__  $$ /$$$_  $$| $$                          | $$$    /$$$                | $$|_____ $$ 
      | $$| $$$$\ $$| $$   /$$  /$$$$$$   /$$$$$$ | $$$$  /$$$$  /$$$$$$   /$$$$$$$     /$$/ 
      | $$| $$ $$ $$| $$  /$$/ /$$__  $$ /$$__  $$| $$ $$/$$ $$ /$$__  $$ /$$__  $$    /$$/  
 /$$  | $$| $$\ $$$$| $$$$$$/ | $$$$$$$$| $$  \__/| $$  $$$| $$| $$  \ $$| $$  | $$   /$$/   
| $$  | $$| $$ \ $$$| $$_  $$ | $$_____/| $$      | $$\  $ | $$| $$  | $$| $$  | $$  /$$/    
|  $$$$$$/|  $$$$$$/| $$ \  $$|  $$$$$$$| $$      | $$ \/  | $$|  $$$$$$/|  $$$$$$$ /$$$$$$$$
 \______/  \______/ |__/  \__/ \_______/|__/      |__/     |__/ \______/  \_______/|________/
                                                                                             
    """

    print(TopBanner)
    print("THIS ONLY WORKS FOR ALPHA 2, When you see this Open Hello Neighbor and press the buttons in game!\n\n")
    print("Press '1' to execute ToggleDebugCamera command.")
    print("Press '2' to execute Fly command.")
    print("Press '3' to execute Ghost command.")
    print("Press '4' to execute PlayersOnly command.")
    print("Press '6' to Stop Flying")
    print("Press '7' to execute Teleport command.")
    print("Press '8' to Show Navigation")
    print("Press '9' to Grow")
    print("Press '0' to Srink")
    print("Press '-' to Fix Size")
    print("Press 'R' to Retart Level")
    print("Press 'Q' to quit the program.")

    while True:
        if keyboard.is_pressed('1'):
            toggle_debug_camera()
            time.sleep(0.5)

        elif keyboard.is_pressed('2'):
            fly()
            time.sleep(0.5)

        elif keyboard.is_pressed('3'):
            ghost()
            time.sleep(0.5) 

        elif keyboard.is_pressed('4'):
            PlayersOnly()
            time.sleep(0.5)    

        elif keyboard.is_pressed('6'):
            walk()
            time.sleep(0.5) 

        elif keyboard.is_pressed('7'):
            TP()
            time.sleep(0.5)     

        elif keyboard.is_pressed('8'):
            ShowNav()
            time.sleep(0.5) 

        elif keyboard.is_pressed('9'):
            Grow()
            time.sleep(0.5) 

        elif keyboard.is_pressed('0'):
            Srink()
            time.sleep(0.5) 

        elif keyboard.is_pressed('-'):
            FixSize()
            time.sleep(0.5) 

        elif keyboard.is_pressed('r'):
            restart()
            time.sleep(0.5) 

        elif keyboard.is_pressed('q'):
            break

if __name__ == "__main__":
    main()
