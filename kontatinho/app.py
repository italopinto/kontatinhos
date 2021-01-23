#!/usr/bin/env python3

import PySimpleGUI as sg
from os import remove, path
from unidecode import unidecode
import string
from time import strftime, gmtime

sg.ChangeLookAndFeel('DarkBlue1')

kontatinho = ""
verify = []
msgm = 'Você ainda não tem kontatinh@s :(\n\nAdicione o primeiro o quanto antes em \"adicionar\" no menu principal!'
# Buttons
contato_add = 'Adicionar contato'
list_view = 'Ver lista'
contato_search = 'Pesquisar contato'
del_contato = 'Apagar contato'
del_all_contato = 'Apagar todos os contatos'
sair = 'Sair'
exclui = 'Excluir'
pesquisa = 'Pesquisar'
volta = 'Voltar'
confirma = 'Confirmar'
editar_ctt = 'Confirmar edição'
y = 'Sim'
n = 'Não'

############################################### CRIACAO DOS LAYOUTS #####################################################


# criar layout menu
def main_menu():
    layout_menu = [
        [sg.Text('Opened: ' + strftime('%d/%m/%Y - %H:%M:%S', gmtime()), text_color='gray')],
        [sg.Button(contato_add, size=(20, 0)), sg.Button(list_view, size=(20, 0))],
        [sg.Button(contato_search, size=(20, 0)), sg.Image('icons/k.png'), sg.Button(del_contato, size=(20, 0))],
        [sg.Button('Editar contato', size=(20, 0),), sg.Button(del_all_contato, button_color=('white', 'red'), size=(20, 0))],
        [sg.Button(sair)],
        [sg.Text('Author: Ítalo Pinto', text_color='gray')]
    ]
    return sg.Window('Kontatinh@s', layout=layout_menu, element_padding=(10, 10), element_justification='center', finalize=True)

# layout janela add ctt
def add_ctt():
    layout_add_ctt = [
        [sg.Text('Digite o nome:')],
        [sg.Input(tooltip='Digite o nome', key='-ADD-')],
        [sg.Text('Digite o número:')],
        [sg.Input(tooltip='Digite o número', key='-NUM-')],
        [sg.Button(confirma, tooltip=confirma),
         sg.Button(volta, tooltip=volta)]
    ]
    return sg.Window('Adicione seu Kontatinh@', layout=layout_add_ctt, finalize=True, return_keyboard_events=True)

# layout janela ver lista
def view_list():
    layout_view_ctt = [
        [sg.Output(size=(55, 10), tooltip=list_view,)],
        [sg.Button(volta, tooltip=volta)]
    ]

    return sg.Window(list_view, layout=layout_view_ctt, margins=(0, 0), finalize=True)

# layout janela pesquisar um contato
def search_ctt():
    layout_search_ctt = [
        [sg.Text('Digite o nome:')],
        [sg.Input(tooltip='Digite o nome', key='-SEA-')],
        [sg.Button(pesquisa, tooltip=pesquisa)],
        [sg.Text('Contato:')],
        [sg.Input(tooltip='Contato', readonly=True, key='-OUT-')],
        [sg.Button(volta, tooltip=volta)]
    ]

    return sg.Window('Pesquisar Kontatinh@', layout=layout_search_ctt, finalize=True)

# layout janela deletar um contato
def del_ctt():
    layout_del_ctt = [
        [sg.Text('Digite o Kontatinh@:')],
        [sg.Input(tooltip='Digite o nome', key='-DEL-')],
        [sg.Button('Pesquisar')],
        [sg.Text('Kontatinh@ a ser deletado:')],
        [sg.Input(tooltip='Kontatinh@', readonly=True, key='-OUTDEL-')],
        [sg.Button(exclui, tooltip=exclui), sg.Button(volta, tooltip=volta)]
    ]
    return sg.Window('Apagar Kontatinh@', layout=layout_del_ctt, finalize=True)

