from Auxiliary_functions_unzip import f_select_file_unzip, f_select_folder, f_main_zip
from Auxiliary_functions_extract import f_select_file, f_sunken_btn
from Case_notes import f_case_notes
from Case_query import f_case_query
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.scrolledtext import ScrolledText


def f_generate_frame_unzip(f29_notebook):
    frame_zip = LabelFrame(f29_notebook, text="Zip Extraction")
    frame_zip.grid(row=0, column=0)

    lbl_file_select1 = Label(frame_zip)
    lbl_file_select2 = Label(frame_zip)
    btn_file_images = Button(frame_zip, text="Select Anki Database file",
                             command=lambda: f_select_file_unzip(lbl_file_select1))
    btn_file_dest = Button(frame_zip, text="Select destination folder",
                           command=lambda: f_select_folder(lbl_file_select2))
    lbl_name_file = Label(frame_zip, text="Name of unzipped files folder")
    ent_name_file = Entry(frame_zip)
    btn_start = Button(frame_zip, text="Start conversion",
                       command=lambda: f_main_zip(lbl_file_select1["text"], lbl_file_select2["text"],
                                                  ent_name_file.get()))

    btn_file_images.grid(row=0, column=0)
    lbl_file_select1.grid(row=0, column=1)
    btn_file_dest.grid(row=1, column=0)
    lbl_file_select2.grid(row=1, column=1)
    lbl_name_file.grid(row=2, column=0)
    ent_name_file.grid(row=2, column=1)
    btn_start.grid(row=3, column=1)

    f29_notebook.add(frame_zip, text="Unzipping")


def f_pipeline_query(f5_path: str, f5_frame, f5_button_mode, f5_button_file, f5_button_main, f5_win):
    if not isinstance(f5_path, str):
        showinfo(title="Pipeline error",
                 message="An error ocurred. Please contact the distributor or modify the source code")
        return None

    if f5_button_mode["relief"] == "raised":
        f5_button_mode.config(state="disabled")
        f_case_query(f5_path, f5_frame, f5_button_mode, f5_button_file, f5_button_main, f5_win)
        return None

    elif f5_button_mode["relief"] == "sunken":
        f5_button_mode.config(state="disabled")
        f_case_notes(f5_path, f5_button_mode, f5_win)
        return None


def f_generate_frame_extraction(f30_notebook):
    frame_extract_nb = LabelFrame(f30_notebook)
    frame_extract_nb.grid(row=0, column=0)

    frame_extract = LabelFrame(frame_extract_nb, text="File selection")
    frame_extract.grid(row=0, column=0, columnspan=4)

    lbl_select_file = Label(frame_extract, text="", wraplength=550)
    btn_select_file = Button(frame_extract, text="Select Anki Database Reader File",
                             command=lambda: f_select_file(lbl_select_file))
    btn_reader_mode = Button(frame_extract, text="Note mode")
    btn_reader_mode.config(command=lambda b=btn_reader_mode: f_sunken_btn(b))
    btn_main2 = Button(frame_extract, text="Extract database elements")
    lbl_select_file.grid(row=0, column=1)
    btn_select_file.grid(row=0, column=0)
    btn_reader_mode.grid(row=1, column=1)
    btn_main2.grid(row=1, column=0)

    frame_scrolled_text = LabelFrame(frame_extract_nb, text="Scrolled text view")
    frame_scrolled_text.grid(row=1, column=0, columnspan=4)

    btn_main2.config(command=lambda: f_pipeline_query(lbl_select_file["text"], frame_scrolled_text, btn_reader_mode,
                                                      btn_select_file, btn_main2, frame_extract_nb))

    f30_notebook.add(frame_extract_nb, text="Extraction")


def f_instructions_tab(f31_notebook):
    frame_instructions = LabelFrame(f31_notebook)
    frame_instructions.grid(row=0, column=0)

    with open("Instructions Anki GUI.txt", "r", encoding="UTF-8") as file:
        txt_inst = file.read()

    f8_scrolled_text = ScrolledText(frame_instructions, wrap="word", height=0)
    f8_scrolled_text.insert(INSERT, txt_inst)
    f8_scrolled_text.grid(row=0, column=0, columnspan=4)
    f8_scrolled_text.config(state="disabled")

    f31_notebook.add(frame_instructions, text="Instructions")
