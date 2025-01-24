from tkinter.messagebox import showinfo
import re
import os


def f_write_txt_file(f23_filename, f23_str_list):
    with open(f23_filename, "w", encoding="UTF-8") as file:
        for _ in range(len(f23_str_list)):
            file.writelines(f"{f23_str_list[_]}\n\n")
    return None


def f_rename_file_txt(f22_folder, f22_entry):
    f3_counter = 1
    if os.path.exists(f"{f22_folder}/{f22_entry}.txt"):
        f3_temp_dir = f"{f22_folder}/{f22_entry}.txt"
        while os.path.exists(f3_temp_dir):
            f3_temp_dir = f"{f22_folder}/{f22_entry}_{f3_counter}.txt"
            f3_counter += 1
    else:
        f3_temp_dir = f"{f22_folder}/{f22_entry}.txt"
    return f3_temp_dir


def f_txt_name(f21_name: str):
    if "." in f21_name:
        regex_pattern = "[.]"
        new_name = re.split(regex_pattern, f21_name)
        return new_name[0]
    else:
        return f21_name


def f_main_case_notes_checks(f20_regex, f20_formatting, f20_folder, f20_name):
    if not f20_regex:
        showinfo(title="Incomplete fields",
                 message="Please write a grouping field.")
        return False

    if not f20_formatting:
        showinfo(title="Incomplete fields",
                 message="Please write the formatting string.")
        return False

    if not f20_folder:
        showinfo(title="Incomplete fields",
                 message="Please select a destination folder.")
        return False

    if not f20_name:
        showinfo(title="Incomplete fields",
                 message="Please name the text file.")
        return False

    return True


def f_query_list_matches(f28_query, f28_regex, f28_formatting, f28_str_list: list):
    for _ in range(len(f28_query)):
        try:
            f28_matches = list(re.finditer(f28_regex, f28_query[_]))
            f28_match_values = [group for match in f28_matches for group in match.groups()]
            # f16_match_values = [_.group() for _ in f16_matches]
            try:
                f18_results = f28_formatting.format(*f28_match_values)
            except IndexError:
                f18_results = f"Extraction error. Original: {f28_query[_]}"
            f28_str_list.append(f18_results)
        except re.error:
            f18_results = f"Extraction error. Original: {f28_query[_]}"
            f28_str_list.append(f18_results)
            continue

    f28_counter = 0
    for _ in range(len(f28_str_list)):
        if "Extraction error" in f28_str_list[_]:
            f28_counter += 1

    print(f28_counter / len(f28_query) * 100)
    f28_str_list.append(f"Error rate: {f28_counter / len(f28_query) * 100} %")

    return f28_str_list


def f_query_one_element_matches(f29_query, f29_regex, f29_formatting, f29_str_list: list):
    f29_str_query = str(f29_query)
    try:
        f29_matches = list(re.finditer(f29_regex, f29_str_query))
        f29_match_values = [group for match in f29_matches for group in match.groups()]
        # f16_match_values = [_.group() for _ in f16_matches]
        try:
            f29_results = f29_formatting.format(*f29_match_values)
        except IndexError:
            f29_results = f"Extraction error. Original: {f29_str_query}"
        f29_str_list.append(f29_results)
    except re.error:
        f18_results = f"Extraction error. Original: {f29_str_query}"
        f29_str_list.append(f18_results)

    return f29_str_list


def f_main_list_matches(f19_query, f19_regex, f19_formatting):
    f19_str_list = []
    try:
        f19_str_list = f_query_list_matches(f19_query, f19_regex, f19_formatting, f19_str_list)
    except TypeError:
        f19_str_list = f_query_one_element_matches(f19_query, f19_regex, f19_formatting, f19_str_list)

    return f19_str_list
