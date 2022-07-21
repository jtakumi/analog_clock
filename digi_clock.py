import PySimpleGUI as psg
from datetime import datetime

psg.theme('DarkTeal11')

layout=[[psg.Text('',key='-time-',font=('',30))],
        [psg.Button('change theme',key='-theme-',size=(7,3))],
        [psg.Button('close',key='-close-',size=(7,3))]]

wnd=psg.Window('digital clock',layout,size=(400,300))

layout2=[[psg.Text('theme browsing')],
        [psg.Text('click theme color')],
        [psg.Listbox(values=psg.theme_list(),size=(20,12),key='-LIST-',enable_events=True)],
        [psg.Button('exit')]]

#レイアウトの内容を読み込む
wnd2=psg.Window('Theme Browser',layout2)

def now():
    ntime=datetime.now()
    nt=ntime.strftime('%H:%M:%S')
    return nt
while True:
    event,values=wnd.read(timeout=10,timeout_key='-timeout-')
    #getting current time
    #when click close button
    if event in (psg.WIN_CLOSED,'-close-'):
        break
    elif event == '-theme-':
        event2,values2 = wnd2.read()
        if event2 in(psg.WIN_CLOSED,'exit'):
            break
        psg.theme(values2['-LIST-'][0])
        psg.popup_get_text('{}'.format(values2['-LIST-'][0]))
        ct=str('{}'.format(values2['-LIST-'][0]))
        psg.theme(ct)
        wnd2.close()
    #update per 10ms
    if event == '-timeout-':
        wnd['-time-'].update(now())
    
wnd.close()