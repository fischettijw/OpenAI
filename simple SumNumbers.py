import tkinter as tk

def calculate_sum():
    x = int(x_entry.get())
    y = int(y_entry.get())
    z = x + y
    x_result.config(text="X: " + str(x))
    y_result.config(text="Y: " + str(y))
    z_result.config(text="Z: " + str(z))

root = tk.Tk()
root.title("Addition Calculator")

x_label = tk.Label(root, text="Enter the value of X:")
x_label.grid(row=0, column=0)

x_entry = tk.Entry(root)
x_entry.grid(row=0, column=1)

y_label = tk.Label(root, text="Enter the value of Y:")
y_label.grid(row=1, column=0)

y_entry = tk.Entry(root)
y_entry.grid(row=1, column=1)

calculate_button = tk.Button(root, text="Calculate", command=calculate_sum)
calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

x_result = tk.Label(root, text="")
x_result.grid(row=3, column=0)

y_result = tk.Label(root, text="")
y_result.grid(row=3, column=1)

z_result = tk.Label(root, text="")
z_result.grid(row=4, column=0, columnspan=2)

root.mainloop()
