# Desenvolvido por K.r.s
# github: https://github.com/IK-R-S

''' Esse código foi desenvolvido com o intuito educacional.
    É um projeto open source 100% livre para você utilizar,
    desenvolver melhorias e se inspirar para seus proejetos.

    *Copiar o código dos outros é feio, utilize mas ajude a melhorar
     o código base que aqui se encontra. Obrigado.
'''

from PySimpleGUI.PySimpleGUI import T, WIN_CLOSED, button_color_to_tuple
import PySimpleGUI as sg

sg.theme('Reddit')

layout = [

    [sg.Text('Nome do elemento:', size=(32,1)), sg.InputText()],
    [sg.Text('Massa Molecular do elemento', size=(32,1)), sg.Input()],
    [sg.Text('Quantidade da amostra em Gramas (g)', size=(32,1)), sg.Input()],

    [sg.Button('Calcular mol', size=(64,3), border_width=3, font=('Helvetica', 13))],
    [sg.Button('Sair', button_color='red', size=(29,2)), sg.Button('Tutorial', button_color='green', size=(32,2))]

]

window = sg.Window('Calculadora de mols', layout, size=(500,200))

while True:
    event, values = window.read()

    if event == WIN_CLOSED or event == 'Sair':
        window.close()
        break
    
    elif event == 'Tutorial':
        sg.popup('Você só precisa pegar a massa molar do elemento na tabela periódica e também fornecer a massa em gramas da amostra, o resto é moleza.', title='Como calcular o mol',)

    elif event == 'Calcular mol':
        nome = str(values[0])
        mmol = float(values[1])
        m = float(values[2])
        a = (6.02*(10**23)*m)/mmol
        sg.popup(f'{a}', font=('Helvetica', 18),title='Número de atómos/moléculas')
