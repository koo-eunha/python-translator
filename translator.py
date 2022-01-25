'''
Joanne Wong, Kaushik Thakkar, Adrian Lam, Eunha Koo
INF1340, Dr. Maher Elshakankiri
Final Project: Translator
Date created: 2021.12.06
Date last modified: 2021.12.10
'''

from googletrans import Translator, LANGUAGES
from tkinter import *
from tkinter import ttk

class translatorProject:
    def __init__(self):
        ws = Tk() # window for GUI
        ws.title("Translator")
    
        frame1 = Frame(ws) # create frame for all elements
        frame1.pack(padx=10, pady=30)

        # labels for dropdown menu
        label1 = Label(frame1,text="Choose the language to translate from: ")
        label2 = Label(frame1,text="Choose the language to translate to: ")

        # create variable and dropdown menu for input language
        self.language1 = StringVar()
        inputlanguage = ttk.OptionMenu(frame1, self.language1, "Choose Language",
                                     "English", "French", "Spanish", "Chinese (Simplified)",
                                     "Japanese", "Korean")

        # create variable and dropdown menu for output language
        self.language2 = StringVar()
        outputlanguage = ttk.OptionMenu(frame1, self.language2, "Choose Language",
                                      "English", "French", "Spanish", "Chinese (Simplified)",
                                      "Japanese", "Korean")

        # labels for textarea
        label3 = Label(frame1,text="Please enter text to be translated: ")
        label4 = Label(frame1,text="Translated text: ")

        # create textareas for input and output text
        self.input_box = Text(frame1, height=15, width=40, wrap=WORD)
        self.output_box = Text(frame1, height=15, width=40, wrap=WORD)

        # create button for translate
        bt = ttk.Button(frame1, text="Translate", command = self.translate)

        # place all elements in a grid
        label1.grid(row=0,column=0,sticky=W)
        label2.grid(row=0,column=1, padx=10, sticky=W)
        inputlanguage.grid(row=1,column=0, sticky=W)
        outputlanguage.grid(row=1,column=1, padx=10, sticky=W)
        label3.grid(row=2, column=0, pady=10, sticky=W)
        label4.grid(row=2, column=1, padx=10, pady=10,sticky=W)
        self.input_box.grid(row=3, column=0, sticky=W)
        self.output_box.grid(row=3, column=1, padx=10, sticky=W)
        bt.grid(row=4, column=1, padx=10, pady=30, sticky=E)

        ws.mainloop() # create an event loop

    def translate(self):
        """ This function translates the user's inputed word/phrase to their selected language
        """

        translator = Translator()

        # get the source and destination languages and translate the input text
        translation = translator.translate(text = self.input_box.get(1.0, END),
                                           src = self.language1.get(),
                                           dest = self.language2.get())
        self.output_box.delete(1.0, END) # clear output box
        self.output_box.insert(END, translation.text) # display traslated text to the output box


translatorProject() # create GUI