#verifica se deleta o contato de vez
def del_ctt_confirmed():
    layout_del_ctt_confirmed = [
        [sg.Text('Deseja mesmo apagar?')],
        [sg.Button(y, tooltip=y), sg.Button(n, tooltip=n)]
    ]

    return sg.Window('Apagar Kontatinh@', layout=layout_del_ctt_confirmed, element_justification='center', element_padding=(10, 10), size=(280, 100), finalize=True)

# deletar todos os contatos
def del_all_ctt():
    layout_del_all = [
        [sg.Text('Deseja mesmo apagar tudo?')],
        [sg.Button(y, tooltip=y), sg.Button(n, tooltip=n)]
    ]
    return sg.Window('Apagar todos os Kontatinh@s', layout=layout_del_all, element_justification='center', element_padding=(10, 10), size=(280, 100), finalize=True)

# editar contato
def edit_ctt():
    layout_edit = [
        [sg.Text('Digite o Kontatinh@:')],
        [sg.Input(tooltip='Digite o nome', key='-EDT-')],
        [sg.Button('Pesquisar')],
        [sg.Text('--------------------- Edite o contato logo abaixo ---------------------')],
        [sg.Text('Nome:')],
        [sg.Input(tooltip='Nome a ser editado:', key='-NEDT-')],
        [sg.Text('Contato:')],
        [sg.Input(tooltip='Contato a ser editado:', key='-CEDT-')],
        [sg.Button(editar_ctt, tooltip=editar_ctt), sg.Button(volta, tooltip=volta)]
    ]
    return sg.Window('Editar Kontatinh@', layout=layout_edit, finalize=True)


#################################################### FUNCOES ######################################################


# adicionar contato
def add_to_file():
    #tirar tds os acentos (unidecode), tudo para minusculo (lower)
        lowercase_alphabets = list(string.ascii_lowercase)
        phone = unidecode(values.get('-NUM-')).lower() 
        for letter in phone:
            #se tiver letras no numero ou o numero for maior 11 ou o nome estiver vazio não salva
            if letter in lowercase_alphabets or len(phone) > 11 or values.get('-ADD-') == "" or values.get('-NUM-') == "":
                sg.popup_ok('O número digitado é inválido ou o campo nome está vazio.\n\nDigite apenas números, com ou sem o código de área e não esqueça o nome do kontatinh@! ;)', title='ERRO! :(')
                break
            elif letter == phone[len(phone)-1]:  
                sg.popup_ok(f"Kontatinh@ {values.get('-ADD-')} - {values.get('-NUM-')}, adicionado com sucesso!", title='Adicionado!')
                with open('contatos.txt', 'a') as file:
                   file.write(f"{values.get('-ADD-')} {values.get('-NUM-')}\n")
                file.close()
                win2['-ADD-'].update("")
                win2['-NUM-'].update("")
                break

#abrir arquivo para leitura
def open_file(show_ctts):
    file = open('contatos.txt', 'r')
    for linhas in file:
        show_ctts.append(linhas.strip())
    file.close()
    return show_ctts

# ver a lista printada num objeto OUTPUT que funciona como um console
def view_file_list():
    lista = []
    #caso o arquivo não exista
    try:
        #acessando a lista de contatos no txt
        open_file(lista)
    #uso de return dentro da função para parar sua execução, algo como o break nos loops
    except:
        return sg.popup_ok(msgm, title='Adicione um contato!') 
    # caso a lista esteja vasia
    if lista == verify:
        return sg.popup_ok(msgm, title='Adicione um contato')
    # caso já tenha itens na lista
    else:
        print('---------------- Seus Kontatinh@s ----------------\n')
        #unpacking dos contatos na lista
        for y in lista:
            try:
                a, b = y.split() 
                print(f'{a}: {b}')
            except:
                a, b, c = y.split()
                print(f'{a} {b}: {c}')

