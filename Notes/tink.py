import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("testing")
root.configure(background = "orange")
root.minsize(250,250)
root.maxsize(1000,1000)
root.geometry("300x100+100+100")
label = tk.Label(root, text="this is working")
label.config(fg ="blue",background="orange")
font=(("Times New Roman"),12,"bold")
label.pack()
#image
image = Image.open("iniduival_projects\download (1).jpg")
# 2. Convert to Tkinter-compatible format
photo = ImageTk.PhotoImage(image)

# 3. Display in a Label
label = tk.Label(root, image=photo)
label.image = photo  # Keep a reference!
label.pack()

#Button 
root.count = 0
def add():
   root.count += 1
   num["text"]= root.count


Btn=tk.Button(root,text="ADD",command=add)
Btn.pack()

num = tk.Label(root,text = "0")
num.pack()
label.pack()


root.mainloop()