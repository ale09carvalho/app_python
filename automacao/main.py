sistemafibra.org.br
#Automaçao
import pyautogui as auto
import time

'''
PyAutoGUI permite que seus scripts Python controlem o mouse e o teclado para automatizar interações com outros aplicativos. 
Projetada para ser simples. 

'''

# define o tempo de espera para cada comando do pyautogui, para que os comandos possam ser executados na hora exata
auto.PAUSE = 0.5

auto.press('win') # abre o menu iniciar
auto.write('chrome') # digita na barra de pesquisa do menu iniciar o nome do programa "chrome"
auto.press('enter') # aperta enter após a digitação do nome do programa
auto.hotkey("alt", "space")
auto.press("x")
auto.write("python")#pequisa por python
auto.press('enter')
auto.hotkey("ctrl", "t") # abri uma nova guia
auto.write("sistemafibra.org.br")
auto.press('enter')

'''
O seu computador irá, sozinho, abrir o menu iniciar, digitar na barra de pesquisa edge (nome do navegador da Microsoft), e abrí-lo.
'''
