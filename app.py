import instaloader
from PIL import ImageTk, Image
import tkinter as tk
from tkinter import messagebox


window = tk.Tk()
window.title('Instagram Image Downloader')


def img_download():
    ig = instaloader.Instaloader()
    profile = entry.get()
    ig.download_profile(profile, profile_pic_only=True)
    messagebox.showinfo('Status', 'Image Downloaded Successfully..!')


img = Image.open('ig_logo.jpg')
img = img.resize((200, 200), Image.ANTIALIAS)
resized_img = ImageTk.PhotoImage(img)

# GUI Part
title = tk.Label(window, text='Instagram Image Downloader', font=('Times', 20, 'bold'))
title.grid(row=0, column=0, columnspan=5, padx=30, pady=10)

image = tk.Label(window, image=resized_img)
image.grid(row=2, column=0, columnspan=5, pady=20)

lable1 = tk.Label(window, text='Enter the Username : ', font=('Arial', 10))
lable1.grid(row=3, column=0)

entry = tk.Entry(window, width=40)
entry.grid(row=3, column=1, columnspan=3)

button = tk.Button(window, text='Download', command=img_download)
button.grid(row=4, column=0, columnspan=5, pady=10)

window.mainloop()
