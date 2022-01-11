#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 6.2
#  in conjunction with Tcl version 8.6
#    Jan 11, 2022 10:01:55 AM CET  platform: Windows NT

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import MainWindow_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = MainWindow (root)
    MainWindow_support.init(root, top)
    root.mainloop()

w = None
def create_MainWindow(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_MainWindow(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = MainWindow (w)
    MainWindow_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_MainWindow():
    global w
    w.destroy()
    w = None

class MainWindow:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font9 = "-family {Segoe UI} -size 9"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font=font9)
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("1317x467+-26+167")
        top.minsize(120, 1)
        top.maxsize(2110, 1418)
        top.resizable(1,  1)
        top.title("Station météo")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.FrameEtat = tk.Frame(top)
        self.FrameEtat.place(relx=0.0, rely=0.942, relheight=0.054
                , relwidth=0.831)
        self.FrameEtat.configure(relief='sunken')
        self.FrameEtat.configure(borderwidth="2")
        self.FrameEtat.configure(relief="sunken")
        self.FrameEtat.configure(background="#d9d9d9")
        self.FrameEtat.configure(highlightbackground="#d9d9d9")
        self.FrameEtat.configure(highlightcolor="black")

        self.MsgEtat = tk.Message(self.FrameEtat)
        self.MsgEtat.place(relx=0.003, rely=0.08, relheight=0.84, relwidth=0.037)

        self.MsgEtat.configure(background="#d9d9d9")
        self.MsgEtat.configure(font="-family {Segoe UI} -size 9")
        self.MsgEtat.configure(foreground="#000000")
        self.MsgEtat.configure(highlightbackground="#d9d9d9")
        self.MsgEtat.configure(highlightcolor="black")
        self.MsgEtat.configure(text='''État :''')
        self.MsgEtat.configure(width=60)

        self.Etat = tk.Label(self.FrameEtat)
        self.Etat.place(relx=0.037, rely=0.16, height=17, width=468)
        self.Etat.configure(activebackground="#f9f9f9")
        self.Etat.configure(activeforeground="black")
        self.Etat.configure(anchor='w')
        self.Etat.configure(background="#d9d9d9")
        self.Etat.configure(disabledforeground="#a3a3a3")
        self.Etat.configure(font="-family {Segoe UI} -size 9")
        self.Etat.configure(foreground="#000000")
        self.Etat.configure(highlightbackground="#d9d9d9")
        self.Etat.configure(highlightcolor="black")
        self.Etat.configure(text='''Mesures en cours ...''')

        self.FrameEMes = tk.LabelFrame(top)
        self.FrameEMes.place(relx=0.008, rely=0.021, relheight=0.867
                , relwidth=0.38)
        self.FrameEMes.configure(relief='groove')
        self.FrameEMes.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.FrameEMes.configure(foreground="black")
        self.FrameEMes.configure(text='''Mesures électriques''')
        self.FrameEMes.configure(background="#d9d9d9")
        self.FrameEMes.configure(highlightbackground="#d9d9d9")
        self.FrameEMes.configure(highlightcolor="black")

        self.MsgEGirouette = tk.Message(self.FrameEMes)
        self.MsgEGirouette.place(relx=0.04, rely=0.074, relheight=0.054
                , relwidth=0.16, bordermode='ignore')
        self.MsgEGirouette.configure(anchor='e')
        self.MsgEGirouette.configure(background="#d9d9d9")
        self.MsgEGirouette.configure(font="-family {Segoe UI} -size 9")
        self.MsgEGirouette.configure(foreground="#000000")
        self.MsgEGirouette.configure(highlightbackground="#d9d9d9")
        self.MsgEGirouette.configure(highlightcolor="black")
        self.MsgEGirouette.configure(text='''Girouette''')
        self.MsgEGirouette.configure(width=80)

        self.EGirouette = tk.Label(self.FrameEMes)
        self.EGirouette.place(relx=0.2, rely=0.074, height=21, width=54
                , bordermode='ignore')
        self.EGirouette.configure(activebackground="#f9f9f9")
        self.EGirouette.configure(activeforeground="black")
        self.EGirouette.configure(anchor='e')
        self.EGirouette.configure(background="#d9d9d9")
        self.EGirouette.configure(disabledforeground="#a3a3a3")
        self.EGirouette.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.EGirouette.configure(foreground="#000000")
        self.EGirouette.configure(highlightbackground="#d9d9d9")
        self.EGirouette.configure(highlightcolor="black")
        self.EGirouette.configure(relief="sunken")
        self.EGirouette.configure(text='''9,999 V''')

        self.MsgEAnemometre = tk.Message(self.FrameEMes)
        self.MsgEAnemometre.place(relx=0.04, rely=0.173, relheight=0.057
                , relwidth=0.16, bordermode='ignore')
        self.MsgEAnemometre.configure(anchor='e')
        self.MsgEAnemometre.configure(background="#d9d9d9")
        self.MsgEAnemometre.configure(font="-family {Segoe UI} -size 9")
        self.MsgEAnemometre.configure(foreground="#000000")
        self.MsgEAnemometre.configure(highlightbackground="#d9d9d9")
        self.MsgEAnemometre.configure(highlightcolor="black")
        self.MsgEAnemometre.configure(text='''Anémomètre''')
        self.MsgEAnemometre.configure(width=80)

        self.EAnemometre = tk.Label(self.FrameEMes)
        self.EAnemometre.place(relx=0.2, rely=0.173, height=21, width=54
                , bordermode='ignore')
        self.EAnemometre.configure(activebackground="#f9f9f9")
        self.EAnemometre.configure(activeforeground="black")
        self.EAnemometre.configure(anchor='e')
        self.EAnemometre.configure(background="#d9d9d9")
        self.EAnemometre.configure(disabledforeground="#a3a3a3")
        self.EAnemometre.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.EAnemometre.configure(foreground="#000000")
        self.EAnemometre.configure(highlightbackground="#d9d9d9")
        self.EAnemometre.configure(highlightcolor="black")
        self.EAnemometre.configure(relief="sunken")
        self.EAnemometre.configure(text='''0''')

        self.MsgEThermometre = tk.Message(self.FrameEMes)
        self.MsgEThermometre.place(relx=0.04, rely=0.272, relheight=0.057
                , relwidth=0.16, bordermode='ignore')
        self.MsgEThermometre.configure(anchor='e')
        self.MsgEThermometre.configure(background="#d9d9d9")
        self.MsgEThermometre.configure(font="-family {Segoe UI} -size 9")
        self.MsgEThermometre.configure(foreground="#000000")
        self.MsgEThermometre.configure(highlightbackground="#d9d9d9")
        self.MsgEThermometre.configure(highlightcolor="black")
        self.MsgEThermometre.configure(text='''Thermomètre''')
        self.MsgEThermometre.configure(width=80)

        self.EThermometre = tk.Label(self.FrameEMes)
        self.EThermometre.place(relx=0.2, rely=0.272, height=21, width=54
                , bordermode='ignore')
        self.EThermometre.configure(activebackground="#f9f9f9")
        self.EThermometre.configure(activeforeground="black")
        self.EThermometre.configure(anchor='e')
        self.EThermometre.configure(background="#d9d9d9")
        self.EThermometre.configure(disabledforeground="#a3a3a3")
        self.EThermometre.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.EThermometre.configure(foreground="#000000")
        self.EThermometre.configure(highlightbackground="#d9d9d9")
        self.EThermometre.configure(highlightcolor="black")
        self.EThermometre.configure(relief="sunken")
        self.EThermometre.configure(text='''9,999 V''')

        self.MsgELuxmetre = tk.Message(self.FrameEMes)
        self.MsgELuxmetre.place(relx=0.04, rely=0.37, relheight=0.054
                , relwidth=0.16, bordermode='ignore')
        self.MsgELuxmetre.configure(anchor='e')
        self.MsgELuxmetre.configure(background="#d9d9d9")
        self.MsgELuxmetre.configure(font="-family {Segoe UI} -size 9")
        self.MsgELuxmetre.configure(foreground="#000000")
        self.MsgELuxmetre.configure(highlightbackground="#d9d9d9")
        self.MsgELuxmetre.configure(highlightcolor="black")
        self.MsgELuxmetre.configure(text='''Luxmètre''')
        self.MsgELuxmetre.configure(width=80)

        self.ELuxmetre = tk.Label(self.FrameEMes)
        self.ELuxmetre.place(relx=0.2, rely=0.37, height=21, width=54
                , bordermode='ignore')
        self.ELuxmetre.configure(activebackground="#f9f9f9")
        self.ELuxmetre.configure(activeforeground="black")
        self.ELuxmetre.configure(anchor='e')
        self.ELuxmetre.configure(background="#d9d9d9")
        self.ELuxmetre.configure(disabledforeground="#a3a3a3")
        self.ELuxmetre.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.ELuxmetre.configure(foreground="#000000")
        self.ELuxmetre.configure(highlightbackground="#d9d9d9")
        self.ELuxmetre.configure(highlightcolor="black")
        self.ELuxmetre.configure(relief="sunken")
        self.ELuxmetre.configure(text='''9,999 V''')

        self.MsgEHumidimetre = tk.Message(self.FrameEMes)
        self.MsgEHumidimetre.place(relx=0.04, rely=0.469, relheight=0.054
                , relwidth=0.16, bordermode='ignore')
        self.MsgEHumidimetre.configure(anchor='e')
        self.MsgEHumidimetre.configure(background="#d9d9d9")
        self.MsgEHumidimetre.configure(font="-family {Segoe UI} -size 9")
        self.MsgEHumidimetre.configure(foreground="#000000")
        self.MsgEHumidimetre.configure(highlightbackground="#d9d9d9")
        self.MsgEHumidimetre.configure(highlightcolor="black")
        self.MsgEHumidimetre.configure(text='''Humidimètre''')
        self.MsgEHumidimetre.configure(width=80)

        self.EHumidimetre = tk.Label(self.FrameEMes)
        self.EHumidimetre.place(relx=0.2, rely=0.469, height=21, width=54
                , bordermode='ignore')
        self.EHumidimetre.configure(activebackground="#f9f9f9")
        self.EHumidimetre.configure(activeforeground="black")
        self.EHumidimetre.configure(anchor='e')
        self.EHumidimetre.configure(background="#d9d9d9")
        self.EHumidimetre.configure(disabledforeground="#a3a3a3")
        self.EHumidimetre.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.EHumidimetre.configure(foreground="#000000")
        self.EHumidimetre.configure(highlightbackground="#d9d9d9")
        self.EHumidimetre.configure(highlightcolor="black")
        self.EHumidimetre.configure(relief="sunken")
        self.EHumidimetre.configure(text='''999 Hz''')

        self.MsgEPluviometre = tk.Message(self.FrameEMes)
        self.MsgEPluviometre.place(relx=0.04, rely=0.568, relheight=0.054
                , relwidth=0.16, bordermode='ignore')
        self.MsgEPluviometre.configure(anchor='e')
        self.MsgEPluviometre.configure(background="#d9d9d9")
        self.MsgEPluviometre.configure(font="-family {Segoe UI} -size 9")
        self.MsgEPluviometre.configure(foreground="#000000")
        self.MsgEPluviometre.configure(highlightbackground="#d9d9d9")
        self.MsgEPluviometre.configure(highlightcolor="black")
        self.MsgEPluviometre.configure(text='''Pluviomètre''')
        self.MsgEPluviometre.configure(width=80)

        self.EPluviometre = tk.Label(self.FrameEMes)
        self.EPluviometre.place(relx=0.2, rely=0.568, height=21, width=54
                , bordermode='ignore')
        self.EPluviometre.configure(activebackground="#f9f9f9")
        self.EPluviometre.configure(activeforeground="black")
        self.EPluviometre.configure(anchor='e')
        self.EPluviometre.configure(background="#d9d9d9")
        self.EPluviometre.configure(disabledforeground="#a3a3a3")
        self.EPluviometre.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.EPluviometre.configure(foreground="#000000")
        self.EPluviometre.configure(highlightbackground="#d9d9d9")
        self.EPluviometre.configure(highlightcolor="black")
        self.EPluviometre.configure(relief="sunken")
        self.EPluviometre.configure(text='''0''')

        self.BtnReset = ttk.Button(self.FrameEMes)
        self.BtnReset.place(relx=0.3, rely=0.568, height=25, width=26
                , bordermode='ignore')
        self.BtnReset.configure(takefocus="")
        self.BtnReset.configure(text='''0''')
        self.BtnReset.bind('<ButtonRelease-1>',lambda e:MainWindow_support.GUIBtnReset(e))

        self.MsgEEncodeur = tk.Message(self.FrameEMes)
        self.MsgEEncodeur.place(relx=0.04, rely=0.667, relheight=0.054
                , relwidth=0.16, bordermode='ignore')
        self.MsgEEncodeur.configure(anchor='e')
        self.MsgEEncodeur.configure(background="#d9d9d9")
        self.MsgEEncodeur.configure(font="-family {Segoe UI} -size 9")
        self.MsgEEncodeur.configure(foreground="#000000")
        self.MsgEEncodeur.configure(highlightbackground="#d9d9d9")
        self.MsgEEncodeur.configure(highlightcolor="black")
        self.MsgEEncodeur.configure(text='''Encodeur''')
        self.MsgEEncodeur.configure(width=80)

        self.EEncodeur = tk.Label(self.FrameEMes)
        self.EEncodeur.place(relx=0.2, rely=0.667, height=21, width=54
                , bordermode='ignore')
        self.EEncodeur.configure(activebackground="#f9f9f9")
        self.EEncodeur.configure(activeforeground="black")
        self.EEncodeur.configure(anchor='e')
        self.EEncodeur.configure(background="#d9d9d9")
        self.EEncodeur.configure(disabledforeground="#a3a3a3")
        self.EEncodeur.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.EEncodeur.configure(foreground="#000000")
        self.EEncodeur.configure(highlightbackground="#d9d9d9")
        self.EEncodeur.configure(highlightcolor="black")
        self.EEncodeur.configure(relief="sunken")
        self.EEncodeur.configure(text='''0''')

        self.EP1_0 = tk.Label(self.FrameEMes)
        self.EP1_0.place(relx=0.37, rely=0.667, height=21, width=10
                , bordermode='ignore')
        self.EP1_0.configure(activebackground="#f9f9f9")
        self.EP1_0.configure(activeforeground="black")
        self.EP1_0.configure(background="#d9d9d9")
        self.EP1_0.configure(disabledforeground="#a3a3a3")
        self.EP1_0.configure(font="-family {Segoe UI} -size 9")
        self.EP1_0.configure(foreground="#000000")
        self.EP1_0.configure(highlightbackground="#d9d9d9")
        self.EP1_0.configure(highlightcolor="black")
        self.EP1_0.configure(relief="raised")

        self.EP1_3 = tk.Label(self.FrameEMes)
        self.EP1_3.place(relx=0.31, rely=0.667, height=21, width=10
                , bordermode='ignore')
        self.EP1_3.configure(activebackground="#f9f9f9")
        self.EP1_3.configure(activeforeground="black")
        self.EP1_3.configure(background="#d9d9d9")
        self.EP1_3.configure(disabledforeground="#a3a3a3")
        self.EP1_3.configure(font="-family {Segoe UI} -size 9")
        self.EP1_3.configure(foreground="#000000")
        self.EP1_3.configure(highlightbackground="#d9d9d9")
        self.EP1_3.configure(highlightcolor="black")
        self.EP1_3.configure(relief="raised")

        self.EP1_2 = tk.Label(self.FrameEMes)
        self.EP1_2.place(relx=0.33, rely=0.667, height=21, width=10
                , bordermode='ignore')
        self.EP1_2.configure(activebackground="#f9f9f9")
        self.EP1_2.configure(activeforeground="black")
        self.EP1_2.configure(background="#d9d9d9")
        self.EP1_2.configure(disabledforeground="#a3a3a3")
        self.EP1_2.configure(font="-family {Segoe UI} -size 9")
        self.EP1_2.configure(foreground="#000000")
        self.EP1_2.configure(highlightbackground="#d9d9d9")
        self.EP1_2.configure(highlightcolor="black")
        self.EP1_2.configure(relief="raised")

        self.EP1_1 = tk.Label(self.FrameEMes)
        self.EP1_1.place(relx=0.35, rely=0.667, height=21, width=10
                , bordermode='ignore')
        self.EP1_1.configure(activebackground="#f9f9f9")
        self.EP1_1.configure(activeforeground="black")
        self.EP1_1.configure(background="#d9d9d9")
        self.EP1_1.configure(disabledforeground="#a3a3a3")
        self.EP1_1.configure(font="-family {Segoe UI} -size 9")
        self.EP1_1.configure(foreground="#000000")
        self.EP1_1.configure(highlightbackground="#d9d9d9")
        self.EP1_1.configure(highlightcolor="black")
        self.EP1_1.configure(relief="raised")

        self.MsgEDureeMesures = tk.Message(self.FrameEMes)
        self.MsgEDureeMesures.place(relx=0.02, rely=0.765, relheight=0.057
                , relwidth=0.18, bordermode='ignore')
        self.MsgEDureeMesures.configure(anchor='e')
        self.MsgEDureeMesures.configure(background="#d9d9d9")
        self.MsgEDureeMesures.configure(font="-family {Segoe UI} -size 9")
        self.MsgEDureeMesures.configure(foreground="#000000")
        self.MsgEDureeMesures.configure(highlightbackground="#d9d9d9")
        self.MsgEDureeMesures.configure(highlightcolor="black")
        self.MsgEDureeMesures.configure(text='''Durée mesures''')
        self.MsgEDureeMesures.configure(width=90)

        self.EDureeMesures = tk.Label(self.FrameEMes)
        self.EDureeMesures.place(relx=0.2, rely=0.765, height=21, width=54
                , bordermode='ignore')
        self.EDureeMesures.configure(activebackground="#f9f9f9")
        self.EDureeMesures.configure(activeforeground="black")
        self.EDureeMesures.configure(anchor='e')
        self.EDureeMesures.configure(background="#d9d9d9")
        self.EDureeMesures.configure(disabledforeground="#a3a3a3")
        self.EDureeMesures.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.EDureeMesures.configure(foreground="#000000")
        self.EDureeMesures.configure(highlightbackground="#d9d9d9")
        self.EDureeMesures.configure(highlightcolor="black")
        self.EDureeMesures.configure(relief="sunken")
        self.EDureeMesures.configure(text='''9999 ms''')

        self.MsgETempsBoucleR = tk.Message(self.FrameEMes)
        self.MsgETempsBoucleR.place(relx=0.02, rely=0.914, relheight=0.057
                , relwidth=0.28, bordermode='ignore')
        self.MsgETempsBoucleR.configure(anchor='e')
        self.MsgETempsBoucleR.configure(background="#d9d9d9")
        self.MsgETempsBoucleR.configure(font="-family {Segoe UI} -size 9")
        self.MsgETempsBoucleR.configure(foreground="#000000")
        self.MsgETempsBoucleR.configure(highlightbackground="#d9d9d9")
        self.MsgETempsBoucleR.configure(highlightcolor="black")
        self.MsgETempsBoucleR.configure(text='''Temps de boucle rapide''')
        self.MsgETempsBoucleR.configure(width=140)

        self.ETempsBoucleR = tk.Label(self.FrameEMes)
        self.ETempsBoucleR.place(relx=0.3, rely=0.914, height=21, width=54
                , bordermode='ignore')
        self.ETempsBoucleR.configure(activebackground="#f9f9f9")
        self.ETempsBoucleR.configure(activeforeground="black")
        self.ETempsBoucleR.configure(anchor='e')
        self.ETempsBoucleR.configure(background="#d9d9d9")
        self.ETempsBoucleR.configure(disabledforeground="#a3a3a3")
        self.ETempsBoucleR.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.ETempsBoucleR.configure(foreground="#000000")
        self.ETempsBoucleR.configure(highlightbackground="#d9d9d9")
        self.ETempsBoucleR.configure(highlightcolor="black")
        self.ETempsBoucleR.configure(relief="sunken")
        self.ETempsBoucleR.configure(text='''9999 ms''')

        self.MsgETempsBoucleL = tk.Message(self.FrameEMes)
        self.MsgETempsBoucleL.place(relx=0.56, rely=0.914, relheight=0.057
                , relwidth=0.28, bordermode='ignore')
        self.MsgETempsBoucleL.configure(anchor='e')
        self.MsgETempsBoucleL.configure(background="#d9d9d9")
        self.MsgETempsBoucleL.configure(font="-family {Segoe UI} -size 9")
        self.MsgETempsBoucleL.configure(foreground="#000000")
        self.MsgETempsBoucleL.configure(highlightbackground="#d9d9d9")
        self.MsgETempsBoucleL.configure(highlightcolor="black")
        self.MsgETempsBoucleL.configure(text='''Temps de boucle lente''')
        self.MsgETempsBoucleL.configure(width=140)

        self.ETempsBoucleL = tk.Label(self.FrameEMes)
        self.ETempsBoucleL.place(relx=0.84, rely=0.914, height=21, width=54
                , bordermode='ignore')
        self.ETempsBoucleL.configure(activebackground="#f9f9f9")
        self.ETempsBoucleL.configure(activeforeground="black")
        self.ETempsBoucleL.configure(anchor='e')
        self.ETempsBoucleL.configure(background="#d9d9d9")
        self.ETempsBoucleL.configure(disabledforeground="#a3a3a3")
        self.ETempsBoucleL.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.ETempsBoucleL.configure(foreground="#000000")
        self.ETempsBoucleL.configure(highlightbackground="#d9d9d9")
        self.ETempsBoucleL.configure(highlightcolor="black")
        self.ETempsBoucleL.configure(relief="sunken")
        self.ETempsBoucleL.configure(text='''9999 ms''')

        self.EChartGirouette = tk.Canvas(self.FrameEMes)
        self.EChartGirouette.place(relx=0.46, rely=0.074, relheight=0.353
                , relwidth=0.506, bordermode='ignore')
        self.EChartGirouette.configure(background="#ffffff")
        self.EChartGirouette.configure(borderwidth="2")
        self.EChartGirouette.configure(highlightbackground="#d9d9d9")
        self.EChartGirouette.configure(highlightcolor="black")
        self.EChartGirouette.configure(insertbackground="black")
        self.EChartGirouette.configure(selectbackground="blue")
        self.EChartGirouette.configure(selectforeground="white")

        self.EGraphHumidite = tk.Canvas(self.FrameEMes)
        self.EGraphHumidite.place(relx=0.46, rely=0.469, relheight=0.353
                , relwidth=0.506, bordermode='ignore')
        self.EGraphHumidite.configure(background="#ffffff")
        self.EGraphHumidite.configure(borderwidth="2")
        self.EGraphHumidite.configure(highlightbackground="#d9d9d9")
        self.EGraphHumidite.configure(highlightcolor="black")
        self.EGraphHumidite.configure(insertbackground="black")
        self.EGraphHumidite.configure(selectbackground="blue")
        self.EGraphHumidite.configure(selectforeground="white")

        self.Msg1 = tk.Message(self.FrameEMes)
        self.Msg1.place(relx=0.32, rely=0.074, relheight=0.057, relwidth=0.122
                , bordermode='ignore')
        self.Msg1.configure(anchor='w')
        self.Msg1.configure(background="#d9d9d9")
        self.Msg1.configure(font="-family {Segoe UI} -size 9")
        self.Msg1.configure(foreground="#000000")
        self.Msg1.configure(highlightbackground="#d9d9d9")
        self.Msg1.configure(highlightcolor="black")
        self.Msg1.configure(text='''>>>>>>''')
        self.Msg1.configure(width=61)

        self.Msg2 = tk.Message(self.FrameEMes)
        self.Msg2.place(relx=0.32, rely=0.469, relheight=0.057, relwidth=0.122
                , bordermode='ignore')
        self.Msg2.configure(anchor='w')
        self.Msg2.configure(background="#d9d9d9")
        self.Msg2.configure(font="-family {Segoe UI} -size 9")
        self.Msg2.configure(foreground="#000000")
        self.Msg2.configure(highlightbackground="#d9d9d9")
        self.Msg2.configure(highlightcolor="black")
        self.Msg2.configure(text='''>>>>>>''')
        self.Msg2.configure(width=61)

        self.Entry1 = tk.Entry(self.FrameEMes)
        self.Entry1.place(relx=0.36, rely=0.84, height=20, relwidth=0.168
                , bordermode='ignore')
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="-family {Courier New} -size 10")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="blue")
        self.Entry1.configure(selectforeground="white")

        self.MesureP = tk.LabelFrame(top)
        self.MesureP.place(relx=0.418, rely=0.021, relheight=0.867
                , relwidth=0.539)
        self.MesureP.configure(relief='groove')
        self.MesureP.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.MesureP.configure(foreground="black")
        self.MesureP.configure(text='''Mesures Physique''')
        self.MesureP.configure(background="#d9d9d9")
        self.MesureP.configure(highlightbackground="#d9d9d9")
        self.MesureP.configure(highlightcolor="black")

        self.DirectVent = tk.Message(self.MesureP)
        self.DirectVent.place(relx=0.028, rely=0.074, relheight=0.054
                , relwidth=0.113, bordermode='ignore')
        self.DirectVent.configure(anchor='e')
        self.DirectVent.configure(background="#d9d9d9")
        self.DirectVent.configure(font="-family {Segoe UI} -size 9")
        self.DirectVent.configure(foreground="#000000")
        self.DirectVent.configure(highlightbackground="#d9d9d9")
        self.DirectVent.configure(highlightcolor="black")
        self.DirectVent.configure(text='''DirectVent''')
        self.DirectVent.configure(width=80)

        self.PDirection = tk.Label(self.MesureP)
        self.PDirection.place(relx=0.141, rely=0.074, height=21, width=74
                , bordermode='ignore')
        self.PDirection.configure(activebackground="#f9f9f9")
        self.PDirection.configure(activeforeground="black")
        self.PDirection.configure(anchor='e')
        self.PDirection.configure(background="#d9d9d9")
        self.PDirection.configure(disabledforeground="#a3a3a3")
        self.PDirection.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.PDirection.configure(foreground="#000000")
        self.PDirection.configure(highlightbackground="#d9d9d9")
        self.PDirection.configure(highlightcolor="black")
        self.PDirection.configure(relief="sunken")
        self.PDirection.configure(text='''9,999''')

        self.VVent = tk.Message(self.MesureP)
        self.VVent.place(relx=0.028, rely=0.173, relheight=0.057, relwidth=0.113
                , bordermode='ignore')
        self.VVent.configure(anchor='e')
        self.VVent.configure(background="#d9d9d9")
        self.VVent.configure(font="-family {Segoe UI} -size 9")
        self.VVent.configure(foreground="#000000")
        self.VVent.configure(highlightbackground="#d9d9d9")
        self.VVent.configure(highlightcolor="black")
        self.VVent.configure(text='''Vitesse Vent''')
        self.VVent.configure(width=80)

        self.PVitesse = tk.Label(self.MesureP)
        self.PVitesse.place(relx=0.141, rely=0.173, height=21, width=54
                , bordermode='ignore')
        self.PVitesse.configure(activebackground="#f9f9f9")
        self.PVitesse.configure(activeforeground="black")
        self.PVitesse.configure(anchor='e')
        self.PVitesse.configure(background="#d9d9d9")
        self.PVitesse.configure(disabledforeground="#a3a3a3")
        self.PVitesse.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.PVitesse.configure(foreground="#000000")
        self.PVitesse.configure(highlightbackground="#d9d9d9")
        self.PVitesse.configure(highlightcolor="black")
        self.PVitesse.configure(relief="sunken")
        self.PVitesse.configure(text='''0''')

        self.Temp = tk.Message(self.MesureP)
        self.Temp.place(relx=0.028, rely=0.272, relheight=0.057, relwidth=0.113
                , bordermode='ignore')
        self.Temp.configure(anchor='e')
        self.Temp.configure(background="#d9d9d9")
        self.Temp.configure(font="-family {Segoe UI} -size 9")
        self.Temp.configure(foreground="#000000")
        self.Temp.configure(highlightbackground="#d9d9d9")
        self.Temp.configure(highlightcolor="black")
        self.Temp.configure(text='''Temperature''')
        self.Temp.configure(width=80)

        self.PTemperature = tk.Label(self.MesureP)
        self.PTemperature.place(relx=0.141, rely=0.272, height=21, width=54
                , bordermode='ignore')
        self.PTemperature.configure(activebackground="#f9f9f9")
        self.PTemperature.configure(activeforeground="black")
        self.PTemperature.configure(anchor='e')
        self.PTemperature.configure(background="#d9d9d9")
        self.PTemperature.configure(disabledforeground="#a3a3a3")
        self.PTemperature.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.PTemperature.configure(foreground="#000000")
        self.PTemperature.configure(highlightbackground="#d9d9d9")
        self.PTemperature.configure(highlightcolor="black")
        self.PTemperature.configure(relief="sunken")
        self.PTemperature.configure(text='''9,999''')

        self.Lumi = tk.Message(self.MesureP)
        self.Lumi.place(relx=0.028, rely=0.37, relheight=0.054, relwidth=0.113
                , bordermode='ignore')
        self.Lumi.configure(anchor='e')
        self.Lumi.configure(background="#d9d9d9")
        self.Lumi.configure(font="-family {Segoe UI} -size 9")
        self.Lumi.configure(foreground="#000000")
        self.Lumi.configure(highlightbackground="#d9d9d9")
        self.Lumi.configure(highlightcolor="black")
        self.Lumi.configure(text='''Luminosite''')
        self.Lumi.configure(width=80)

        self.PLuminosite = tk.Label(self.MesureP)
        self.PLuminosite.place(relx=0.141, rely=0.37, height=21, width=54
                , bordermode='ignore')
        self.PLuminosite.configure(activebackground="#f9f9f9")
        self.PLuminosite.configure(activeforeground="black")
        self.PLuminosite.configure(anchor='e')
        self.PLuminosite.configure(background="#d9d9d9")
        self.PLuminosite.configure(disabledforeground="#a3a3a3")
        self.PLuminosite.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.PLuminosite.configure(foreground="#000000")
        self.PLuminosite.configure(highlightbackground="#d9d9d9")
        self.PLuminosite.configure(highlightcolor="black")
        self.PLuminosite.configure(relief="sunken")
        self.PLuminosite.configure(text='''9,999''')

        self.Humi = tk.Message(self.MesureP)
        self.Humi.place(relx=0.028, rely=0.469, relheight=0.054, relwidth=0.113
                , bordermode='ignore')
        self.Humi.configure(anchor='e')
        self.Humi.configure(background="#d9d9d9")
        self.Humi.configure(font="-family {Segoe UI} -size 9")
        self.Humi.configure(foreground="#000000")
        self.Humi.configure(highlightbackground="#d9d9d9")
        self.Humi.configure(highlightcolor="black")
        self.Humi.configure(text='''Humidite''')
        self.Humi.configure(width=80)

        self.PHumidite = tk.Label(self.MesureP)
        self.PHumidite.place(relx=0.141, rely=0.469, height=21, width=54
                , bordermode='ignore')
        self.PHumidite.configure(activebackground="#f9f9f9")
        self.PHumidite.configure(activeforeground="black")
        self.PHumidite.configure(anchor='e')
        self.PHumidite.configure(background="#d9d9d9")
        self.PHumidite.configure(disabledforeground="#a3a3a3")
        self.PHumidite.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.PHumidite.configure(foreground="#000000")
        self.PHumidite.configure(highlightbackground="#d9d9d9")
        self.PHumidite.configure(highlightcolor="black")
        self.PHumidite.configure(relief="sunken")
        self.PHumidite.configure(text='''999''')

        self.Pluvi = tk.Message(self.MesureP)
        self.Pluvi.place(relx=0.028, rely=0.568, relheight=0.054, relwidth=0.113
                , bordermode='ignore')
        self.Pluvi.configure(anchor='e')
        self.Pluvi.configure(background="#d9d9d9")
        self.Pluvi.configure(font="-family {Segoe UI} -size 9")
        self.Pluvi.configure(foreground="#000000")
        self.Pluvi.configure(highlightbackground="#d9d9d9")
        self.Pluvi.configure(highlightcolor="black")
        self.Pluvi.configure(text='''Pluviometrie''')
        self.Pluvi.configure(width=80)

        self.PPluviometrie = tk.Label(self.MesureP)
        self.PPluviometrie.place(relx=0.141, rely=0.568, height=21, width=54
                , bordermode='ignore')
        self.PPluviometrie.configure(activebackground="#f9f9f9")
        self.PPluviometrie.configure(activeforeground="black")
        self.PPluviometrie.configure(anchor='e')
        self.PPluviometrie.configure(background="#d9d9d9")
        self.PPluviometrie.configure(disabledforeground="#a3a3a3")
        self.PPluviometrie.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.PPluviometrie.configure(foreground="#000000")
        self.PPluviometrie.configure(highlightbackground="#d9d9d9")
        self.PPluviometrie.configure(highlightcolor="black")
        self.PPluviometrie.configure(relief="sunken")
        self.PPluviometrie.configure(text='''0''')

        self.NoStation = tk.Message(self.MesureP)
        self.NoStation.place(relx=0.028, rely=0.667, relheight=0.054
                , relwidth=0.113, bordermode='ignore')
        self.NoStation.configure(anchor='e')
        self.NoStation.configure(background="#d9d9d9")
        self.NoStation.configure(font="-family {Segoe UI} -size 9")
        self.NoStation.configure(foreground="#000000")
        self.NoStation.configure(highlightbackground="#d9d9d9")
        self.NoStation.configure(highlightcolor="black")
        self.NoStation.configure(text='''No Station''')
        self.NoStation.configure(width=80)

        self.PStation = tk.Label(self.MesureP)
        self.PStation.place(relx=0.141, rely=0.667, height=21, width=54
                , bordermode='ignore')
        self.PStation.configure(activebackground="#f9f9f9")
        self.PStation.configure(activeforeground="black")
        self.PStation.configure(anchor='e')
        self.PStation.configure(background="#d9d9d9")
        self.PStation.configure(disabledforeground="#a3a3a3")
        self.PStation.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.PStation.configure(foreground="#000000")
        self.PStation.configure(highlightbackground="#d9d9d9")
        self.PStation.configure(highlightcolor="black")
        self.PStation.configure(relief="sunken")
        self.PStation.configure(text='''0''')

        self.PluviReset = tk.Button(self.MesureP)
        self.PluviReset.place(relx=0.056, rely=0.79, height=24, width=116
                , bordermode='ignore')
        self.PluviReset.configure(activebackground="#ececec")
        self.PluviReset.configure(activeforeground="#000000")
        self.PluviReset.configure(background="#d9d9d9")
        self.PluviReset.configure(disabledforeground="#a3a3a3")
        self.PluviReset.configure(font="-family {Segoe UI} -size 9")
        self.PluviReset.configure(foreground="#000000")
        self.PluviReset.configure(highlightbackground="#d9d9d9")
        self.PluviReset.configure(highlightcolor="black")
        self.PluviReset.configure(pady="0")
        self.PluviReset.configure(text='''Reset Pluviometre''')

        self.BVVent = ttk.Progressbar(self.MesureP)
        self.BVVent.place(relx=0.254, rely=0.173, relwidth=0.141, relheight=0.0
                , height=22, bordermode='ignore')

        self.BTemp = ttk.Progressbar(self.MesureP)
        self.BTemp.place(relx=0.254, rely=0.272, relwidth=0.141, relheight=0.0
                , height=22, bordermode='ignore')

        self.BLumi = ttk.Progressbar(self.MesureP)
        self.BLumi.place(relx=0.254, rely=0.37, relwidth=0.141, relheight=0.0
                , height=22, bordermode='ignore')

        self.BHumi = ttk.Progressbar(self.MesureP)
        self.BHumi.place(relx=0.254, rely=0.469, relwidth=0.141, relheight=0.0
                , height=22, bordermode='ignore')

        self.BPluvi = ttk.Progressbar(self.MesureP)
        self.BPluvi.place(relx=0.254, rely=0.568, relwidth=0.141, relheight=0.0
                , height=22, bordermode='ignore')

        self.EChartGirouette_1 = tk.Canvas(self.MesureP)
        self.EChartGirouette_1.place(relx=0.408, rely=0.074, relheight=0.501
                , relwidth=0.554, bordermode='ignore')
        self.EChartGirouette_1.configure(background="#ffffff")
        self.EChartGirouette_1.configure(borderwidth="2")
        self.EChartGirouette_1.configure(highlightbackground="#d9d9d9")
        self.EChartGirouette_1.configure(highlightcolor="black")
        self.EChartGirouette_1.configure(insertbackground="black")
        self.EChartGirouette_1.configure(selectbackground="blue")
        self.EChartGirouette_1.configure(selectforeground="white")

        self.Text = tk.Text(self.MesureP)
        self.Text.place(relx=0.423, rely=0.593, relheight=0.38, relwidth=0.541
                , bordermode='ignore')
        self.Text.configure(background="#cacaca")
        self.Text.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.Text.configure(foreground="black")
        self.Text.configure(highlightbackground="#d9d9d9")
        self.Text.configure(highlightcolor="black")
        self.Text.configure(insertbackground="black")
        self.Text.configure(selectbackground="blue")
        self.Text.configure(selectforeground="white")
        self.Text.configure(wrap="word")

if __name__ == '__main__':
    vp_start_gui()





