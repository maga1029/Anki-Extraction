from Auxiliary_functions_case_notes import (f_main_list_matches, f_main_case_notes_checks, f_txt_name,
                                            f_rename_file_txt, f_write_txt_file)
from Auxiliary_functions_extract import f_query_just_notes, f_output_regex_formatting_test, f_select_folder
from Data import list_elements_frame_regex_formating
from sqlite3 import DatabaseError
from tkinter import *
from tkinter import scrolledtext
from tkinter.messagebox import showinfo


def f_main_case_notes(f18_path, f18_ent_regex, f18_ent_formatting, f18_lbl_folder, f18_ent_name):
    f18_query = f_query_just_notes(f18_path)
    f18_regex = f18_ent_regex.get()
    f18_formatting = f18_ent_formatting.get()
    f18_folder = f18_lbl_folder.cget("text")
    f18_name = f18_ent_name.get()
    f18_flag = f_main_case_notes_checks(f18_regex, f18_formatting, f18_folder, f18_name)
    if not f18_flag:
        return None

    main_case_notes_str_list = f_main_list_matches(f18_query, f18_regex, f18_formatting)
    f18_name = f_txt_name(f18_name)
    f18_filename = f_rename_file_txt(f18_folder, f18_name)
    f_write_txt_file(f18_filename, main_case_notes_str_list)

    showinfo(title="Extraction done", message="Text file generated")
    return None


def f_regex_formatted_frame(f8_str: list, f8_frame, f8_path):
    if not isinstance(f8_str, list):
        showinfo(title="Pipeline error",
                 message="An error ocurred. Please contact the distributor or modify the source code")
        return None

    if not list_elements_frame_regex_formating == []:
        for _ in range(len(list_elements_frame_regex_formating)):
            list_elements_frame_regex_formating[_].destroy()

    frame_regex_formatting = LabelFrame(f8_frame, text="Regex and formatting")
    frame_regex_formatting.grid(row=3, column=0, columnspan=4)

    f8_scrolled_text = scrolledtext.ScrolledText(frame_regex_formatting, wrap="word", height=0)
    f8_scrolled_text.insert(INSERT, f8_str[0])
    f8_scrolled_text.grid(row=0, column=0, columnspan=4)
    f8_scrolled_text.config(state="disabled")

    lbl_regex = Label(frame_regex_formatting, text="Regex")
    lbl_format = Label(frame_regex_formatting, text="Formatting")
    entry_regex = Entry(frame_regex_formatting, width=50)
    entry_format = Entry(frame_regex_formatting, width=50)
    f8_lbl_test_output = Label(frame_regex_formatting, text="", wraplength=100)
    f8_btn_regex_formatting = Button(frame_regex_formatting, text="Test output",
                                  command=lambda: f_output_regex_formatting_test(f8_scrolled_text, entry_regex,
                                                                                 entry_format, f8_lbl_test_output))
    lbl_regex.grid(row=1, column=0)
    lbl_format.grid(row=2, column=0)
    entry_regex.grid(row=1, column=1)
    entry_format.grid(row=2, column=1)
    f8_btn_regex_formatting.grid(row=1, column=2, rowspan=2)
    f8_lbl_test_output.grid(row=1, column=3, rowspan=2)

    f8_lbl_select_folder = Label(frame_regex_formatting, text="", wraplength=550)
    f8_btn_select_folder = Button(frame_regex_formatting, text="Select destination folder",
                                  command=lambda: f_select_folder(f8_lbl_select_folder))
    f8_lbl_file_name = Label(frame_regex_formatting, text="Name of the file")
    f8_ent_file_name = Entry(frame_regex_formatting)
    f8_btn_select_folder.grid(row=3, column=0)
    f8_lbl_select_folder.grid(row=3, column=1)
    f8_lbl_file_name.grid(row=4, column=0)
    f8_ent_file_name.grid(row=4,column=1)

    f8_btn_start = Button(frame_regex_formatting, text="Generate txt file",
                          command=lambda: f_main_case_notes(f8_path, entry_regex, entry_format, f8_lbl_select_folder,
                                                            f8_ent_file_name))
    f8_btn_start.grid(row=5, column=0, columnspan=4)

    list_elements_frame_regex_formating.extend([f8_scrolled_text, lbl_regex, lbl_format, entry_format, entry_regex,
                                                f8_btn_regex_formatting, f8_lbl_test_output, f8_lbl_select_folder,
                                                f8_btn_start, f8_btn_select_folder, f8_lbl_file_name,
                                                f8_ent_file_name])
    return None


def f_case_notes(f15_path: str, f15_button_mode, f15_frame):
    try:
        notes_label = f_query_just_notes(f15_path)
    except DatabaseError:
        showinfo(title="Missing field", message="Please select an Anki Database Reader File")
        f15_button_mode.config(state="normal")
        return None

    f_regex_formatted_frame(notes_label, f15_frame, f15_path)
    if not notes_label:
        f15_button_mode.config(state="normal")
        return None
