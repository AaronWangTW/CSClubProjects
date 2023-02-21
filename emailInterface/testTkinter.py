import tkinter as tk

root = tk.Tk()

root.title("test program")
root.geometry("800x550+200+200")
root.resizable(True,True)

block1 = tk.Frame(root,bg="black",width=100,height=50)
block1.pack()

def clicked():
    print("clicked!")

button1 = tk.Button(root,text="click me!",width=10,height=1,command=clicked)
button1.pack(side="right")




root.mainloop()