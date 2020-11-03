from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog


def run():
    # order_combo_val =
    print('File Prefix:', file_prefix_ent.get())
    # print('File Path:', file_path_ent.get())
    print('Counter:', counter_ent.get())
    print('Order Combo:', order_combo.get())
    print('Map:', map_ent.get())

    file_prefix_ent.configure(text="File Opened: ")
    file_path_ent.configure(text="File Opened: ")
    counter_ent.configure(text="File Opened: ")
    map_ent.configure(text="File Opened: ")


def browse_files(file_type, extension):
    filename = filedialog.askopenfilename(initialdir="/Users/viniciusrocha/development/ARESTA-files-organizer/src/data",
                                          title="Select a File",
                                          filetypes=(("{}".format(file_type), "*.{}".format(extension)), ("all files", "*.*")))
    # Change label contents
    file_path_ent.configure(text=filename)


root = Tk()
root.title("File Scanner")
root.geometry('350x200')

# Elements ==========
file_prefix_lbl = Label(root, text="New Name")
file_prefix_ent = Entry(root, width=22)
file_prefix_ent_val = file_prefix_ent.get()

file_path_ent = Label(root, width=22)
file_path_btn = Button(root, text="File Path",
                       command=lambda: browse_files('PDF', 'pdf'))

# file_path_ent_val = file_path_ent.get()


counter_lbl = Label(root, text="Counter")
counter_ent = Entry(root, width=22)
counter_ent_val = counter_ent.get()

order_lbl = Label(root, text="Order")
order_combo = Combobox(root)
order_combo['values'] = ('Ascending', 'Descending')
order_combo.current(1)  # set the selected item
# order_combo_val = order_combo.get()

map_btn = Button(root, text="Get Map",
                 command=lambda: browse_files('JSON', 'json'))
map_ent = Entry(root, width=22)
map_ent_val = map_ent.get()

label_file_explorer = Label(root, text="File Explorer using Tkinter")

run_btn = Button(root, text="Run", command=run)


# Grid ==========

file_prefix_lbl.grid(column=0, row=0)
file_prefix_ent.grid(column=1, row=0)

file_path_btn.grid(column=0, row=1)
file_path_ent.grid(column=1, row=1)

counter_lbl.grid(column=0, row=2)
counter_ent.grid(column=1, row=2)

order_lbl.grid(column=0, row=3)
order_combo.grid(column=1, row=3)

map_btn.grid(column=0, row=4)
map_ent.grid(column=1, row=4)

run_btn.grid(column=1, row=5)
# filename.grid(column=1, row=5)
label_file_explorer.grid(column=1, row=6)

root.mainloop()


# # Running APP - Test Order desc
# file_prefix = 'Test_Order_Desc'
# pdf_path = '../data/test-input.pdf'
# counter = 2020
# order = 'desc'
# map = '../data/map.json'
# app(file_prefix, pdf_path, counter, order)
