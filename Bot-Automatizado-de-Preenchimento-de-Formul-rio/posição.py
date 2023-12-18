import pyautogui
import time
import cv2
pyautogui.PAUSE=1
pyautogui.FAILSAFE=True


pyautogui.hotkey("win","r")
pyautogui.typewrite("https://docs.google.com/forms/d/e/1FAIpQLSdiKSEUZ21J79XFd7hmF66J1KFUo5uid2RBAoa4FDadpqBjjQ/viewform") 
pyautogui.press("enter")



time.sleep(5)
pyautogui.moveTo(360,476)
pyautogui.moveTo(1359,144)
pyautogui.dragRel(1354,200,duration=0.5)
time.sleep(2)


with open(r"C:\Users\camil\preenchendo cadastro\dados formulario.csv") as f:

    next(f)
    for line in f:
        line=line.strip()
        line=line.split(";")
        print("dados: ",line)
        nome=line[0]
        email=line[1]
        phone=line[2]
        

        pyautogui.locateCenterOnScreen(r"C:\Users\camil\preenchendo cadastro\nome.PNG",confidence=0.8)
        pyautogui.click(pyautogui.locateCenterOnScreen(r"C:\Users\camil\preenchendo cadastro\resposta.png",confidence=0.8),duration=1)
        pyautogui.typewrite(nome, interval =0.25)

        pyautogui.locateCenterOnScreen(r"C:\Users\camil\preenchendo cadastro\email.PNG" , confidence = 0.8)
        pyautogui.click(pyautogui.locateCenterOnScreen(r"C:\Users\camil\preenchendo cadastro\resposta.png", confidence=0.8), duration=1)
        pyautogui.typewrite(email, interval=0.25)
        
        pyautogui.locateCenterOnScreen(r"C:\Users\camil\preenchendo cadastro\telefone.PNG", confidence=0.8)
        pyautogui.click(pyautogui.locateCenterOnScreen(r"C:\Users\camil\preenchendo cadastro\resposta.png", confidence=0.8), duration=1)
        pyautogui.typewrite(phone, interval=0.25)

     

       


        


        pyautogui.click(pyautogui.locateCenterOnScreen(r"C:\Users\camil\preenchendo cadastro\enviar.PNG",confidence=0.8),duration=1)

        time.sleep(3)
       

pyautogui.alert(text="cadastro finalizado",title="aviso ", button ="confirma")
      