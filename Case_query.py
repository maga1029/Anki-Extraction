from Auxiliary_functions_extract import (f_string_from_query_indexes, f_checks_scrolled_text_frame, f_querry_all_values,
                                         f_generate_scrolled_text, f_output_regex_formatting_test, f_select_folder)
from Auxiliary_functions_case_notes import (f_main_case_notes_checks, f_main_list_matches, f_txt_name,
                                            f_rename_file_txt, f_write_txt_file)
from Auxiliary_functions_case_query import f_querry_complete_df, f_correct_first_index_query, f_index_case_query
from Data import list_elements_frame_scrolled, list_elements_frame_regex_formating
from sqlite3 import DatabaseError
from tkinter import *
from tkinter import scrolledtext
from tkinter.messagebox import showinfo


def f_main_querry_case(f24_list_test: list, f24_path: str, f24_ent_regex, f24_ent_formatting, f24_lbl_folder,
                       f24_ent_name):
    f24_regex = f24_ent_regex.get()
    f24_formatting = f24_ent_formatting.get()
    f24_folder = f24_lbl_folder.cget("text")
    f24_name = f24_ent_name.get()
    f24_flag = f_main_case_notes_checks(f24_regex, f24_formatting, f24_folder, f24_name)
    if not f24_flag:
        return None

    f24_corrected_first_index = f_correct_first_index_query(f24_list_test[1])
    f24_df = f_querry_complete_df(f24_path)
    f24_result_query = f_index_case_query(f24_corrected_first_index, f24_list_test[2], f24_df)
    main_case_notes_str_list = f_main_list_matches(f24_result_query, f24_regex, f24_formatting)
    f18_name = f_txt_name(f24_name)
    f18_filename = f_rename_file_txt(f24_folder, f18_name)
    f_write_txt_file(f18_filename, main_case_notes_str_list)

    showinfo(title="Extraction done", message="Text file generated")
    return None


def f_generate_frame_selected_indexes(f10_list_query: list, f10_index1: str, f10_index2: str, f10_btn_file,
                                      f10_btn_main, f10_win, f10_path):
    result_string_query = f_string_from_query_indexes(f10_list_query, f10_index1, f10_index2)
    print(result_string_query)
    if not result_string_query[0]:
        showinfo(title="Empty index", message="This idex is empty. Please select another one.")
        return None

    if not list_elements_frame_regex_formating == []:
        for _ in range(len(list_elements_frame_regex_formating)):
            list_elements_frame_regex_formating[_].destroy()

    f10_btn_file.config(state="disabled")
    f10_btn_main.config(state="disabled")

    frame_regex_formatting = LabelFrame(f10_win, text="Regex and formatting")
    frame_regex_formatting.grid(row=2, column=0, columnspan=4)

    f10_scrolled_text = scrolledtext.ScrolledText(frame_regex_formatting, wrap="word", height=0)
    f10_scrolled_text.insert(INSERT, result_string_query[0])
    f10_scrolled_text.grid(row=0, column=0, columnspan=4)
    f10_scrolled_text.config(state="disabled")

    f10_lbl_test_output = Label(frame_regex_formatting, text="", wraplength=100)
    f10_btn_regex_formatting = Button(frame_regex_formatting, text="Test output",
                                  command=lambda: f_output_regex_formatting_test(f10_scrolled_text, entry_regex,
                                                                                 entry_format, f10_lbl_test_output))
    lbl_regex = Label(frame_regex_formatting, text="Regex")
    lbl_format = Label(frame_regex_formatting, text="Formatting")
    entry_regex = Entry(frame_regex_formatting, width=50)
    entry_format = Entry(frame_regex_formatting, width=50)
    lbl_regex.grid(row=1, column=0)
    lbl_format.grid(row=2, column=0)
    entry_regex.grid(row=1, column=1)
    entry_format.grid(row=2, column=1)
    f10_btn_regex_formatting.grid(row=1, column=2, rowspan=2)
    f10_lbl_test_output.grid(row=1, column=3, rowspan=2)

    f10_lbl_select_folder = Label(frame_regex_formatting, text="", wraplength=350)
    f10_btn_select_folder = Button(frame_regex_formatting, text="Select destination folder",
                                  command=lambda: f_select_folder(f10_lbl_select_folder))
    f10_btn_select_folder.grid(row=3, column=0)
    f10_lbl_select_folder.grid(row=3, column=1)

    f10_lbl_file_name = Label(frame_regex_formatting, text="Name of the file")
    f10_ent_file_name = Entry(frame_regex_formatting)
    f10_lbl_file_name.grid(row=4, column=0)
    f10_ent_file_name.grid(row=4,column=1)

    f10_btn_start = Button(frame_regex_formatting, text="Generate txt file",
                           command=lambda: f_main_querry_case(result_string_query, f10_path, entry_regex, entry_format,
                                                              f10_lbl_select_folder, f10_ent_file_name))
    f10_btn_start.grid(row=5, column=0, columnspan=4)

    list_elements_frame_regex_formating.extend([f10_scrolled_text, lbl_regex, entry_regex, entry_format, lbl_format,
                                                f10_btn_regex_formatting, f10_lbl_test_output, f10_lbl_select_folder,
                                                f10_btn_start, f10_btn_select_folder])

    return None


