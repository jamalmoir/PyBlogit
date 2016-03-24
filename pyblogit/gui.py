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

root.mainloop()
