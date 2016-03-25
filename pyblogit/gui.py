"""
pyblogit.gui
~~~~~~~~~~~~

This module builds displays and manages the applications GUI.
"""
import tkinter
from tkinter import ttk

root = tkinter.Tk()
root.title('pyblogit')

main_frame = ttk.Frame(root, padding='3 3 12 12')
main_frame.grid(column=0, row=0, sticky=('N, W, E, S'))
main_frame.columnconfigure(0, weight=1)
main_frame.rowconfigure(0, weight=1)

content_frame = ttk.Frame(main_frame, padding='3 3 12 12')
content_frame.grid(column=0, row=0, columnspan=2, sticky=('N, W, S'))
content_frame.columnconfigure(0, weight=1)
content_frame.rowconfigure(0, weight=1)

sidebar_frame = ttk.Frame(main_frame, padding='3 3 12 12')
sidebar_frame.grid(column=2, row=0, sticky=('N, E, S'))
sidebar_frame.columnconfigure(2, weight=1)
sidebar_frame.rowconfigure(0, weight=1)

title_entry = ttk.Entry(content_frame, width=50)
title_entry.grid(column=1, row=0, sticky='N E W')

tags_entry = ttk.Entry(content_frame, width=50)
tags_entry.grid(column=1, row=1, sticky='W')

url_entry = ttk.Entry(content_frame, width=50)
url_entry.grid(column=1, row=2, sticky='W')

content_entry = tkinter.Text(content_frame )
content_entry.grid(column=0, row=4, columnspan=4, sticky='E S W')

ttk.Label(content_frame, text='Title').grid(column=0, row=0, sticky='N W')
ttk.Label(content_frame, text='Tags').grid(column=0, row=1, sticky='W')
ttk.Label(content_frame, text='URL').grid(column=0, row=2, sticky='W')
ttk.Label(content_frame, text='Content').grid(column=0, row=3, sticky='W')

for child in main_frame.winfo_children():
    for c in child.winfo_children():
        c.grid_configure(padx=5, pady=5)

root.mainloop()
