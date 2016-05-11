"""
pyblogit.tk_custom_dialog
~~~~~~~~~~~~~~~~~~~~~~~~~

This module provides a way to create custom tk
dialogs.
"""

import tkinter
from tkinter import ttk

class Dialog(tkinter.Toplevel):
    """The custom dialog."""

    def __init__(self, parent, title = None):
        tkinter.Toplevel.__init__(self, parent)
        self.transient(parent)

        if title:
            self.title(title)

        self.parent = parent
        self.result = None

        body = ttk.Frame(self)
        self.initial_focus = self.body(body)

        for child in body.winfo_children():
            child.grid_configure(padx=5, pady=5)

        body.pack(padx=5, pady=5)

        self.buttonbox()
        self.grab_set()

        if not self.initial_focus:
            self.initial_focus = self

            self.protocol('WM_DELETE_WINDOW', self.cancel)
            self.geometry('+%d+%d' % (parent.winfo_rootx() + 50,
                                      parent.winfo_rooty() + 50))
            self.initial_focus.focus_set()
            self.wait_window(self)

    def body(self, master):
        """Create dialog body. return widget should have.
        initial focus. This method should be overridden."""

        pass

    def buttonbox(self):
        """ Add standart button box. Override if you don't want the
        standard buttons."""

        box = ttk.Frame(self)

        button_ok = ttk.Button(box, text='OK', width=10, command=self.ok,
                           default='active')
        button_ok.pack(side='left')
        button_cancel = ttk.Button(box, text='Cancel', width=10,
                                   command=self.cancel)
        button_cancel.pack(side='left')

        self.bind('<Return>', self.ok)
        self.bind('<Escape>', self.cancel)

        box.pack()


    def ok(self, event=None):
        if not self.validate():
            self.initial_focus.focus_set()
            return

        self.withdraw()
        self.update_idletasks()
        self.apply()
        self.cancel()

    def cancel(self, event=None):
        """Puts focus back to parent window."""

        self.parent.focus_set()
        self.destroy()

    def validate(self):
        return 1 # override

    def apply(self):
        pass # override


class AddBlogDialog(Dialog):
    """The dialog for adding blogs."""

    def body(self, master):
        self.title_label = ttk.Label(master, text='Add Blog')
        self.title_label.grid(row=0, column=0, columnspan=2)

        self.id_label = ttk.Label(master, text='Blog ID')
        self.id_label.grid(row=1, column=0)
        self.name_label = ttk.Label(master, text='Blog Name')
        self.name_label.grid(row=2, column=0)

        self.id_entry = ttk.Entry(master, width=50)
        self.id_entry.grid(row=1, column=1)
        self.name_entry = ttk.Entry(master, width=50)
        self.name_entry.grid(row=2, column=1)

    def apply(self):
        blog_id = self.id_entry.get()
        blog_name = self.name_entry.get()
        self.result =  blog_id, blog_name
