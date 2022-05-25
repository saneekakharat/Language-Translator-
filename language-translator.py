from tkinter import *
import tkinter as tk
from tkinter import ttk
from translate import Translator
# from googletrans import Translator, constants

Screen = Tk()
Screen.title("Language Translator")
Screen.geometry("700x500")
Screen.intro_label = Label(Screen, text = "Convert Text in any language to another Language", fg="red", relief=tk.RAISED, borderwidth=5)
Screen.intro_label.config(font=('Times New Roman', 18, 'bold'))
Screen.intro_label.place(relx= 0.5,rely=0.5, anchor='center')

#Variable that stores the input of the language 
InputLanguageChoice = StringVar()
#Variable that stores the output of the language
TranslateLanguageChoice = StringVar()
LanguageChoices = {'Hindi','English','French','German','Spanish'}
InputLanguageChoice.set('English')
TranslateLanguageChoice.set('Hindi')


def Translate():
    translator = Translator(from_lang = InputLanguageChoice.get(),to_lang =TranslateLanguageChoice.get())
    # Translation = translator.translate( )
    Translation = translator.translate(TextVar.get())
    OutputVar.set(Translation)


#choice for input language
InputLanguageChoiceMenu = OptionMenu(Screen,InputLanguageChoice,*LanguageChoices)
Label(Screen,text="Choose a Language").grid(row=0,column=1)
InputLanguageChoiceMenu.grid(row=1,column=1)
 
#choice in which the language is to be translated
NewLanguageChoiceMenu = OptionMenu(Screen,TranslateLanguageChoice,*LanguageChoices)
Label(Screen,text="Translated Language").grid(row=0,column=2)
NewLanguageChoiceMenu.grid(row=1,column=2)

Label(Screen,text="Enter Text").grid(row=2,column =0)
TextVar = StringVar()
TextBox = Entry(Screen,textvariable=TextVar).grid(row=2,column = 1)
 
Label(Screen,text="Output Text").grid(row=2,column = 4)
OutputVar = StringVar()
TextBox = Entry(Screen,textvariable=OutputVar).grid(row=2,column = 3)
 
#Button for calling function
B = Button(Screen,text="Translate",command=Translate, relief = GROOVE).grid(row=3,column=1,columnspan = 3)
 
mainloop()