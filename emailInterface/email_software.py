import tkinter as tk
from tkinter import font

class App:

    root = tk.Tk()
    header_space = tk.Frame(root,bg="#d5dfed")
    content_space = tk.Frame(root,bg="white")

    def initialize():
        App.root.title("CS Club Email")
        App.root.geometry("1000x700+200+200")
        App.root.resizable(True,True)
    
    def widget():
        header_font = font.Font(family="lato",size=12,weight="bold")
        content_font = font.Font(family="lato",size=12,weight="normal")

        App.header_space.pack(fill="x",expand=False,side="top")
        App.content_space.pack(fill="both",expand=True,side="top")

        to_label = tk.Label(App.header_space,text="To: ",bg="#d5dfed",font=header_font)
        to_label.grid(row=1,column=1,pady=(10,5))

        from_label = tk.Label(App.header_space,text="From: ",bg="#d5dfed",font=header_font)
        from_label.grid(row=2,column=1,pady=(5,5))

        subject_label = tk.Label(App.header_space,text="Subject: ",bg="#d5dfed",font=header_font)
        subject_label.grid(row=3,column=1,pady=(5,10))

        to_email = tk.StringVar()
        App.to_input = tk.Entry(App.header_space,textvariable=to_email,borderwidth=0,font=content_font)
        App.to_input.grid(row=1,column=2)

        from_email = tk.StringVar()
        App.from_input = tk.Entry(App.header_space,textvariable=from_email,borderwidth=0,font=content_font)
        App.from_input.grid(row=2,column=2)

        subject = tk.StringVar()
        App.subject_input = tk.Entry(App.header_space,textvariable=subject,borderwidth=0,font=content_font)
        App.subject_input.grid(row=3,column=2)

        send_icon = tk.PhotoImage(file="send.png")
        send_icon = send_icon.subsample(20)
        send_button = tk.Button(App.header_space,image=send_icon)
        send_button.image = send_icon
        send_button.grid(row=1,rowspan=3,column=3)

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
finally:
    App.initialize()
    App.widget()
    tk.mainloop()