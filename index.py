import PySimpleGUI as sg

def create_window(theme):
    sg.theme(theme)
    sg.set_options(font = 'Calibri 14', button_element_size = (6,3))
    button_size = (6,3)
    layout = [
        [sg.Text('0',
        font = 'Franklin 26', justification = 'right',
        expand_x = True, 
        pad = (10,20),
        right_click_menu = theme_menu, key = '-TEXT-'        
        )],
        [sg.Button('Clear', size = (12,3))],
        [sg.Button(7, size = button_size),sg.Button(8, size = button_size),sg.Button(9, size = button_size),sg.Button('*', size = button_size)],
        [sg.Button(4, size = button_size),sg.Button(5, size = button_size),sg.Button(6, size = button_size),sg.Button('/', size = button_size)],
        [sg.Button(1, size = button_size),sg.Button(2, size = button_size),sg.Button(3, size = button_size),sg.Button('-', size = button_size)],
        [sg.Button(0, expand_x= True),sg.Button('.', size = button_size),sg.Button('+', size = button_size),sg.Button('=', size = button_size)],
    ]
    return sg.Window('Calculator', layout)

theme_menu = ['menu',['LightGrey1','dark','DarkGrey8','random']]
window = create_window('dark')

current_num = ['0']
full_operation = []

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event in theme_menu[1]:
        window.close()
        window = create_window(event)#

    if event in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        window['-TEXT-'].update('')

        # full_operation.reverse()

        # if full_operation and full_operation[0] in event:
        #  full_operation = full_operation.pop()

        current_num = []
        current_num.append(''.join(event))
        num_string = ''. join(current_num)
        window['-TEXT-'].update(num_string)
        print(current_num)
        print(full_operation)

    if event == '.':
        window['-TEXT-'].update('')

        
        current_num.append(''.join(event))
        num_string = ''. join(current_num)
        window['-TEXT-'].update(num_string)
        print(current_num)
        print(full_operation)


    if event in ['+', '-', '/', '*']:

        if current_num:
          full_operation.append(''.join(current_num))  
          current_num = []
          full_operation = list(filter(None, full_operation))

        full_operation.reverse()

        if  full_operation[0] not in event:
            full_operation.reverse()
            result = eval(''.join(full_operation))
            window['-TEXT-'].update(result)
            full_operation.append(event)
            current_num = []

            print(full_operation) 

        else:
           full_operation.reverse()
           full_operation = list(filter(None, full_operation))
           print(full_operation)

    
    if event == '=': 
        # full_operation.reverse()
        # if full_operation[0] == ',':
        #     full_operation.pop()
        #     full_operation.reverse()
        # else:
        #     full_operation.reverse()

        full_operation.append(''.join(current_num))
        full_operation = list(filter(None, full_operation))
        result = eval(''.join(full_operation))
        window['-TEXT-'].update(result)
        current_num = ['0']

        print(current_num)
        print(full_operation)

    if event == 'Clear':
        window['-TEXT-'].update('')
        full_operation = []
        current_num = ['0']
window.close()    