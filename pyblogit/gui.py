"""
pyblogit.gui
~~~~~~~~~~~~

This module builds displays and manages the applications GUI.
"""
import tkinter
from tkinter import ttk


class PyblogitGui(ttk.Frame):
    """The GUI for pyblogit."""
    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.root = parent
        self.init_gui()

    def init_gui(self):
        self.root.title('pyblogit')
        self.root.option_add('*tearOff', 'FALSE')

        self.grid(column=0, row=0, sticky='nesw')

        self.menubar = tkinter.Menu(root)

        self.menu_file = tkinter.Menu(self.menubar)
        self.menubar.add_cascade(menu=self.menu_file, label='File')

        self.menu_edit = tkinter.Menu(self.menubar)
        self.menubar.add_cascade(menu=self.menu_edit, label='Edit')

        self.root.config(menu=self.menubar)

        self.content_frame = ttk.Frame(self)
        self.content_frame.grid(column=0, row=0, sticky='n')

        self.sidebar_frame = ttk.Frame(self)
        self.sidebar_frame.grid(column=2, row=0, sticky='n')

        # Content frame
        self.title_entry = ttk.Entry(self.content_frame, width=50)
        self.title_entry.grid(column=1, row=0, sticky='w')

        self.tags_entry = ttk.Entry(self.content_frame, width=50)
        self.tags_entry.grid(column=1, row=1, sticky='w')

        self.url_entry = ttk.Entry(self.content_frame, width=50)
        self.url_entry.grid(column=1, row=2, sticky='w')

        self.content_entry = tkinter.Text(self.content_frame)
        self.content_entry.grid(column=0, row=4, columnspan=2, sticky='n')

        self.sidebar_separator = ttk.Separator(self, orient='vertical')
        self.sidebar_separator.grid(column=1, row=0, sticky='ns')
        self.content_separator = ttk.Separator(self.content_frame,
                orient='horizontal')
        self.content_separator.grid(column=0, row=3, columnspan=2, sticky='ew')

        self.title_label = ttk.Label(self.content_frame, text='Title')
        self.title_label.grid(column=0, row=0, sticky='w')
        self.tags_label = ttk.Label(self.content_frame, text='Tags')
        self.tags_label.grid(column=0, row=1, sticky='w')
        self.url_label = ttk.Label(self.content_frame, text='URL')
        self.url_label.grid(column=0, row=2, sticky='w')

        # Sidebar frame
        posts = []
        local_posts = []
        self.posts_listbox = tkinter.Listbox(self.sidebar_frame,
                listvariable=posts)
        self.posts_listbox.grid(column=0, row=1, sticky='n')

        self.local_posts_listbox = tkinter.Listbox(self.sidebar_frame,
                listvariable=local_posts)
        self.local_posts_listbox.grid(column=0, row=3, sticky='n')

        ttk.Label(self.sidebar_frame, text='Posts').grid(column=0, row=0,
                sticky='n')
        ttk.Label(self.sidebar_frame, text='Local Posts').grid(column=0, row=2,
                sticky='n')

        for child in self.winfo_children():
            for c in child.winfo_children():
                c.grid_configure(padx=5, pady=5)

if __name__ == '__main__':
    root = tkinter.Tk()
    PyblogitGui(root)
    root.mainloop()