def f_scrolled_text_frame(f4_str: str, f4_frame, f4_list_query: list, f4_btn_file, f4_btn_main, f4_win, f4_path):
    flags = f_checks_scrolled_text_frame(f4_str, f4_list_query)
    if 0 in flags:
        showinfo(title="Pipeline error",
                 message="An error ocurred. Please contact the distributor or modify the source code")
        return None

    if not list_elements_frame_scrolled == []:
        for _ in range(len(list_elements_frame_scrolled)):
            list_elements_frame_scrolled[_].destroy()

    scrolled_text = scrolledtext.ScrolledText(f4_frame, wrap="word")
    scrolled_text.insert(INSERT, f4_str)
    scrolled_text.config(state = "disabled")
    scrolled_text.grid(row=2, column=0, columnspan=4)

    lbl1_scrolled = Label(f4_frame, text="First Index")
    lbl2_scrolled = Label(f4_frame, text="Second Index")
    ent1_scrolled = Entry(f4_frame)
    ent2_scrolled = Entry(f4_frame)
    btn_select_indexes = Button(f4_frame, text="Select element",
                                command=lambda: f_generate_frame_selected_indexes(f4_list_query, ent1_scrolled.get(),
                                                                                  ent2_scrolled.get(), f4_btn_file,
                                                                                  f4_btn_main, f4_win, f4_path))
    lbl1_scrolled.grid(row=3, column=0)
    ent1_scrolled.grid(row=3, column=1)
    lbl2_scrolled.grid(row=3, column=2)
    ent2_scrolled.grid(row=3, column=3)
    btn_select_indexes.grid(row=4, column=0, columnspan=4)

    list_elements_frame_scrolled.extend([scrolled_text, lbl1_scrolled, lbl2_scrolled, ent1_scrolled, ent2_scrolled,
                                         btn_select_indexes])
    return None


def f_case_query(f14_path: str, f14_frame, f14_button_mode, f14_button_file, f14_button_main, f14_win):
    try:
        result_query = f_querry_all_values(f14_path)
        print(result_query)
        if not result_query:
            f14_button_mode.config(state="normal")
            return None
    except DatabaseError:
        showinfo(title="Missing field", message="Please select an Anki Database Reader File")
        f14_button_mode.config(state="normal")
        return None

    scrolled_string = f_generate_scrolled_text(result_query)
    if not scrolled_string:
        f14_button_mode.config(state="normal")
        return None

    f_scrolled_text_frame(scrolled_string, f14_frame, result_query, f14_button_file, f14_button_main, f14_win, f14_path)
    return None
