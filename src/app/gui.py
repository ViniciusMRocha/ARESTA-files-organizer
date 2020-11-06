from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from tkinter import messagebox
import sys
import os
import app
import config.ui as ui  # TODO: Set up Config file
import config.user as user  # TODO: Set up Config file

global global_file_path
global global_output_path
global global_csv_map
global_csv_map = None


# ======================================== Functions ========================================
def run():
    file_path = global_file_path
    output_folder = global_output_path

    # Set New Name
    # Strip white space and remove spaces to check validity
    if new_name_ent.get().strip().replace(' ', '').isalnum():
        new_name = new_name_ent.get().strip().replace(' ', '_')
    else:
        messagebox.showerror(
            'Error', 'File name has a special character, only characters, numbers and spaces are allowed!')

    # Set Counter
    try:
        counter = int(counter_ent.get())
    except:
        messagebox.showerror('Error', 'Counter is not a number!')

    # Set Order
    order = None
    if order_combo.get() == 'Ascending':
        order = 'asc'
    elif order_combo.get() == 'Descending':
        order = 'desc'

    # Set Map
    global global_csv_map
    map = global_csv_map
    if map == '':
        map = None

    app.app(new_name, file_path, output_folder, counter, order, map)


def cleanup_path(path):
    while "/" in path:
        index = path.find("/")
        path = path[index + 1:len(path)]
    return path


def get_file_path():
    # Value saved on variable
    file_path = filedialog.askopenfilename(initialdir="../data/",
                                           title="Select a File",
                                           filetypes=(("PDF", "*.pdf"), ("all files", "*.*")))

    # Set display value
    file_path_ent = Text(root, state='normal', width=22, height=1)
    file_path_display_val = cleanup_path(file_path)
    file_path_ent.insert('end', file_path_display_val)
    file_path_ent.configure(state='disable')
    file_path_ent.grid(column=1, row=0, columnspan=2, sticky=W)

    # Save variable as a Global Variable
    global global_file_path
    global_file_path = file_path
    return file_path


def get_csv_map_path():
    # Value saved on variable
    csv_map = filedialog.askopenfilename(initialdir="../data/",
                                         title="Select a File",
                                         filetypes=(("CSV", "*.csv"), ("all files", "*.*")))
    map_path_ent = Text(root, state='normal', width=22, height=1)

    # Set display value
    csv_map_display_val = cleanup_path(csv_map)
    map_path_ent.insert('end', csv_map_display_val)
    map_path_ent.configure(state='disable')
    map_path_ent.grid(column=1, row=4, columnspan=2, sticky=W)

    # Save variable as a Global Variable
    global global_csv_map
    global_csv_map = csv_map
    return csv_map


def get_output_path():
    # Value saved on variable
    output_path = filedialog.askdirectory(initialdir="../../",
                                          title="Select a File")
    output_path_ent = Text(root, state='normal', width=22, height=1)

    # Set display value
    output_path_display_val = cleanup_path(output_path)
    output_path_ent.insert('end', output_path_display_val)
    output_path_ent.configure(state='disable')
    output_path_ent.grid(column=1, row=5, columnspan=2, sticky=W)

    # Save variable as a Global Variable
    global global_output_path
    global_output_path = output_path
    return output_path


def resert_inputs():
    # Reruns the scripts
    python = sys.executable
    os.execl(python, python, * sys.argv)


# ======================================== GUI ========================================
root = Tk()
root.title("File Scanner")
root.geometry('350x200')

# File Path ----------------------------
file_path_ent = Entry(root)
file_path_ent.config(width=22)
file_path_btn = Button(root, text="File Path", command=lambda: get_file_path())

# New Name ----------------------------
new_name_lbl = Label(root, text="New Name")
new_name_ent = Entry(root, width=22)

# Counter ----------------------------
counter_lbl = Label(root, text="Counter")
counter_ent = Entry(root, width=22)

# Order ----------------------------
order_lbl = Label(root, text="Order")
order_combo = Combobox(root, width=22, state="readonly")
# order_combo['values'] = ('Ascending', 'Descending')
order_combo['values'] = ui.order_options
order_combo.current(0)  # Set a default value

# Map ----------------------------
map_ent = Entry(root)
map_ent.config(width=22)
map_btn = Button(root, text="Get Map", command=lambda: get_csv_map_path())

# Output Folder ----------------------------
output_folder_ent = Entry(root)
output_folder_ent.config(width=22)
output_folder_btn = Button(root, text="Output", command=lambda: get_output_path())

# Reset Button ----------------------------
resert_btn = Button(root, text="Reset", command=lambda: resert_inputs())

# Run Button ----------------------------
run_btn = Button(root, text="Run", command=lambda: run())

# Menu ----------------------------


def test():
    pass


my_menu = Menu(root)
root.config(menu=my_menu)

settings_menu = Menu(my_menu)

my_menu.add_cascade(label="Settings", menu=settings_menu)
settings_menu.add_command(label='Set Root', command=test())
settings_menu.add_command(label='Language', command=test())
settings_menu.add_separator()
settings_menu.add_command(label='View Count', command=test())
settings_menu.add_separator()
settings_menu.add_command(label='Exit', command=root.quit)


# ======================================== LAYOUT ========================================
file_path_btn.grid(column=0, row=0, sticky=E)

new_name_lbl.grid(column=0, row=1, sticky=E)
new_name_ent.grid(column=1, row=1, columnspan=2, sticky=W)

counter_lbl.grid(column=0, row=2, sticky=E)
counter_ent.grid(column=1, row=2, columnspan=2, sticky=W)

order_lbl.grid(column=0, row=3, sticky=E)
order_combo.grid(column=1, row=3, columnspan=2, sticky=W)

map_btn.grid(column=0, row=4, sticky=E)

output_folder_btn.grid(column=0, row=5, sticky=E)

resert_btn.grid(column=1, row=7)

run_btn.grid(column=2, row=7)


# End frame
root.mainloop()
