from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
import app

global global_filename
global global_json_map


def run():
    # order_combo_val =
    print('New Name:', new_name_ent.get())
    print('File Path:', global_filename)
    print('Counter:', counter_ent.get())
    print('Order Combo:', order_combo.get())
    print('Map:', global_json_map)
    print('Type Map:', type(global_json_map))

    new_name = new_name_ent.get()
    filename = global_filename
    counter = counter_ent.get()
    order = order_combo.get()
    map = global_json_map

    # Set New Name
    new_name = new_name.strip()

    # Set Order
    order = None
    if order_combo.get() == 'Ascending':
        order = 'asc'
    elif order_combo.get() == 'Descending':
        order = 'desc'

    # Set Counter
    counter = int(counter)

    # Set Map
    if map == '':
        map = None

    app.app(new_name, filename, counter, order, map)


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


def clear_map():
    json_map = ''
    map_path_entry = Text(root, state='normal', width=50, height=1)
    map_path_entry.insert('end', json_map)
    map_path_entry.configure(state='disable')
    map_path_entry.grid(column=1, row=4)

    global global_json_map
    global_json_map = json_map
    return json_map


def convert_csv_to_json(csv_file_path):
    csv_file_path = '../data/csv_input.csv'
    json_file_path = '{}.json'.format(csv_file_path[:-4])

    data = {}
    with open(csv_file_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for rows in csv_reader:
            id = rows['ID']
            data[id] = rows['Name']

    with open(json_file_path, 'w') as json_file:
        json_file.write(json.dumps(data, indent=4))


root = Tk()
root.title("File Scanner")
root.geometry('600x200')

# New Name ----------------------------
new_name_lbl = Label(root, text="New Name")
new_name_ent = Entry(root, width=50)
new_name_lbl.grid(column=0, row=0, sticky=W)
new_name_ent.grid(column=1, row=0)

# File Path ----------------------------
file_path_entry = Entry(root)
file_path_entry.config(width=50)
file_path_btn = Button(root, text="File Path", command=lambda: get_file_path())
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
map_entry = Entry(root)
map_entry.config(width=50)
map_btn = Button(root, text="Get Map",
                 command=lambda: get_json_map_path())
clear_map_btn = Button(root, text="Clear Map",
                       command=lambda: clear_map())

map_btn.grid(column=0, row=4)
clear_map_btn.grid(column=0, row=5, sticky=W)

# # Map ----------------------------
# TODO: Create Json form CSV GUI option
# create_map_entry = Entry(root)
# create_map_entry.config(width=50)
# create_map_btn = Button(root, text="Create Map",
#                         command=lambda: get_json_create_map_path())

# create_map_btn.grid(column=0, row=4)

# Run Button ----------------------------
run_btn = Button(root, text="Run", command=lambda: run())
run_btn.grid(column=1, row=5)

# End frame
root.mainloop()
