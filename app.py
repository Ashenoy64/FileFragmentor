import tkinter as tk
from tkinter import ttk
from fragmentor import FileFragmentor

Object = FileFragmentor()


def fragment_task(fragment_size=20, file_path=None):

    if file_path==None or file_path=='':
        result_label.config(text="File Path Cannot be none or empty")
        return

    result=Object.fragment(File_path=file_path, size=fragment_size)
    result_label.config(text=result)

def merge_task(directory_path=None):
    if directory_path ==None or directory_path=='':
        result_label.config(text="Directory Path Cannot be none or empty")
        return
    
    result=Object.merge(dirPath=directory_path)
    result_label.config(text=result)

def on_fragment_submit():
    result_label.config(text='')
    try:

        if fragment_size_entry.get() == '':
            size=20
        else:
            size = int(fragment_size_entry.get())
    except:
        result_label.config(text=f"Invalid Input")
        return
    
    file_path = file_path_entry.get()
    fragment_task(size, file_path)

def on_merge_submit():
    result_label.config(text='')
    directory_path = directory_path_entry.get()
    merge_task(directory_path)

root = tk.Tk()
root.title("File Fragmentor")

frame = ttk.Frame(root, padding="10")
frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

fragment_label = ttk.Label(frame, text="Fragment Size:")
fragment_label.grid(column=0, row=0, padx=5, pady=5)

fragment_size_entry = ttk.Entry(frame)
fragment_size_entry.grid(column=1, row=0, padx=5, pady=5)

file_path_label = ttk.Label(frame, text="File Path:")
file_path_label.grid(column=0, row=1, padx=5, pady=5)

file_path_entry = ttk.Entry(frame)
file_path_entry.grid(column=1, row=1, padx=5, pady=5)

fragment_button = ttk.Button(frame, text="Fragment")
fragment_button.grid(column=0, row=2, padx=5, pady=5)
fragment_button.config(command=lambda: on_fragment_submit())

merge_label = ttk.Label(frame, text="Directory Path:")
merge_label.grid(column=0, row=3, padx=5, pady=5)

directory_path_entry = ttk.Entry(frame)
directory_path_entry.grid(column=1, row=3, padx=5, pady=5)

merge_button = ttk.Button(frame, text="Merge")
merge_button.grid(column=0, row=4, padx=5, pady=5)
merge_button.config(command=lambda: on_merge_submit())



result_label = ttk.Label(frame, text="")
result_label.grid(column=0, row=6, columnspan=2, padx=5, pady=5)

root.mainloop()
