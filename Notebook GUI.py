from Auxiliary_functions_notebook import f_generate_frame_unzip, f_generate_frame_extraction
from tkinter import *
from tkinter import ttk

root= Tk()
root.title("Anki Extraction")
root.geometry("700x750")

notebook = ttk.Notebook(root)
notebook.pack(fill=BOTH, expand=True)

f_generate_frame_unzip(notebook)
f_generate_frame_extraction(notebook)

root.mainloop()
