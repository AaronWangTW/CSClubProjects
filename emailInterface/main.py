import tkinter as tk
import yagmail
import os
import json
from tkinter import font

class App:

    root = tk.Tk()
    header_space = tk.Frame(root,bg="#d5dfed")
    content_space = tk.Frame(root,bg="white")
    save_file = "save.json"

    current_email = None
    wait_flag = tk.IntVar()

    def initialize():
        App.root.title("CS Club Email")
        App.root.geometry("1000x700+200+200")
        App.root.resizable(True,True)

        if not os.path.exists(App.save_file) and not os.path.isfile(App.save_file):
            with open("save.json","w") as f:
                json.dump({},f)
                print("save file created")
        else:
            print("save file accessed")

    def send_email(from_email,to_email,subject,content):
        try:
            yag = yagmail.SMTP(user=from_email, oauth2_file="credentials.json")
            yag.send(to=to_email, subject=subject,contents=content)
            print("email sent successfully")
        except Exception as e:
            print("error sending email",e)

    def save(from_email,to_email,subject,content):
        try:
            save_data = {}
            save_data['from_email']=from_email
            save_data['to_email']=to_email
            save_data['subject']=subject
            save_data['content']=content

            with open(App.save_file,"r") as f:
                save = json.load(f)
            
            id=0
            for key in save.keys():
                if int(key)>id:
                    id = int(key)
            id+=1

            save[id] = save_data

            with open(App.save_file,"w") as f:
                json.dump(save,f,sort_keys=True,indent=4)

            print("Email saved successfully")
        except Exception as e:
            print("Error saving email: ",e)

    def pick_email(event):
        if App.current_email == None:
            App.current_email = event.widget
            App.wait_flag.set(1)
        else:
            pass

    def open_old():
        select_window = tk.Toplevel(App.root)
        select_window.title("Open Old")
        select_window.geometry("300x200")
        select_window.resizable(True,True)

        header = tk.Frame(select_window,bg="black",borderwidth=2)
        header.grid(row=1,column=1,sticky="nswe")
        select_window.grid_columnconfigure(1,weight=1)
        select_window.grid_rowconfigure(1,weight=1)

        id_label = tk.Label(header,text="Id",bg="white")
        id_label.grid(row=1,column=1,sticky="nswe")
        from_label = tk.Label(header,text="From",bg="white")
        from_label.grid(row=1,column=2,sticky="nswe")
        to_label = tk.Label(header,text="To",bg="white")
        to_label.grid(row=1,column=3,sticky="nswe")
        subject_label = tk.Label(header,text="Subject",bg="white")
        subject_label.grid(row=1,column=4,sticky="nswe")

        header.grid_rowconfigure(1,weight=1)
        for i in range(1,5):
            header.grid_columnconfigure(i,weight=1)

        with open(App.save_file,"r") as f:
                save = json.load(f)

        emails = []
        App.wait_flag.set(0)
        App.current_email = None
        wait = tk.Frame(select_window)
        for key in save.keys():
            frame = tk.Frame(select_window,bg="white",borderwidth=2)
            frame.grid(row=int(key)+1,column=1,sticky="nswe")
            select_window.grid_rowconfigure(int(key)+1,weight=1)

            id_l = tk.Label(frame,text=key,bg="white")
            id_l.grid(row=1,column=1,sticky="nswe")
            from_l = tk.Label(frame,text=save[key]['from_email'],bg="white")
            from_l.grid(row=1,column=2,sticky="nswe")
            to_l = tk.Label(frame,text=save[key]['to_email'],bg="white")
            to_l.grid(row=1,column=3,sticky="nswe")
            subject_l = tk.Label(frame,text=save[key]['subject'],bg="white")
            subject_l.grid(row=1,column=4,sticky="nswe")

            for i in range(1,5):
                frame.grid_columnconfigure(i,weight=1)

            frame.bind("<ButtonRelease-1>",App.pick_email)
            

            emails.append(frame)
        wait.wait_variable(App.wait_flag)

        App.render_email(id=App.current_email.winfo_children()[0].cget("text"))

        select_window.destroy()
        select_window.update()
        
    def render_email(id):
        if id == -1:
            App.to_input.delete(0,tk.END)
            App.from_input.delete(0,tk.END)
            App.from_input.insert(0,"honglin2023@gmail.com")
            App.subject_input.delete(0,tk.END)
            App.content_box.delete("1.0",tk.END)
            return

        with open(App.save_file,"r") as f:
            save = json.load(f)
        email = save[id]
        App.to_input.delete(0,tk.END)
        App.to_input.insert(0,email['to_email'])
        App.from_input.delete(0,tk.END)
        App.from_input.insert(0,email['from_email'])
        App.subject_input.delete(0,tk.END)
        App.subject_input.insert(0,email['subject'])
        App.content_box.delete("1.0",tk.END)
        App.content_box.insert("1.0",email['content'])

    def new_email():
        App.render_email(-1)
    
    def widgets():

        menubar = tk.Menu(App.root,background="#FFF",foreground="black")
        file = tk.Menu(menubar, tearoff=0)
        file.add_command(label="New",command=App.new_email)
        file.add_command(label="Open",command=App.open_old)
        file.add_command(label="Save",command=lambda:App.save(from_email=from_email.get(),to_email=to_email.get(),subject=subject.get(),content=App.content_box.get("1.0",tk.END)))
        file.add_command(label="Exit",command=App.root.quit)
        menubar.add_cascade(label="File",menu=file)

        App.root.config(menu=menubar)

        header_font = font.Font(family="lato",size=12,weight="bold")
        content_font = font.Font(family="lato",size=14)

        App.header_space.pack(fill="x",expand=False,side="top")
        App.content_space.pack(fill="both",expand=True,side="top")

        to_label = tk.Label(App.header_space,text="To:",bg="#d5dfed",font=header_font)
        to_label.grid(row=1,column=1,pady=(10,5),sticky="we")

        to_email = tk.StringVar(App.header_space)
        App.to_input = tk.Entry(App.header_space,textvariable=to_email,borderwidth=0,font=content_font)
        App.to_input.grid(row=1,column=2,pady=(10,5),padx=10,ipady=2,sticky="we")

        from_label = tk.Label(App.header_space,text="From:",bg="#d5dfed",font=header_font)
        from_label.grid(row=2,column=1,pady=(5,5),sticky="we")

        from_email = tk.StringVar(App.header_space)
        App.from_input = tk.Entry(App.header_space,textvariable=from_email,borderwidth=0,font=content_font)
        App.from_input.grid(row=2,column=2,pady=(5,5),padx=10,ipady=2,sticky="we")
        App.from_input.insert(0,"honglin2023@gmail.com")

        subject_label = tk.Label(App.header_space,text="Subject:",bg="#d5dfed",font=header_font)
        subject_label.grid(row=3,column=1,pady=(5,10),sticky="we")

        subject = tk.StringVar(App.header_space)
        App.subject_input = tk.Entry(App.header_space,textvariable=subject,borderwidth=0,font=content_font)
        App.subject_input.grid(row=3,column=2,pady=(5,10),padx=10,ipady=2,sticky="we")

        send_icon = tk.PhotoImage(file="send.png")
        send_icon = send_icon.subsample(20)
        send_button = tk.Button(App.header_space,image=send_icon,command=lambda:App.send_email(from_email=from_email.get(),to_email=to_email.get(),subject=subject.get(),content=App.content_box.get("1.0",tk.END)))
        send_button.image = send_icon
        send_button.grid(row=1,rowspan=3,column=3)

        App.header_space.grid_columnconfigure(1,weight=1)
        App.header_space.grid_columnconfigure(2,weight=18)
        App.header_space.grid_columnconfigure(3,weight=1)
        App.header_space.grid_rowconfigure(1,weight=1)
        App.header_space.grid_rowconfigure(2,weight=1)
        App.header_space.grid_rowconfigure(3,weight=1)

        App.content_box = tk.Text(App.content_space,borderwidth=0,font=content_font)
        App.content_box.pack(fill="both",expand=True,padx=5,pady=5)

try:
    from ctypes import windll

    windll.shcore.SetProcessDpiAwareness(1)

finally:
    App.initialize()
    App.widgets()
    tk.mainloop()