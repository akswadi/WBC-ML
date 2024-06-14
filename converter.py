from tkinter import *
from tkinter import filedialog as fd
from PIL import Image
from tkinter import messagebox
import os

root = Tk()
root.title("Image_Conversion_App")

def jpg_to_png():
    # import the image from the folder
    import_filenames = fd.askopenfilenames(filetypes=[("JPEG files", "*.jpg")])
    for import_filename in import_filenames:
        im1 = Image.open(import_filename)
        # Get the directory and filename without extension
        export_directory = os.path.dirname(import_filename)
        filename = os.path.splitext(os.path.basename(import_filename))[0]
        # Construct the export filename with PNG extension in the same directory
        export_filename = os.path.join(export_directory, filename + ".png")
        im1.save(export_filename)
    messagebox.showinfo("Success", "Your Images converted to PNG")

def png_to_jpg():
    # import the image from the folder
    import_filenames = fd.askopenfilenames(filetypes=[("PNG files", "*.png")])
    for import_filename in import_filenames:
        im1 = Image.open(import_filename)
        # Get the directory and filename without extension
        export_directory = os.path.dirname(import_filename)
        filename = os.path.splitext(os.path.basename(import_filename))[0]
        # Construct the export filename with JPG extension in the same directory
        export_filename = os.path.join(export_directory, filename + ".jpg")
        im1.save(export_filename)
    messagebox.showinfo("Success", "Your Images converted to JPG")

button1 = Button(root, text="JPG_to_PNG", width=20, height=2, bg="green",
                fg="white", font=("helvetica", 12, "bold"), command=jpg_to_png)
button1.place(x=120, y=120)

button2 = Button(root, text="PNG_to_JPEG", width=20, height=2, bg="green",
                fg="white", font=("helvetica", 12, "bold"), command=png_to_jpg)
button2.place(x=120, y=220)

root.geometry("500x500+400+200")
root.mainloop()
