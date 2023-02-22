from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import qrcode

master = Tk()

class App(Tk):
    
    def __init__(self):

        master.title("QrCode Generator")
        master.resizable(False,False)
        
        self.img = PhotoImage(file="qr-code.png")
        master.iconphoto(False,self.img)

        self.canvas = Canvas(master, height=450, width=800)
        self.canvas.pack()

        self.top_frame = Frame(master,bg="#516150")
        self.top_frame.place(relx=0.02,rely=0.03,relwidth=0.96,relheight=0.1)

        self.left_frame = Frame(master,bg="#516150")
        self.left_frame.place(relx=0.02,rely=0.15,relwidth=0.47,relheight=0.82)

        self.right_frame = Frame(master,bg="#516150")
        self.right_frame.place(relx=0.51,rely=0.15,relwidth=0.47,relheight=0.82)

        self.main_title = Label(self.top_frame,bg="#516150",text="QrCode Generator",font=("Verdana",17,"bold"),fg="#ffffff")
        self.main_title.pack(anchor=CENTER)

        self.url_label = Label(self.left_frame,bg="#516150",text="Text or URL",font=("Verdana",15,"bold"),fg="#ffffff")
        self.url_label.place(x=20,y=20)

        self.url_entry = Entry(self.left_frame,font=("Verdana",10,"bold"),width=36)
        self.url_entry.place(x=23,y=70)

        self.file_name_label = Label(self.left_frame,bg="#516150",text="PNG Name",font=("Verdana",15,"bold"),fg="#ffffff")
        self.file_name_label.place(x=20,y=100)

        self.file_name_entry = Entry(self.left_frame,font=("Verdana",10,"bold"),width=36)
        self.file_name_entry.place(x=23,y=150)

        self.file_location_button = Button(self.left_frame,text="Select Folder",font=("Verdana",10,"bold"),bg="#3b423a",fg="#ffffff",width=36,height=2,command=self.ask_directory)
        self.file_location_button.place(x=23,y=200)

        self.file_location_label = Label(self.left_frame,text="...",bg="#516150",fg="#ffffff",font=("Verdana",10,"bold"))
        self.file_location_label.place(x=20,y=260)

        self.generate_button = Button(self.left_frame,text="Generate",font=("Verdana",10,"bold"),bg="#3b423a",fg="#ffffff",width=36,height=2,command=self.generate_qrcode)
        self.generate_button.place(x=23,y=300)

        self.img_view_label = Label(self.right_frame,bg="#516150")
        self.img_view_label.pack(padx=5,pady=35,anchor="center")
    
    def ask_directory(self):
        
        self.file_path = filedialog.askdirectory()

        self.file_location_label.config(text=self.file_path)

    def generate_qrcode(self):
        
        try:

            self.file_name = self.file_name_entry.get()
            self.text_url = self.url_entry.get()

            self.qr_code = qrcode.make(self.text_url)
            self.qr_code.save(self.file_path + "/" + str(self.file_name) + ".png")

            self.img = PhotoImage(file= self.file_path + "/" + str(self.file_name) + ".png")
            self.img_view_label.config(image=self.img)

            message = "Your QrCode has been created."
            messagebox.showinfo("Success!",message)
        
        except Exception as err:
            
            message = "QrCode creation has crashed!"
            messagebox.showerror("Failed!",message)

app = App()
master.mainloop()