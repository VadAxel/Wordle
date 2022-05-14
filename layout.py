import PySimpleGUI as sg

#Layout vid spel
def layout_func():
    layout = [
    [sg.Text("Wooordle", font='_21')],   
    [sg.HorizontalSeparator(color='black')],
    [sg.Text('', key='string1', font='Raleway')],
    [sg.HorizontalSeparator(color='black')],
    [sg.Text('', key='string2', font='Raleway')],
    [sg.HorizontalSeparator(color='black')],
    [sg.Text('', key='string3', font='Raleway')],
    [sg.HorizontalSeparator(color='black')],    #Få kortare, en string/L
    [sg.Text('', key='string4', font='Raleway')],
    [sg.HorizontalSeparator(color='black')],
    [sg.Text('', key='string5', font='Raleway')],
    [sg.HorizontalSeparator(color='black')],
    [sg.Text('', key='string6', font='Raleway')],
    [sg.HorizontalSeparator(color='black')],
    [sg.B('Enter', bind_return_key=True, key='confirm_button'), sg.B('Nytt Spel', key='new_game_button'), sg.B('Inställningar', key='settings_button')],
    [sg.InputText( key='input_box', do_not_clear = False)],
    [sg.Text('Ditt Score: ', font='_ 15'), sg.VerticalSeparator(color='black'), sg.Text("rätt = rätt bokstav på rätt plats" + "\n" + "rätt ish = rätt bokstav på fel plats" + "\n" + "fel = fel bokstav på fel plats", font='_ 10')],
    [sg.Text('_____ ', font='_ 15', key = 'yiscore')],
    [sg.Text('Top 3! - High Score: ', font='_ 15'), sg.VerticalSeparator(color='black'), sg.Text("För varje fel och halvrätt" + "\n" + "får du 2 respektive 1 poäng." + "\n" + "Du ska därför få så låga" + "\n" + "poäng som möjligt!", font='_ 10')],
    [sg.Text('\n\n\n', font='_ 10', key = 'High_Score')], 
    ]
        
    return layout

#Layout vid val av tema
def layout2_func():
    layout2 = [[sg.T('Denna ruta representerar valt tema, om du vill spela direkt, tryck OK')],
              [sg.Button('Ok'), sg.Button('Ändra tema'), sg.Button('Avsluta')]]
    return layout2