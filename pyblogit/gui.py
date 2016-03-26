"""
pyblogit.gui
~~~~~~~~~~~~

This module builds displays and manages the applications GUI.
"""
import tkinter
from tkinter import ttk

root = tkinter.Tk()
root.title('pyblogit')
root.option_add('*tearOff', 'FALSE')


main_frame = ttk.Frame(root, padding='3 3 12 12')
main_frame.grid(column=0, row=0, sticky='nesw')
main_frame.columnconfigure(0, weight=1)
main_frame.rowconfigure(0, weight=1)

menubar = tkinter.Menu(root)
menu_file = tkinter.Menu(menubar)
menu_edit = tkinter.Menu(menubar)
menubar.add_cascade(menu=menu_file, label='File')
menubar.add_cascade(menu=menu_edit, label='Edit')
root.config(menu=menubar)

content_frame = ttk.Frame(main_frame, padding='')
content_frame.grid(column=0, row=0, columnspan=2, sticky='nsw')
content_frame.columnconfigure(0, weight=1)
content_frame.rowconfigure(0, weight=1)

sidebar_frame = ttk.Frame(main_frame, padding='')
sidebar_frame.grid(column=2, row=0, sticky='nes')
sidebar_frame.columnconfigure(2, weight=1)
sidebar_frame.rowconfigure(0, weight=1)

# Content frame
title_entry = ttk.Entry(content_frame, width=50)
title_entry.grid(column=1, row=0, sticky='nw')

tags_entry = ttk.Entry(content_frame, width=50)
tags_entry.grid(column=1, row=1, sticky='w')

url_entry = ttk.Entry(content_frame, width=50)
url_entry.grid(column=1, row=2, sticky='w')

content_entry = tkinter.Text(content_frame )
content_entry.grid(column=0, row=4, columnspan=4, sticky='n')

ttk.Label(content_frame, text='Title').grid(column=0, row=0, sticky='w')
ttk.Label(content_frame, text='Tags').grid(column=0, row=1, sticky='w')
ttk.Label(content_frame, text='URL').grid(column=0, row=2, sticky='w')
ttk.Label(content_frame, text='Content').grid(column=0, row=3, sticky='w')

# Sidebar frame
posts = []
local_posts = []
posts_listbox = tkinter.Listbox(sidebar_frame, listvariable=posts)
posts_listbox.grid(column=0, row=1, sticky='n')

local_posts_listbox = tkinter.Listbox(sidebar_frame, listvariable=local_posts)
local_posts_listbox.grid(column=0, row=3, sticky='n')

ttk.Label(sidebar_frame, text='Posts').grid(column=0, row=0, sticky='n')
ttk.Label(sidebar_frame, text='Local Posts').grid(column=0, row=2, sticky='n')

#for child in main_frame.winfo_children():
#    for c in child.winfo_children():
#        c.grid_configure(padx=5, pady=5)

root.mainloop()
