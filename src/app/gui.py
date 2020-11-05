from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
import app
import config  # TODO: Set up Config file

global global_file_path
global global_output_path
global global_json_map
global_json_map = None


def run():
    # Set New Name
    new_name = new_name_ent.get().strip()

    file_path = global_file_path

    output_folder = global_output_path

    # Set Counter
    counter = int(counter_ent.get())

    # Set Order
    order = None
    if order_combo.get() == 'Ascending':
        order = 'asc'
    elif order_combo.get() == 'Descending':
        order = 'desc'

    # Set Map
    global global_json_map
    map = global_json_map
    if map == '':
        map = None

    app.app(new_name, file_path, output_folder, counter, order, map)


def get_file_path():
    file_path = filedialog.askopenfilename(initialdir="../data/",
                                           title="Select a File",
                                           filetypes=(("PDF", "*.pdf"), ("all files", "*.*")))
    file_path_ent = Text(root, state='normal', width=50, height=1)
    file_path_ent.insert('end', file_path)
    file_path_ent.configure(state='disable')
    file_path_ent.grid(column=1, row=1)

    global global_file_path
    global_file_path = file_path
    return file_path


def get_json_map_path():
    json_map = filedialog.askopenfilename(initialdir="../data/",
                                          title="Select a File",
                                          filetypes=(("CSV", "*.csv"), ("all files", "*.*")))
    map_path_ent = Text(root, state='normal', width=50, height=1)
    map_path_ent.insert('end', json_map)
    map_path_ent.configure(state='disable')
    map_path_ent.grid(column=1, row=4)

    global global_json_map
    global_json_map = json_map
    return json_map


def get_output_path():
    output_path = filedialog.askdirectory(initialdir="../../",
                                          title="Select a File")
    output_path_ent = Text(root, state='normal', width=50, height=1)
    output_path_ent.insert('end', output_path)
    output_path_ent.configure(state='disable')
    output_path_ent.grid(column=1, row=5)

    global global_output_path
    global_output_path = output_path
    return output_path


def clear_map():
    json_map = ''
    map_path_ent = Text(root, state='normal', width=50, height=1)
    map_path_ent.insert('end', json_map)
    map_path_ent.configure(state='disable')
    map_path_ent.grid(column=1, row=4)

    global global_json_map
    global_json_map = json_map
    return json_map


root = Tk()
root.title("File Scanner")
root.geometry('600x200')

# New Name ----------------------------
new_name_lbl = Label(root, text="New Name")
new_name_ent = Entry(root, width=50)
new_name_lbl.grid(column=0, row=0, sticky=W)
new_name_ent.grid(column=1, row=0)

# File Path ----------------------------
file_path_ent = Entry(root)
file_path_ent.config(width=50)
file_path_btn = Button(root, text="File Path",
                       command=lambda: get_file_path())
file_path_btn.grid(column=0, row=1)

# Counter ----------------------------
counter_lbl = Label(root, text="Counter")
counter_ent = Entry(root, width=50)
counter_lbl.grid(column=0, row=2, sticky=W)
counter_ent.grid(column=1, row=2)

# Order ----------------------------
order_lbl = Label(root, text="Order")
order_combo = Combobox(root, width=48, state="readonly")
order_combo['values'] = ('Ascending', 'Descending')
order_combo.current(0)  # set the selected item
order_lbl.grid(column=0, row=3, sticky=W)
order_combo.grid(column=1, row=3)

# Map ----------------------------
map_ent = Entry(root)
map_ent.config(width=50)
map_btn = Button(root, text="Get Map",
                 command=lambda: get_json_map_path())
clear_map_btn = Button(root, text="Clear Map",
                       command=lambda: clear_map())

map_btn.grid(column=0, row=4)
clear_map_btn.grid(column=0, row=5, sticky=W)

# Output Folder ----------------------------
output_folder_ent = Entry(root)
output_folder_ent.config(width=50)
output_folder_btn = Button(root, text="Get Output",
                           command=lambda: get_output_path())

output_folder_btn.grid(column=0, row=5)

# Run Button ----------------------------
run_btn = Button(root, text="Run", command=lambda: run())
run_btn.grid(column=1, row=6)

# End frame
root.mainloop()
