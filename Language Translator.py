# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 18:39:00 2022

@author: Fierce Bird // Ziyah Virani
"""
from tkinter import*
from tkinter import ttk
from googletrans import Translator, LANGUAGES
from tkinter import messagebox

root = Tk()
root.geometry("800x700")
root.title("language translator")
root.configure(bg="CadetBlue1")



label_heading=Label(root,text="LANGUAGE TRANSLATOR",font=("Bookman Old Style",20,"bold","italic"),bg="CadetBlue1",fg="#030140")

label_EnterText=Label(root,text="Enter Text : ",font=("times",15,"bold"),bg="CadetBlue1",fg="#030140")

label_Output=Label(root,text="Output : ",font=("times",15,"bold"),bg="CadetBlue1",fg="#030140")

label_heading.place(relx=0.5,rely=0.1,anchor=CENTER)
label_EnterText.place(relx=0.08,rely=0.2,anchor=CENTER)
label_Output.place(relx=0.6,rely=0.2,anchor=CENTER)

Entertext_area=Text(root,bg="LightBlue1",fg="#030140",font=("times",15,"bold"),height=10,wrap=WORD,width=35,padx=10,pady=10,bd=2)
Entertext_area.place(relx=0.2,rely=0.45,anchor=CENTER)

Outputtext_area=Text(root,bg="LightBlue1",fg="#030140",font=("times",15,"bold"),height=10,wrap=WORD,width=35,padx=15,pady=10,bd=2)
Outputtext_area.place(relx=0.75,rely=0.45,anchor=CENTER)

    
language = list(LANGUAGES.values())

Text_dropdown = ttk.Combobox(state="readonly",background="LightBlue1",value=language)

Output_dropdown = ttk.Combobox(state="readonly",background="LightBlue1",value=language)

Text_dropdown.set("english")

Text_dropdown.place(relx=0.25,rely=0.2,anchor=CENTER)
Output_dropdown.place(relx=0.75,rely=0.2,anchor=CENTER)


def Translate():
    translator = Translator()
    try:
        translated = translator.translate(text=Entertext_area.get(1.0,END),src=Text_dropdown.get(),dest = Output_dropdown.get())
        Outputtext_area.delete(1.0,END)
        Outputtext_area.insert(END,translated.text)
    except :
        messagebox.showinfo("Complication","Please try Again!")
    
    

bt=Button(root,text=" TRANSLATE ",bg="DeepSkyBlue2",fg="#030140",pady=10,width=10,font=("times",15,"bold"),command= Translate)
bt.place(relx=0.48,rely=0.75,anchor=CENTER)

label_end =Label(root,text="Created by : Ziyah Virani//FierceBird",bg="CadetBlue1",fg="#030140",font=("times",15,"bold"))
label_end.place(relx=0.5,rely=0.8,anchor=CENTER)

root.mainloop()





