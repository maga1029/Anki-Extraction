from sqlite3 import connect
from tkinter import END
from tkinter.filedialog import askopenfile, askdirectory
from tkinter.messagebox import showinfo
import pandas as pd
import re


def f_select_file(f1_lbl):
    try:
        f1_lbl["text"] = askopenfile(mode="r", filetypes=[("Anki Database Reader File","*.anki2")]).name
    except AttributeError:
        f1_lbl["text"] = ""


def f_select_folder(f17_lbl):
    try:
        f17_lbl["text"] = askdirectory()
    except AttributeError:
        f17_lbl["text"] = ""


def f_sunken_btn(f6_btn):
    if f6_btn["relief"] == "raised":
        f6_btn.config(relief = "sunken")
    elif f6_btn["relief"] == "sunken":
        f6_btn.config(relief = "raised")
    return None


def f_generate_scrolled_text(f3_list_strings: list):
    if not isinstance(f3_list_strings, list):
        showinfo(title="Pipeline error",
                 message="An error ocurred. Please contact the distributor or modify the source code")
        return False

    string_scrolledtext = ""
    outer_counter = 0
    for _ in range(len(f3_list_strings)):
      try:
        if isinstance(f3_list_strings[_+1], list):
            string_scrolledtext += f"{outer_counter+1} {f3_list_strings[_]}\n"
            for __ in range(len(f3_list_strings[_+1])):
                string_scrolledtext += f"{outer_counter + 1}.{__+1} {f3_list_strings[_+1][__]}\n"
            outer_counter += 1
            continue
        elif isinstance(f3_list_strings[_], list):
            continue
        elif not isinstance(f3_list_strings[_+1], list):
            string_scrolledtext += f"{outer_counter + 1} {f3_list_strings[_]}\n"
            outer_counter += 1
      except IndexError:
            string_scrolledtext += f"{outer_counter+1} {f3_list_strings[_]}"

    return string_scrolledtext


def f_query_just_notes(f7_path: str):
    if not isinstance(f7_path, str):
        showinfo(title="Pipeline error",
                 message="An error ocurred. Please contact the distributor or modify the source code")
        return False

    with connect(f7_path) as conn:
        notes_df = pd.read_sql_query("SELECT * FROM notes;", conn)
    notes_df = notes_df.to_numpy()

    notes_list = []

    for _ in range(len(notes_df)):
        notes_list.append(notes_df[_][6])

    return notes_list


def f_querry_all_values(f2_path: str):
    if f2_path == "":
        showinfo(title="Missing file", message="Please select an .anki2 file to proceed")
        return False

    f2_list_text = []
    with connect(f2_path) as conn:
        tables = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table';", conn)
        table_names = tables['name'].tolist()

    for _ in range(len(table_names)):
        with connect(f2_path) as conn:
            notes_df = pd.read_sql_query(f"SELECT * FROM {table_names[_]};", conn)
        notes_df = notes_df.to_numpy()

        try:
            list_text_aux = []
            for __ in range(len(notes_df[0])):
                list_text_aux.append(notes_df[0][__])
            f2_list_text.append(table_names[_])
            f2_list_text.append(list_text_aux)
        except IndexError:
            f2_list_text.append(table_names[_])

    return f2_list_text


def f_checks_scrolled_text_frame(f11_str: str, f11_list_query: list):
    flags = [1, 1]
    if not isinstance(f11_str, str):
        flags[0] = 0

    if not isinstance(f11_list_query, list):
        flags[1] = 0

    return flags


def f_ckecks_string_query_indexes(f12_list_query: list, f12_index1: str, f12_index2: str):
    flags = [1,1]
    if not isinstance(f12_list_query, list):
        flags[0] = 0

    list_indexes_processed = []
    try:
        f12_index1_int = abs(int(f12_index1))
        f12_index2_int = abs(int(f12_index2))
        f12_index2_normalized = f12_index2_int - 1
        list_indexes_processed.extend([f12_index1_int, f12_index2_int, f12_index2_normalized])
    except (ValueError, TypeError, AttributeError, NameError):
        flags[1] = 0

    return flags, list_indexes_processed


def f_query_index_processing(f13_list_query: list, f13_index1_int: int, f13_index2_normalized: int):
    try:
        if f13_index1_int == 1:
            print(f13_list_query[f13_index1_int][f13_index2_normalized])
            return f13_list_query[f13_index1_int][f13_index2_normalized], f13_index1_int, f13_index2_normalized
        elif f13_index1_int == 2:
            print(f13_list_query[f13_index1_int + 1][f13_index2_normalized])
            return f13_list_query[f13_index1_int + 1][f13_index2_normalized], f13_index1_int + 1, f13_index2_normalized
        elif f13_index1_int == 3:
            print(f13_list_query[f13_index1_int + 2][f13_index2_normalized])
            return f13_list_query[f13_index1_int + 2][f13_index2_normalized], f13_index1_int + 2, f13_index2_normalized
        elif f13_index1_int == 5:
            print(f13_list_query[f13_index1_int + 3][f13_index2_normalized])
            return f13_list_query[f13_index1_int + 3][f13_index2_normalized], f13_index1_int + 3, f13_index2_normalized
        elif (f13_index1_int == 4) or (f13_index1_int == 6) or (f13_index1_int == 7):
            return None
    except IndexError:
        return None


def f_string_from_query_indexes(f9_list_query: list, f9_index1: str, f9_index2: str):
    f12_result_checks = f_ckecks_string_query_indexes(f9_list_query, f9_index1, f9_index2)
    if f12_result_checks[0][0] == 0:
        showinfo(title="Pipeline error",
                 message="An error ocurred. Please contact the distributor or modify the source code")
        return None
    if f12_result_checks[0][1] == 0:
        showinfo(title="Type error", message="Please select valid indexes")
        return None

    f9_index1_int, f9_index2_int, f9_index2_normalized = f12_result_checks[1]
    f9_result = f_query_index_processing(f9_list_query, f9_index1_int, f9_index2_normalized)

    if not f9_result and ((f9_index1_int == 4) or (f9_index1_int == 6) or (f9_index1_int == 7)):
        showinfo(title="Invalid set", message="This combination isn't accepted to create the txt files")
        return None
    if not f9_result:
        showinfo(title="Index error", message="Please select a valid numerical index")
        return None

    return f9_result


def f_output_regex_formatting_test(f16_lbl_text, f16_ent_regex_pattern, f16_ent_formatting, f16_result_lbl):
    f16_text = f16_lbl_text.get('1.0', END)
    f16_regex_pattern = f16_ent_regex_pattern.get()
    f16_formatting = f16_ent_formatting.get()
    print(f16_regex_pattern)
    print(f16_formatting)

    try:
        f16_matches = list(re.finditer(f16_regex_pattern, f16_text))
        f16_match_values = [group for match in f16_matches for group in match.groups()]
        # f16_match_values = [_.group() for _ in f16_matches]
        try:
            f16_results = f16_formatting.format(*f16_match_values)
        except IndexError:
            f16_result_lbl.config(text="")
            showinfo(title="Error", message="Formatting string references non-existent groups.")
            return None
        print(f16_results)
        f16_result_lbl.config(text=f16_results)
    except re.error as e:
        f16_result_lbl.config(text="")
        showinfo(title="Regex Error", message=f"Invalid regex: {e}")
    return None
