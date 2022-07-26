import PySimpleGUI as sg
from datetime import datetime
import tkinter.font




#レイアウトの内容を読み込む



def now():
    ntime=datetime.now()
    nt=ntime.strftime('%H:%M:%S')
    return nt

def make_window(theme,cfont):
    if theme:
        sg.theme(theme)
    layout=[[sg.Text('',key='-time-',font=(cfont,40),justification='center')],
        [sg.Button('change theme',key='-theme-',size=(10,3))],
        [sg.Button('change clock font',key='-font-',size=(10,3))],
        [sg.Button('close',key='-close-',size=(10,3))]]

    return sg.Window('digital clock',layout,size=(300,250))    
    

def main():
    cfont='Times New Roman'
    theme='Black'
    wnd=make_window(theme,cfont)

    while True:
        event,values=wnd.read(timeout=10,timeout_key='-timeout-')
        #getting current time
        #when click close button
        #update per 10ms
        if event == '-timeout-':
            wnd['-time-'].update(now())

        if event in (sg.WIN_CLOSED,'-close-'):
            break

        #changing theme
        if event == '-theme-':
            #layout and window create
            event,values = sg.Window('Theme Browser',
            [[sg.Text('theme browsing')],
            [sg.Text('click theme color')],
            [sg.Combo(values=sg.theme_list(),size=(20,12),key='-LIST-',readonly=True)],
            [sg.OK(),sg.Cancel()]]).read(close=True)

            #when OK button click, changing theme
            if event == 'OK':
                theme=values['-LIST-']
                wnd.close()
                wnd= make_window(theme,cfont) 
        #changing font
        if event == '-font-':
            #layout and window create
            event,values = sg.Window('Font Browser',
            [[sg.Text('Font browsing')],
            [sg.Text('click font')],
            [sg.Combo(values=tkinter.font.families(),size=(20,12),key='-FONT-',readonly=True)],
            [sg.OK(),sg.Cancel()]]).read(close=True)

            #when OK button click, changing font
            if event == 'OK':
                cfont=values['-FONT-']
                wnd.close()
                wnd= make_window(theme,cfont)
                
            
    wnd.close()

if __name__ == '__main__':
    main()