import tkinter as tk
from tkinter import messagebox
import base58

def integers_to_bytes(int_list):
    """Convert a list of integers to bytes."""
    return bytes(int_list)

def bytes_to_base58(byte_data):
    """Convert bytes to a Base58-encoded string."""
    return base58.b58encode(byte_data).decode('utf-8')

def integers_to_base58(int_list):
    """Convert a list of integers to a Base58-encoded string."""
    byte_data = integers_to_bytes(int_list)
    base58_encoded = bytes_to_base58(byte_data)
    return base58_encoded

def base58_to_bytes(base58_str):
    """Convert a Base58-encoded string to bytes."""
    return base58.b58decode(base58_str)

def bytes_to_integers(byte_data):
    """Convert bytes to a list of integers."""
    return list(byte_data)

def base58_to_integers(base58_str):
    """Convert a Base58-encoded string to a list of integers."""
    byte_data = base58_to_bytes(base58_str)
    int_list = bytes_to_integers(byte_data)
    return int_list

def convert():
    try:
        if conversion_type.get() == "Encode":
            int_list = list(map(int, input_text.get("1.0", "end-1c").split(',')))
            result = integers_to_base58(int_list)
        elif conversion_type.get() == "Decode":
            base58_str = input_text.get("1.0", "end-1c")
            result = base58_to_integers(base58_str)
        result_text.delete("1.0", "end")
        result_text.insert("1.0", str(result))
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the main window
root = tk.Tk()
root.title("Integer <-> Base58 Converter")

# Create and place the widgets
tk.Label(root, text="Input:").grid(row=0, column=0, padx=10, pady=10, sticky='nw')
input_text = tk.Text(root, height=10, width=60)
input_text.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Conversion Type:").grid(row=1, column=0, padx=10, pady=10, sticky='w')
conversion_type = tk.StringVar(value="Encode")
tk.Radiobutton(root, text="Encode (Integers to Base58)", variable=conversion_type, value="Encode").grid(row=1, column=1, sticky='w', padx=20)
tk.Radiobutton(root, text="Decode (Base58 to Integers)", variable=conversion_type, value="Decode").grid(row=1, column=1, sticky='w', padx=250)

tk.Button(root, text="Convert", command=convert).grid(row=2, column=0, columnspan=2, padx=10, pady=10)

tk.Label(root, text="Result:").grid(row=3, column=0, padx=10, pady=10, sticky='nw')
result_text = tk.Text(root, height=10, width=60)
result_text.grid(row=3, column=1, padx=10, pady=10)

# Start the GUI event loop
root.mainloop()
