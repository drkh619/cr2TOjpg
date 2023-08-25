import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from PIL import Image
import os
import threading

def convert_files(input_dir, output_dir):
    files_to_convert = [filename for filename in os.listdir(input_dir) if filename.lower().endswith(".cr2")]
    total_files = len(files_to_convert)
    
    for index, filename in enumerate(files_to_convert):
        cr2_file = os.path.join(input_dir, filename)
        jpg_file = os.path.join(output_dir, os.path.splitext(filename)[0] + ".jpg")
        try:
            with Image.open(cr2_file) as im:
                im.save(jpg_file, "JPEG")
            status_label.config(text=f"Converted: {filename}")
        except Exception as e:
            status_label.config(text=f"Error converting {filename}: {str(e)}")
        
        # Update the progress bar
        progress = (index + 1) / total_files * 100
        progress_var.set(progress)
        app.update_idletasks()

def select_input_dir():
    input_dir = filedialog.askdirectory()
    input_dir_entry.delete(0, tk.END)
    input_dir_entry.insert(0, input_dir)

def select_output_dir():
    output_dir = filedialog.askdirectory()
    output_dir_entry.delete(0, tk.END)
    output_dir_entry.insert(0, output_dir)

def convert():
    input_dir = input_dir_entry.get()
    output_dir = output_dir_entry.get()
    if not input_dir or not output_dir:
        status_label.config(text="Please select input and output directories.")
        return
    
    # Create a separate thread for conversion to avoid freezing the GUI
    conversion_thread = threading.Thread(target=convert_files, args=(input_dir, output_dir))
    conversion_thread.start()

app = tk.Tk()
app.title("CR2 to JPG Converter")

frame = tk.Frame(app)
frame.pack(padx=10, pady=10)

input_dir_label = tk.Label(frame, text="Input Directory:")
input_dir_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

input_dir_entry = tk.Entry(frame)
input_dir_entry.grid(row=0, column=1, padx=5, pady=5)

input_dir_button = tk.Button(frame, text="Select", command=select_input_dir)
input_dir_button.grid(row=0, column=2, padx=5, pady=5)

output_dir_label = tk.Label(frame, text="Output Directory:")
output_dir_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

output_dir_entry = tk.Entry(frame)
output_dir_entry.grid(row=1, column=1, padx=5, pady=5)

output_dir_button = tk.Button(frame, text="Select", command=select_output_dir)
output_dir_button.grid(row=1, column=2, padx=5, pady=5)

convert_button = tk.Button(frame, text="Convert", command=convert)
convert_button.grid(row=2, column=0, columnspan=3, padx=5, pady=10)

progress_var = tk.DoubleVar()
progress_bar = ttk.Progressbar(frame, variable=progress_var, maximum=100)
progress_bar.grid(row=3, column=0, columnspan=3, padx=5, pady=5, sticky="we")

status_label = tk.Label(frame, text="")
status_label.grid(row=4, column=0, columnspan=3, padx=5, pady=5)

app.mainloop()
