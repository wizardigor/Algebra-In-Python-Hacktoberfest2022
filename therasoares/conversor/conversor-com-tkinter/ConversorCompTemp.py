from tkinter import *
from tkinter import ttk


# alterna entre as janelas substituindo-as
def raise_frame(frame):
    frame.tkraise()


def converte_temp():
    if str(va_ctemp.get()).isnumeric():
        temp_eva = int(va_ctemp.get())
        temp_ua = cb_ctempa.get()
        temp_uf = cb_ctempf.get()
        # Se unidade atual = s
        if temp_ua == "seg" and temp_uf == "min":
            temp_vf = temp_eva / 60
            vf_ctempf["text"] = temp_vf

        elif temp_ua == "seg" and temp_uf == "h":
            temp_vf = temp_eva / 3600
            vf_ctempf["text"] = temp_vf

        # Se unidade atual = m
        if temp_ua == "min" and temp_uf == "seg":
            temp_vf = temp_eva * 60
            vf_ctempf["text"] = temp_vf

        elif temp_ua == "min" and temp_uf == "h":
            temp_vf = temp_eva / 60
            vf_ctempf["text"] = temp_vf

        # Se unidade atual = h
        if temp_ua == "h" and temp_uf == "min":
            temp_vf = temp_eva * 60
            vf_ctempf["text"] = temp_vf

        elif temp_ua == "h" and temp_uf == "seg":
            temp_vf = temp_eva * 3600
            vf_ctempf["text"] = temp_vf

    else:
        vf_ctempf["text"] = "Valor inválido"


def converte_comp():
    if str(va_ccomp.get()).isalpha():
        vf_ccompf["text"] = "Valor inválido"

    else:
        comp_eva = float(va_ccomp.get())
        comp_ua = cb_ccompa.get()
        comp_uf = cb_ccompf.get()
        comp_vua = diccomp[comp_ua]
        comp_vuf = diccomp[comp_uf]
        comp_vf = float((comp_vua / comp_vuf) * comp_eva)
        vf_ccompf["text"] = comp_vf


janela = Tk()
janela.rowconfigure(0, weight=1)
janela.columnconfigure(0, weight=1)
janela.state('zoomed')

# TELAS
bgmenu = PhotoImage(file='bgmenu.png')
bgmenu = bgmenu.subsample(1, 1)
bg_ctemp = PhotoImage(file='bgctemp.png')
bg_ctemp = bg_ctemp.subsample(1, 1)
bg_ccomp = PhotoImage(file='bgccomp.png')
bg_ccomp = bg_ccomp.subsample(1, 1)
iconeVoltar = PhotoImage(file='voltar.png')


menup = Frame(janela)
ctemp = Frame(janela)
ccomp = Frame(janela)

for frames in (menup, ctemp, ccomp):
    frames.grid(row=0, column=0, sticky='nsew')

# Menu
lb_bg_menu = Label(menup, image=bgmenu)
lb_bg_menu.place(x=0, y=0, relwidth=1.0, relheight=1.0)
menu_pag_title = Label(menup, text='Conversor de medidas', font="Courier 35 bold")
menu_pag_title.place(x=100, y=100)
btctemp = Button(menup, width=10, text='Tempo', font="Courier 20", command=lambda: raise_frame(ctemp))
btctemp.place(x=310, y=200)
btccomp = Button(menup, width=15, text='Comprimento', font="Courier 20", command=lambda: raise_frame(ccomp))
btccomp.place(x=265, y=290)

# Conversor de Tempo
lb_bg_ctemp = Label(ctemp, image=bg_ctemp)
lb_bg_ctemp.place(x=0, y=0, relwidth=1.0, relheight=1.0)
# titulo
ctemp_pag_title = Label(ctemp, text='Conversor de medidas de Tempo', font="Courier 35 bold")
ctemp_pag_title.place(x=500, y=100)
vmenu1 = Button(ctemp, image=iconeVoltar, command=lambda: raise_frame(menup))
vmenu1.place(x=10, y=10)
und_ctemp = ['min', 'seg', 'h']
# caixa para o valor atual
tcb_ctempav = Label(ctemp, text='valor atual', font="Courier 20")
tcb_ctempav.place(x=570, y=200)
va_ctemp = Entry(ctemp, font="Courier 20")
va_ctemp.place(x=570, y=250)

tcb_ctempa = Label(ctemp, text='Unidade de Tempo atual', font="Courier 20")
tcb_ctempa.place(x=950, y=200)
cb_ctempa = ttk.Combobox(ctemp, font="Courier 20", values=und_ctemp)
cb_ctempa.place(x=950, y=250)
#####botão converter
btctemp = Button(ctemp, text='Converter', font="Courier 20", command=lambda: converte_temp())
btctemp.place(x=830, y=350)

tvf_ctempf = Label(ctemp, text='Valor Final', font="Courier 20")
tvf_ctempf.place(x=570, y=450)
vf_ctempf = Label(ctemp, text=' ', font="Courier 20")
vf_ctempf.place(x=570, y=500)
tcb_ctempf = Label(ctemp, text='Unidade de Tempo final', font="Courier 20")
tcb_ctempf.place(x=950, y=450)
cb_ctempf = ttk.Combobox(ctemp, font="Courier 20", values=und_ctemp)
cb_ctempf.place(x=950, y=500)

# Conversor de Comprimento
lb_bg_ccomp = Label(ccomp, image=bg_ccomp)
lb_bg_ccomp.place(x=0, y=0, relwidth=1.0, relheight=1.0)
#####titulo
ccomp_pag_title = Label(ccomp, text='Conversor de medidas de comprimento', font="Courier 35 bold")
ccomp_pag_title.place(x=230, y=100)
vmenu2 = Button(ccomp, image=iconeVoltar, command=lambda: raise_frame(menup))
vmenu2.place(x=10, y=10)
diccomp = {'km': 10 ** 3, 'hm': 10 ** 2, 'dam': 10 ** 1, 'm': 10 ** 0, 'dm': 10 ** -1, 'cm': 10 ** -2, 'mm': 10 ** -3}
und_ccomp = list(diccomp.keys())
#####caixa para o valor atual
tcb_ccompav = Label(ccomp, text='valor atual', font="Courier 20")
tcb_ccompav.place(x=250, y=200)
va_ccomp = Entry(ccomp, font="Courier 20")
va_ccomp.place(x=250, y=250)
#####combobox unidade atual
tcb_ccompa = Label(ccomp, text='Unidade de Comprimento atual', font="Courier 20")
tcb_ccompa.place(x=750, y=200)
cb_ccompa = ttk.Combobox(ccomp, font="Courier 20", values=und_ccomp)
cb_ccompa.place(x=750, y=250)
#####botão converter
btccomp = Button(ccomp, text='Converter', font="Courier 20", command=lambda: converte_comp())
btccomp.place(x=550, y=350)
#####label valor final (convertido)
tvf_ccompf = Label(ccomp, text='Valor Final', font="Courier 20")
tvf_ccompf.place(x=250, y=450)
vf_ccompf = Label(ccomp, text=' ', font="Courier 20")
vf_ccompf.place(x=250, y=500)
#####combobox unidade final
tcb_ccompf = Label(ccomp, text='Unidade de Comprimento final', font="Courier 20")
tcb_ccompf.place(x=750, y=450)
cb_ccompf = ttk.Combobox(ccomp, font="Courier 20", values=und_ccomp)
cb_ccompf.place(x=750, y=500)

raise_frame(menup)

janela.mainloop()
