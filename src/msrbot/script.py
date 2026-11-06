import pyautogui as pg
import pandas as pd
import time, random

from .helper import resource_path

def pesquisar_automaticamente():
    pg.PAUSE = 1 

    pg.press('Win')
    pg.write('edge')
    pg.press('enter')
    time.sleep(1) 
    pg.hotkey("alt", "space")
    pg.press("x")
    time.sleep(1) 
    pg.hotkey("ctrl", "l")
    pg.write('https://rewards.bing.com/')
    pg.press('enter')
    pg.hotkey('ctrl', 't')

    caminho_seguro = resource_path('times_brasileiros.csv')
    tabela = pd.read_csv(caminho_seguro)

    for i in range(0, 40): # -> número de pesquisas
        indice = random.randint(1, 100)
        team = tabela.loc[indice, 'Time']
        pg.write(str(team))
        pg.press('enter')
        time.sleep(1) 
        pg.hotkey('ctrl', 'w')
        pg.hotkey('ctrl', 't')
        pg.hotkey("ctrl", "l")

    return None