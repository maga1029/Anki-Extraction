from sqlite3 import connect
from tkinter.messagebox import showinfo
import pandas as pd


def f_index_case_query(f27_first_index: int, f27_second_index: int, f27_df):
    if f27_first_index == 0:
        column_names = ['id', 'crt', 'mod', 'scm', 'ver', 'dty', 'usn', 'ls', 'conf', 'models', 'decks', 'dconf',
                        'tags']
        return f27_df[f27_first_index][0][column_names[f27_second_index]].iloc[0]

    if f27_first_index == 1:
        column_names = ['id', 'guid', 'mid', 'mod', 'usn', 'tags', 'flds', 'sfld', 'csum', 'flags', 'data']
        return f27_df[f27_first_index][0][column_names[f27_second_index]]  # Va a regresar una lista de n valores.

    if f27_first_index == 2:
        column_names = ['id', 'nid', 'did', 'ord', 'mod', 'usn', 'type', 'queue', 'due', 'ivl', 'factor', 'reps',
                        'lapses', 'left', 'odue', 'odid', 'flags', 'data']
        return f27_df[f27_first_index][0][column_names[f27_second_index]]  # Va a regresar una lista de n valores.

    if f27_first_index == 4:
        column_names = ['tbl', 'idx', 'stat']
        return f27_df[f27_first_index][0][column_names[f27_second_index]].iloc[0]


def f_querry_complete_df(f25_path: str):
    if f25_path == "":
        showinfo(title="Missing file", message="Please select an .anki2 file to proceed")
        return False

    with connect(f25_path) as conn:
        tables = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table';", conn)
        table_names = tables['name'].tolist()

    f25_list_text =[]

    for _ in range(len(table_names)):
        with connect(f25_path) as conn:
            tables_df = pd.read_sql_query(f"SELECT * FROM {table_names[_]};", conn)
        f25_list_text.extend([[tables_df]])

    return f25_list_text


def f_correct_first_index_query(f26_first_index: int):
    if f26_first_index == 1:
        return 0
    elif f26_first_index == 3:
        return 1
    elif f26_first_index == 5:
        return 2
    elif f26_first_index == 8:
        return 4
