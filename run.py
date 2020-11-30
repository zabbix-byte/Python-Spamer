from multiprocessing import Process
import time
import pyautogui
import threading
import os
import sys

#funccion combinada de las dos simples
def Combinedloop_0(char, looprange, sleeptime):
    for _ in range(looprange):
        pyautogui.write(char)
        pyautogui.press('enter')
        time.sleep(sleeptime)

#funccion loop simple
def simpleloop_0(char, looprange, sleeptime):
    for _ in range(looprange):
        pyautogui.write(char)
        time.sleep(sleeptime)

#funccion loop simple
def simpleloop_1(looprange, sleeptime):
    for _ in range(looprange):
        pyautogui.press('enter')
        time.sleep(sleeptime)
        
#THREADING
# MENOS PRECISO PERO BASTANTE RAPIDO (8sec/100lops) FIABILIDAD(90%)
def MyThread(char, loops):
    t0 = threading.Thread(target=simpleloop_0, args=(char, loops, 0,))
    t1 = threading.Thread(target=simpleloop_1, args=(loops, 0,))
    t0.start()
    t1.start()
    t0.join()
    t0.join()

#PROCESSING
#MAS PRECISO KE EL THEADING Y IGUAL DE RAPIDO (8sec/100lops) FIABILIDAD(98%)
def MyProcess(char, loops):
    p0 = Process(target=simpleloop_0, args=(char, loops, 0,))
    p1 = Process(target=simpleloop_1, args=(loops, 0,))
    p0.start()
    p1.start()
    p0.join()
    p0.join()

#THREADING + PROCESSING + PARALLELIZATION ( f(n) = θ(g(n)))
#MENOS PRECISO PORQUE FALTA PARALELIZAR LOS CORES I LOS ILOS PERO ES MOCHISIMO MAS RAPISO (3/100 lops sec ) FIABILIDAD(60%)
#SI SE APLICA LA PARALELIZACION Y SINCRONIZACION CORES/ILOS >  CALCULO ESTIMADO (0.5/100 LOPS SEC) FIABILIDAD (99 %)

def CombinedFuncction(char, loops):
    #sincronizador del loop
    loop = int(int(loops) / 3)

    #Ejecucion del trading

    p0 = Process(target=simpleloop_0, args=(char, loop, 0,))

    p1 = Process(target=simpleloop_1, args=(loop, 0,))

    t0 = threading.Thread(target=simpleloop_0, args=(char, loop, 0.1,))

    t1 = threading.Thread(target=simpleloop_1, args=(loop, 0.1,))

    t2 = threading.Thread(target=simpleloop_0, args=(char, loop, 0.0,))

    t3 = threading.Thread(target=simpleloop_0, args=(char, loop, 0.5,))
        
    p0.start()
    p1.start()
    t0.start()
    t1.start()
    t2.start()
    t3.start()

    p0.join()
    p1.join()
    t0.join() 
    t1.join()  
    t2.join()  
    t3.join()

if __name__ == "__main__": 
    time.sleep(2)

    print("""

    SELECCIONA EL CAMPO DE TEXTO
          Z A B B I X
    
    """)

    init_time = time.time()

    char = "prueba"
    loops = 100
    MyProcess(char, loops)

    fin_time = time.time()

    print(f"T I E M P O :  {fin_time - init_time} .S P O R {loops} L O O P S ")