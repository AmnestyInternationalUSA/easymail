from tkinter import *
from tkinter import ttk

class inputFrame(ttk.Frame):
    def __init__(self, parent, row, column, sticky):
        ttk.Frame.__init__(self, parent)
        self.donate_footer_url = StringVar(self, value='campaignpage_url~130707~https://donate.amnestyusa.org/page/37908/donate/1')
        self.grid(row=row, column=column, sticky=sticky)
        self.columnconfigure(column, weight=1)
        self.hero_image_entry = ttk.Entry(self, width=7)
        ttk.Label(self, text='Hero Image').grid(column=1, row=1)
        self.hero_image_entry.grid(column=1, row=2, sticky=(W, E))
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.preview_text_entry = ttk.Entry(self, width=7)
        ttk.Label(self, text='Preview Text').grid(column=1, row=3)
        self.preview_text_entry.grid(column=1, row=4, sticky=(W, E))
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.url_entry = ttk.Entry(self, width=7)
        ttk.Label(self, text='Link URL').grid(column=1, row=5)
        self.url_entry.grid(column=1, row=6, sticky=(W, E))
        self.rowconfigure(5, weight=1)
        self.rowconfigure(6, weight=1)
        self.donate_footer_url_entry = ttk.Entry(self, width=7, textvariable=self.donate_footer_url)
        ttk.Label(self, text='Footer Donate URL').grid(column=1, row=7)
        self.donate_footer_url_entry.grid(column=1, row=8, sticky=(W, E))
        self.rowconfigure(7, weight=1)
        self.rowconfigure(8, weight=1)
        self.credit_entry = ttk.Entry(self, width=7)
        ttk.Label(self, text='Credit Text').grid(column=1, row=9)
        self.credit_entry.grid(column=1, row=10, sticky=(W, E))
        self.rowconfigure(9, weight=1)
        self.rowconfigure(10, weight=1)
        self.signature_entry_options = ['Margaret Huang', 'Andrea Kost']
        self.signature_entry_var = StringVar(self)
        self.signature_entry_var.set(self.signature_entry_options[0])
        self.signature_entry = ttk.OptionMenu(self, self.signature_entry_var,
                                              self.signature_entry_options[0], *self.signature_entry_options)
        ttk.Label(self, text='Signature').grid(column=1, row=11)
        self.signature_entry.grid(column=1, row=12, sticky=(W, E))
        self.rowconfigure(11, weight=1)
        self.rowconfigure(12, weight=1)
        self.action_question_var = IntVar()
        self.action_question = ttk.Checkbutton(self, text='Is this an action?', variable=self.action_question_var)
        self.action_question.grid(column=1, row=13, sticky=(W, E))
        self.rowconfigure(13, weight=1)
        self.button_question_var = IntVar()
        self.button_question = ttk.Checkbutton(self, text='Are there buttons in the body of the email and hero?',
                                               variable=self.button_question_var)
        self.button_question.grid(column=1, row=14, sticky=(W, E))
        self.rowconfigure(14, weight=1)
