from tkinter.filedialog import askopenfile, askdirectory
from tkinter.messagebox import showinfo
from zipfile import ZipFile
import os


def f_select_file_unzip(f1_lbl):
    try:
        f1_lbl["text"] = askopenfile(mode="r", filetypes=[("Anki Database","*.apkg")]).name
    except AttributeError:
        f1_lbl["text"] = ""


def f_select_folder(f2_lbl):
    try:
        f2_lbl["text"] = askdirectory()
    except AttributeError:
        f2_lbl["text"] = ""


def f_rename_directory(f3_folder, f3_entry):
    f3_counter = 1
    if os.path.exists(f"{f3_folder}/{f3_entry}"):
        f3_temp_dir = f"{f3_folder}/{f3_entry}"
        while os.path.exists(f3_temp_dir):
            f3_temp_dir = f"{f3_folder}/{f3_entry}_{f3_counter}"
            f3_counter += 1
    else:
        f3_temp_dir = f"{f3_folder}/{f3_entry}"
    return f3_temp_dir


def f_main_zip(f_main1_apkg: str, f_main1_folder: str, f_main1_entry: str):

    if (f_main1_apkg == "") or (f_main1_folder == "") or (f_main1_entry == ""):
        showinfo(title="Missing entries", message="Please fill all fields")
        return None

    f_main1_temp_dir = f_rename_directory(f_main1_folder, f_main1_entry)
    anki_file_path = f_main1_apkg

    print(f_main1_temp_dir)
    os.makedirs(f_main1_temp_dir, exist_ok=True)

    with ZipFile(anki_file_path, 'r') as zip_ref:
        zip_ref.extractall(f_main1_temp_dir)

    showinfo(title="Extraction done", message="Anki Database File extraction successfully finished")
    return None
