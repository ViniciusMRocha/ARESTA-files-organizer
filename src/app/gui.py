from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
import app


def run():
    # order_combo_val =
    print('New Name:', new_name_ent.get())
    print('File Path:', global_filename)
    print('Counter:', counter_ent.get())
    print('Order Combo:', order_combo.get())
    print('Map:', global_json_map)

    app.app(new_name_ent.get(), global_filename, counter_ent.get(), order_combo.get(), map=global_json_map)


def get_file_path():
    filename = filedialog.askopenfilename(initialdir="../data/",
                                          title="Select a File",
                                          filetypes=(("PDF", "*.pdf"), ("all files", "*.*")))
    file_path_entry = Text(root, state='normal', width=50, height=1)
    file_path_entry.insert('end', filename)
    file_path_entry.configure(state='disable')
    file_path_entry.grid(column=1, row=1)

    global global_filename
    global_filename = filename
    return filename


def get_json_map_path():
    json_map = filedialog.askopenfilename(initialdir="../data/",
                                          title="Select a File",
                                          filetypes=(("JSON", "*.json"), ("all files", "*.*")))
    map_path_entry = Text(root, state='normal', width=50, height=1)
    map_path_entry.insert('end', json_map)
    map_path_entry.configure(state='disable')
    map_path_entry.grid(column=1, row=4)

    global global_json_map
    global_json_map = json_map
    return json_map


root = Tk()
root.title("File Scanner")
root.geometry('350x200')

# New Name ----------------------------
new_name_lbl = Label(root, text="New Name")
new_name_ent = Entry(root, width=22)
new_name_ent_val = new_name_ent.get()
new_name_lbl.grid(column=0, row=0)
new_name_ent.grid(column=1, row=0)

# File Path ----------------------------
file_path_entry = Entry(root)
file_path_entry.config(width=22)
file_path_btn = Button(root, text="File Path", command=lambda: get_file_path())
file_path_entry_val = file_path_entry.get()
file_path_btn.grid(column=0, row=1)

# Counter ----------------------------
counter_lbl = Label(root, text="Counter")
counter_ent = Entry(root, width=22)
counter_ent_val = counter_ent.get()
counter_lbl.grid(column=0, row=2)
counter_ent.grid(column=1, row=2)

# Order ----------------------------
order_lbl = Label(root, text="Order")
order_combo = Combobox(root)
order_combo['values'] = ('Ascending', 'Descending')
order_combo.current(1)  # set the selected item
order_lbl.grid(column=0, row=3)
order_combo.grid(column=1, row=3)

# Map ----------------------------
map_entry = Entry(root)
map_entry.config(width=22)
map_btn = Button(root, text="Get Map",
                 command=lambda: get_json_map_path())
map_ent_val = map_entry.get()
map_btn.grid(column=0, row=4)

# Run Button ----------------------------
run_btn = Button(root, text="Run", command=run)
run_btn.grid(column=1, row=5)

# End frame
root.mainloop()
