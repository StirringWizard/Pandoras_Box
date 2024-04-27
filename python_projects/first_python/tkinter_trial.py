import tkinter as tk

def label_test(root):
    label1 = tk.Label(root, text="Label 1")
    label1.grid(row=0, column=0)

    label2 = tk.Label(root, text="Label 2")
    label2.grid(row=1, column=0)

    button = tk.Button(root, text="Click Me")
    button.grid(row=2, column=0)



def print_entry_content():
    content = e1.get()
    print("Entry 1 content:", content)

def button(root):
    

    # creating main tkinter window/toplevel
    # Create a label widget
    label = tk.Label(root, text="Enter something:")
    label.grid(row=0, column=0)


    # Create a button to print the content of e1
    button = tk.Button(root, text="Print Entry 1 Content", command=print_entry_content)
    button.grid(row=4, column= 1,columnspan=2)  # Spanning two columns

# Create an instance of Tkinter window
root = tk.Tk()
root.geometry("800x600")
# Create an instance of MyButton with row and column specified

button(root)

# Create an Entry widget
e1 = tk.Entry(root)
e1.grid(row=0, column=1)


# Start the Tkinter event loop
root.mainloop()
