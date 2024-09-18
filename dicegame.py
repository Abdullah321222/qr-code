import tkinter as tk
from PIL import Image,ImageTk
import random

window=tk.Tk()
window.geometry("500x360")
window.title("Dice Roll")
dice = ["one.jpg","two.jpg","three.png","four.png","five.jpg","six.png"]
image1=Image.tk.PhotoImage(Image.open(random.choice(dice)))
image2=Image.tk.PhotoImage(Image.open(random.choice(dice)))
label1=tk.Label(window,image=image1)
label2= tk.Label(window,image=image2)
label1.image =image1
label2.image =image2
label1.place(x=40,y=100)
label2.place(x=300,y=100)
window.mainloop()