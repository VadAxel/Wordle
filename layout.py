import PySimpleGUI as sg

def layout_func():
    layout = [
    [sg.Text("Wooordle", font='_21')],  
    [sg.HorizontalSeparator(color='black')],
    [sg.Text('', key='string1', font='Raleway')],
    [sg.HorizontalSeparator(color='black')],
    [sg.Text('', key='string2')],
    [sg.HorizontalSeparator(color='black')],
    [sg.Text('', key='string3')],
    [sg.HorizontalSeparator(color='black')],    #Få kortare, en string/L
    [sg.Text('', key='string4')],
    [sg.HorizontalSeparator(color='black')],
    [sg.Text('', key='string5')],
    [sg.HorizontalSeparator(color='black')],
    [sg.Text('', key='string6')],
    [sg.HorizontalSeparator(color='black')],
    [sg.B('Enter', bind_return_key=True, key='confirm_button')],
    [sg.InputText( key='input_box', do_not_clear = False)],
    [sg.Text('Eller tryck enter\nDitt Score: ', font='_ 15')],
    [sg.Text('_____ ', font='_ 15', key = 'yiscore')],
    [sg.Text('Top 3! - High Score: ', font='_ 15')],
    [sg.Text('\n\n\n', font='_ 10', key = 'High_Score')], 
    ]
        
    return layout

    
def layout2_func():
    layout2 = [[sg.T('Denna ruta representerar valt tema')],
              [sg.Button('Ok'), sg.Button('Ändra tema'), sg.Button('Avsluta')]]
    return layout2