# pesquisar contato                
def search_file_ctt():
    lista = []
    try:
        #acessando a lista de contatos no txt
        open_file(lista)
    except:
        return sg.popup_ok(msgm, title='Adicione um contato!') 
    # caso a lista esteja vasia
    if lista == verify:
        return sg.popup_ok(msgm, title='Adicione um contato!') 
    else: 
        nome = values.get('-SEA-')
        for y in lista:
            if nome in y:
                #unpacking da linha do txt 'italo 134134' => 'italo', '12313', um para cada variavel, gracas ao split()
                name, number = y.split()
                win4['-OUT-'].update(number)
                break
            #se y for o útimo valor da lista de ctts, e o codigo chegar aqui, então ctt nao encontrado
            elif lista[len(lista)-1] == y:
                return sg.popup_ok('Kontatinh@ não encontrado :(', no_titlebar=True) 

# apagar um contato da lista
def del_file_ctt_search():
    global kontatinho 
    lista = []
    try:
        #acessando a lista de contatos no txt
        open_file(lista)
    except:
        return sg.popup_ok(msgm, title='Adicione um contato!') 
    # caso a lista esteja vasia
    if lista == verify:
        return sg.popup_ok(msgm, title='Adicione um contato!') 
    else: 
        nome = values.get('-DEL-')
        for y in lista:
            if nome in y:
                kontatinho = y
                name, number = y.split()
                win5['-OUTDEL-'].update(f"Nome: {name}, Número: {number}")
                break
            #se y for o útimo valor da lista de ctts, e o codigo chegar aqui, então ctt nao encontrado
            elif lista[len(lista)-1] == y:
                return sg.popup_ok('Kontatinh@ não encontrado :(', no_titlebar=True)

def del_file_ctt_confirmed():
    lista = []
    open_file(lista)
    global kontatinho
    lista.remove(kontatinho)   
    with open('contatos.txt', 'w') as file:
        for lines in lista:
            file.write(f"{lines}\n")
    file.close()
    win5['-DEL-'].update("")
    win5['-OUTDEL-'].update("")   
    return sg.popup_no_buttons('Kontatinh@ excluído com sucesso!', no_titlebar=True, auto_close=True, auto_close_duration=3.5)

#apagar a lista
def del_list():
    if path.exists("contatos.txt") == False:
        return sg.popup_ok(msgm, title='Adicione um contato!')
    else:
        remove("contatos.txt")
        return sg.popup_no_buttons('Todos os Kontatinh@s excluídos com sucesso!', no_titlebar=True, auto_close=True, auto_close_duration=3.5)

#pesquisar contato para editar
def edit_file_ctt_search():
    if values.get('-EDT-') == '':
        return sg.popup_ok('Digite um Kontatinh@ para editar!', title='Digite um Kontatinh@')
    global kontatinho 
    lista = []
    try:
        #acessando a lista de contatos no txt
        open_file(lista)
    except:
        return sg.popup_ok(msgm, title='Adicione um contato!') 
    # caso a lista esteja vasia
    if lista == verify:
        return sg.popup_ok(msgm, title='Adicione um contato!') 
    else: 
        nome = values.get('-EDT-')
        for y in lista:
            if nome in y:
                kontatinho = y
                name, number = y.split()
                win8['-NEDT-'].update(name)
                win8['-CEDT-'].update(number)
                break
            #se y for o útimo valor da lista de ctts, e o codigo chegar aqui, então ctt nao encontrado
            elif lista[len(lista)-1] == y:
                return sg.popup_ok('Kontatinh@ não encontrado :(', no_titlebar=True)

