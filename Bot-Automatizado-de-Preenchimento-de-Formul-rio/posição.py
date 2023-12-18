import pyautogui
import time
import cv2
pyautogui.PAUSE=1
pyautogui.FAILSAFE=True

pyautogui.hotkey("win","r")
pyautogui.typewrite("https://docs.google.com/forms/d/e/1FAIpQLSdiKSEUZ21J79XFd7hmF66J1KFUo5uid2RBAoa4FDadpqBjjQ/viewform") 
pyautogui.press("enter")

time.sleep(5)

with open(r"C:\Users\camil\cadastro1\Bot-Automatizado-de-Preenchimento-de-Formul-rio\dados formulario.csv") as f:

    next(f)
    for line in f:
        
        line=line.strip()
        line=line.split(";")
        print("dados: ",line)
        nome=line[0]
        data=line[1]
        matricula=line[2]

        pyautogui.click(417,433)
        time.sleep(2)    
        pyautogui.moveTo(1359,144)
        pyautogui.dragRel(1354,200,duration=0.5)
        time.sleep(2)      

        pyautogui.locateCenterOnScreen(r"C:\Users\camil\cadastro1\Bot-Automatizado-de-Preenchimento-de-Formul-rio\nome completo.PNG",confidence=0.8)
        pyautogui.click(pyautogui.locateCenterOnScreen(r"C:\Users\camil\cadastro1\Bot-Automatizado-de-Preenchimento-de-Formul-rio\resp.PNG",confidence=0.8),duration=1)
        pyautogui.typewrite(nome, interval =0.25)

        pyautogui.locateCenterOnScreen(r"C:\Users\camil\cadastro1\Bot-Automatizado-de-Preenchimento-de-Formul-rio\data nnascimento.PNG", confidence = 0.8)
        pyautogui.click(pyautogui.locateCenterOnScreen(r"c:\Users\camil\cadastro1\Bot-Automatizado-de-Preenchimento-de-Formul-rio\data resp.PNG", confidence=0.8), duration=1)
        pyautogui.typewrite(data, interval=0.25)
        
        pyautogui.locateCenterOnScreen(r"C:\Users\camil\cadastro1\Bot-Automatizado-de-Preenchimento-de-Formul-rio\matricula.PNG", confidence=0.8)
        pyautogui.click(pyautogui.locateCenterOnScreen(r"C:\Users\camil\preenchendo cadastro\resposta.png", confidence=0.8), duration=1)
        pyautogui.typewrite(matricula, interval=0.25)

        pyautogui.click(pyautogui.locateCenterOnScreen(r"C:\Users\camil\preenchendo cadastro\enviar.PNG",confidence=0.8),duration=1)
        pyautogui.click(pyautogui.locateAllOnScreen(r"C:\Users\camil\cadastro1\Bot-Automatizado-de-Preenchimento-de-Formul-rio\novamente.PNG", confidence=0.8), duration=1)
        

        time.sleep(3)
       
pyautogui.alert(text="cadastro finalizado",title="aviso ", button ="confirma")
      
