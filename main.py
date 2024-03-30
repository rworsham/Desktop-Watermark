from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageFont, ImageDraw, ImageTk

window = Tk()
window.minsize(width=1350, height=600)
window.maxsize(width=1350, height=600)
window.title("Watermark")

def file_grab():
    image_path = filedialog.askopenfilename(initialdir="/", title="Select A File",filetype=(("jpeg", "*.jpg"), ("png", "*.png")))
    file_location.configure(state=NORMAL)
    file_location.insert(string=str(image_path), index=1)
    file_location.configure(state=DISABLED)
    label = Label(left,text="Image Upload : ")
    label.grid(column=0,row=0, sticky=N)
    label.configure(text=f"Image Upload : {image_path}")
    display_image()


def display_image():
    image = Image.open(fp=file_location.get(), mode='r').resize((900,600))
    display = ImageTk.PhotoImage(image=image)
    picture_display = Label(left, image=display)
    picture_display.image = display
    picture_display.grid(column=0, row=1)


def display_watermark():
    image = combined.resize((900,600))
    display = ImageTk.PhotoImage(image=image)
    picture_display = Label(left, image=display)
    picture_display.image = display
    picture_display.grid(column=0, row=1)


def watermark():
    global combined
    image = Image.open(file_location.get()).convert("RGBA")
    txt = Image.new("RGBA", image.size,(255, 255, 255, 0))
    watermark_image = image.copy()
    draw = ImageDraw.Draw(txt)
    font = ImageFont.truetype("arial.ttf", font_size.get())
    x, y = image.size
    for lines in range(x//160):
        draw.text((lines*160,lines*100), user_text.get(), (255, 255, 255, transparency_level.get()), font=font)
    combined = Image.alpha_composite(watermark_image, txt)
    display_watermark()

def save_image():
    save_location = filedialog.asksaveasfilename(initialdir="/", title="Select A File", filetype=(("png", "*.png") , ("jpeg", "*.jpg")),defaultextension='*.png')
    print(save_location)
    combined.save(save_location)


def scale_used(value):
    print(value)

def reset_variables():
    user_text.delete(0, END)
    transparency_level.set(0)
    file_location.configure(state=NORMAL)
    file_location.delete(0, END)
    file_location.configure(state=DISABLED)
    font_size.set(0)


right = Frame(window,width=300, height=600)
right.grid(column=1,row=0, sticky=N)
left = Frame(window,width=900, height=600,highlightbackground="black",highlightthickness=1)
left.grid(column=0,row=0, sticky=N)
user_text_label = Label(right, text="Enter Text to show on Image: ")
user_text_label.grid(column=1,row=1, sticky=N, pady=20)
user_text = Entry(right,width=42)
user_text.grid(column=2,row=1, sticky=N, pady=20)
transparency_level = Scale(right,from_=0, to=255,orient=HORIZONTAL, command=scale_used, width=10, length=250)
transparency_level.grid(column=2,row=2, sticky=N,pady=20)
transparency_level_label = Label(right, text="Transparency level: ")
transparency_level_label.grid(column=1,row=2, sticky=N, pady=20)
font_size = Scale(right,from_=1, to=142,orient=HORIZONTAL, command=scale_used, width=10, length=250)
font_size.grid(column=2,row=3, sticky=N,pady=20)
font_size_label = Label(right, text="Font Size: ")
font_size_label.grid(column=1,row=3, sticky=N, pady=20)
file_select_label = Label(right, text="File path for image to edit: ")
file_select_label.grid(column=1,row=5, sticky=N)
file_select = Button(right, text="Image Select", command=file_grab)
file_select.grid(column=2,row=4, sticky=N)
file_location = Entry(right,  width=42)
file_location.grid(column=2,row=5, sticky=N)
file_location.configure(state=DISABLED)
reset_button = Button(right, text="Reset Variables", command=reset_variables)
reset_button.grid(column=2, row=7,sticky=W, pady=40)
watermark_button = Button(right, text="Watermark", command=watermark)
watermark_button.grid(column=1,row=7, sticky=E, pady=40)
Save_button = Button(right, text="Save", command=save_image)
Save_button.grid(column=2,row=8, sticky=W, pady=40)


window.mainloop()