#editar o contato
def edit_confirmed():
    lowercase_alphabets = list(string.ascii_lowercase)
    if values.get('-EDT-') == '' or path.exists("contatos.txt") == False:
        return sg.popup_ok('Não existem kontatinh@s ou você não forneceu um para editar', title='ERRO :(')
    phone = unidecode(values.get('-CEDT-')).lower()
    for letter in phone:
        if letter in lowercase_alphabets or len(phone) > 11 or values.get('-NEDT-') == "" or values.get('-CEDT-') == "":
            return sg.popup_ok('O número digitado é inválido ou o campo nome está vazio.\n\nDigite apenas números, com ou sem o código de área e não esqueça o nome do kontatinh@! ;)', title='ERRO! :(')
        elif letter == phone[len(phone)-1]:
            edited = str(f"{values.get('-NEDT-')} {values.get('-CEDT-')}")
            global kontatinho
            lista = []
            open_file(lista)
            for y in lista:
                if y == kontatinho:
                    lista.remove(y)
                    lista.append(edited)
                    with open('contatos.txt', 'w') as file:
                        for lines in lista:
                            file.write(f"{lines}\n")
                    file.close()
                    win8['-EDT-'].update("")
                    win8['-NEDT-'].update("")
                    win8['-CEDT-'].update("")
                    return sg.popup_no_buttons(f'Kontatinh@ editado com sucesso!', no_titlebar=True, auto_close=True, auto_close_duration=3.5)

###################################################### CHAMANDO AS JANELAS ########################################################


# criando janelas (multiplas janelas) e lendo os eventos
win1, win2, win3, win4, win5, win6, win7, win8, win9 = main_menu(), None, None, None, None, None, None, None, None
# janela 1, menu

while True:
    #chamando todas as janelas
    window, event, values = sg.read_all_windows()

    if window == win1 and event == sg.WIN_CLOSED or event == sair:
        break

# Janela 2, adicionar contato
    elif window == win1 and event == contato_add:
        win2 = add_ctt()
        win1.hide()

    elif window == win2 and event == 'Confirmar':
        add_to_file()

    elif window == win2 and event == volta or event == sg.WIN_CLOSED:
        win2.close()
        win1.un_hide()
    
# Janela 3, ver contatos
    elif window == win1 and event == list_view:
        win3 = view_list()
        win1.hide()
        view_file_list()

    elif window == win3 and event == volta or event == sg.WIN_CLOSED:
        win3.close()
        win1.un_hide()

# Janela 4, pesquisar contatos
    elif window == win1 and event == contato_search:
        win4 = search_ctt()
        win1.hide()

    elif window == win4 and event == pesquisa:
        search_file_ctt()

    elif window == win4 and event == volta or event == sg.WIN_CLOSED:
        win4.close()
        win1.un_hide()

# Janela 5 e 6, pesquisar e deletar contato, respectivamente
    elif window == win1 and event == del_contato:
        win5 = del_ctt()
        win1.hide()

    elif window == win5 and event == pesquisa:
        del_file_ctt_search()

    elif window == win5 and event == exclui:
        win6 = del_ctt_confirmed()
            
    elif window == win6 and event == y:
        win6.close()
        del_file_ctt_confirmed()
    
    elif window == win6 and event == n or event == sg.WIN_CLOSED:
        win6.close()

    elif window == win5 and event == volta or event == sg.WIN_CLOSED:
        win5.close()
        win1.un_hide()

# Janela 7, deletar todos os contatos
    elif window == win1 and event == del_all_contato:
        win7 = del_all_ctt()
        win1.hide()

    elif window == win7 and event == y:
        win7.close()
        del_list()
        win1.un_hide()

    elif window == win7 and event == n or event == sg.WIN_CLOSED:
        win7.close()
        win1.un_hide()

# Janela 8 e 9, edição de nome e numero do contato e confirmação
    elif window == win1 and event == 'Editar contato':
        win8 = edit_ctt()
        win1.hide()

    elif window == win8 and event == pesquisa:
        edit_file_ctt_search()

    elif window == win8 and event == editar_ctt:
        edit_confirmed()

    elif window == win8 and event == volta or event == sg.WIN_CLOSED:
        win8.close()
        win1.un_hide()
