#Paasso a passo do projeto

#Passo 1 - entrar no sistema da empresa: https://dlp.hashtagtreinamentos.com/python/intensivao/login

#Passo 2 - Fazer login no sistema

#Passo 3 - importar a base de dados

#Passo 4 - Cadastrar um produto 

#Passo 5 - Repetir isto até acabar a base de dados

import pyautogui
import time
     
# clicar > pyautogui.click
# escrever > pyautogui.write
# aperter uma tecla > pyautogui.press
# apertar > pyautogui.notkey("ctrl", 'C')
# scroll (rolar) > pyautogui.scroll

#Passo 1 - entrar no sistema da empresa: https://dlp.hashtagtreinamentos.com/python/intensivao/login

# Comando para deixar mais lento
pyautogui.PAUSE = 1
# Aperta a teclado do win
pyautogui.press("win")
# digita o nome do programa
pyautogui.write("Chrome")
# Apertar enter
pyautogui.press("enter")
# digitar o links
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
# apertar o enter
pyautogui.press("enter")
# Espera 5 segundos
time.sleep(5)


#Passo 2 - Fazer login no sistema
pyautogui.click(x=-565, y=447)

#digita o email
pyautogui.write("pythonimpressionador@gmail.com")
#passar para o campo de senha
pyautogui.press("tab")
#digitar a senha
pyautogui.write("senha")
#Fazer login
pyautogui.click(x=-613, y=613)

#Passo 3 - importar a base de dados

import pandas

tabela = pandas.read_csv("produtos.csv")

for linha in tabela.index:

    #Passo 4 - Cadastrar um produto 
    pyautogui.click(x=-492, y=321)

    #Codigo
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")
    #marca
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")
    #tipo
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")
    #categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    #preco
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    #custo
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    #obs
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs)
# Enviar o produto  2   2   25.0    
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(5000)

















