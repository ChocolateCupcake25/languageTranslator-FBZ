# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 18:39:00 2022

@author: Fierce Bird // Ziyah Virani
"""
from tkinter import*
from tkinter import ttk
from googletrans import Translator
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

Entertext_area=Text(root,bg="LightBlue1",fg="#030140",font=("times",15,"bold"),height=10,wrap=WORD,width=50,padx=10,pady=10,bd=2)
Entertext_area.place(relx=0.2,rely=0.45,anchor=CENTER)

Outputtext_area=Text(root,bg="LightBlue1",fg="#030140",font=("times",15,"bold"),height=10,wrap=WORD,width=50,padx=15,pady=10,bd=2)
Outputtext_area.place(relx=0.75,rely=0.45,anchor=CENTER)

LANGUAGES = {'af': 'afrikaans',
'sq': 'albanian',
'am': 'amharic',
'ar': 'arabic',
'hy': 'armenian',
'az': 'azerbaijani',
'eu': 'basque',
'be': 'belarusian',
'bn': 'bengali',
'bs': 'bosnian',
'bg': 'bulgarian',
'ca': 'catalan',
'ceb': 'cebuano',
'ny': 'chichewa',
'zh-cn': 'chinese (simplified)',
'zh-tw': 'chinese (traditional)',
'co': 'corsican',
'hr': 'croatian',
'cs': 'czech',
'da': 'danish',
'nl': 'dutch',
'en': 'english',
'eo': 'esperanto',
'et': 'estonian',
'tl': 'filipino',
'fi': 'finnish',
'fr': 'french',
'fy': 'frisian',
'gl': 'galician',
'ka': 'georgian',
'de': 'german',
'el': 'greek',
'gu': 'gujarati',
'ht': 'haitian creole',
'ha': 'hausa',
'haw': 'hawaiian',
'iw': 'hebrew',
'he': 'hebrew',
'hi': 'hindi',
'hmn': 'hmong',
'hu': 'hungarian',
'is': 'icelandic',
'ig': 'igbo',
'id': 'indonesian',
'ga': 'irish',
'it': 'italian',
'ja': 'japanese',
'jw': 'javanese',
'kn': 'kannada',
'kk': 'kazakh',
'km': 'khmer',
'ko': 'korean',
'ku': 'kurdish (kurmanji)',
'ky': 'kyrgyz',
'lo': 'lao',
'la': 'latin',
'lv': 'latvian',
'lt': 'lithuanian',
'lb': 'luxembourgish',
'mk': 'macedonian',
'mg': 'malagasy',
'ms': 'malay',
'ml': 'malayalam',
'mt': 'maltese',
'mi': 'maori',
'mr': 'marathi',
'mn': 'mongolian',
'my': 'myanmar (burmese)',
'ne': 'nepali',
'no': 'norwegian',
'or': 'odia',
'ps': 'pashto',
'fa': 'persian',
'pl': 'polish',
'pt': 'portuguese',
'pa': 'punjabi',
'ro': 'romanian',
'ru': 'russian',
'sm': 'samoan',
'gd': 'scots gaelic',
'sr': 'serbian',
'st': 'sesotho',
'sn': 'shona',
'sd': 'sindhi',
'si': 'sinhala',
'sk': 'slovak',
'sl': 'slovenian',
'so': 'somali',
'es': 'spanish',
'su': 'sundanese',
'sw': 'swahili',
'sv': 'swedish',
'tg': 'tajik',
'ta': 'tamil',
'te': 'telugu',
'th': 'thai',
'tr': 'turkish',
'uk': 'ukrainian',
'ur': 'urdu',
'ug': 'uyghur',
'uz': 'uzbek',
'vi': 'vietnamese',
'cy': 'welsh',
'xh': 'xhosa',
'yi': 'yiddish',
'yo': 'yoruba',
'zu': 'zulu',}
    
language = list(LANGUAGES.values())

Text_dropdown = ttk.Combobox(state="readonly",background="LightBlue1",value=language)

Output_dropdown = ttk.Combobox(state="readonly",background="LightBlue1",value=language)

Text_dropdown.set("english")

Text_dropdown.place(relx=0.25,rely=0.2,anchor=CENTER)
Output_dropdown.place(relx=0.75,rely=0.2,anchor=CENTER)


def Translate():
    
    src_lang = Text_dropdown.get()
    dest_lang  = Output_dropdown.get()
    translator = Translator()
    try:
        translated = translator.translate(text=
        Entertext_area.get(1.0,END),src=src_lang.get(),dest = dest_lang())
    except UnkownValueError:
        messagebox.showinfo("Complication","Please try Again!")
        
    Outputtext_area.delete(1.0,END)
    Outputtext_area.insert(END,translated.text)
    

bt=Button(root,text=" TRANSLATE ",bg="DeepSkyBlue2",fg="#030140",pady=10,width=10,font=("times",15,"bold"),command= Translate)
bt.place(relx=0.48,rely=0.75,anchor=CENTER)

label_end =Label(root,text="Created by : Ziyah Virani//FierceBird",bg="CadetBlue1",fg="#030140",font=("times",15,"bold"))
label_end.place(relx=0.5,rely=0.8,anchor=CENTER)

root.mainloop()





