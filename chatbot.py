from tkinter import*
import tkinter

class App:
	def __init__(self,root):
		self.root=root
		self.w=self.root.winfo_screenwidth()
		self.h=self.root.winfo_screenheight()
		self.root.overrideredirect(True)
		self.root.geometry(str(self.w)+"x"+str(self.h)+"+0+0")
		self.root.config(bg="white")
		self.string=StringVar()
		
		self.dict ={"hi":"hello","how are you":"I'm fine","who are you":"I'm chat bot"}
		
	def main(self):
		self.btnw=250
		self.btnh=100
		self.labelw=600
		self.labelh=150
		self.mainbg = Label(self.root,bg="#765AFC",fg="white",font=("Arial", 10 , "bold"))
		self.mainbg.place(x=0,y=0,width=self.w,height=self.h)
		
		self.label = Label(self.mainbg,text="Chat Bot",fg="white",bg="#765AFC",font=("Arial" , 25, "bold" ,"italic"))
		self.label.place(x=self.w/2-self.labelw/2,y=150,width=self.labelw,height=self.labelh)
		
		self.startbtn = Button(self.mainbg,bg="white",bd=0,fg="#765AFC",text="Start",font=("Halvatica",10,"bold"),command=self.chat)
		self.startbtn.place(x=self.w/2-self.btnw/2,y=self.h/2-self.btnh/2,width=250,height=100)
		
		
	def chat(self):
		self.chatbg = Label(self.root,bg="white",fg="white",font=("Arial", 10 , "bold"))
		self.chatbg.place(x=0,y=0,width=self.w,height=self.h)
		
		self.navlabel = Label(self.chatbg,text="Start Chatting",bg="#765AFC",fg="white",font=("Arial",10,"bold"))
		self.navlabel.place(x=0,y=0,width=self.w,height=120)
		
		self.frame = Frame(self.chatbg,bg="white")
		self.frame.place(x=20,y=150,width=self.w-40,height=1000)
		
		self.backbtn = Button(self.chatbg,bg="#765AFC",bd=0,fg="white",text="<<-",font=("Halvatica",10,"bold"),command=self.main)
		self.backbtn.place(x=20,y=10,width=100,height=100)
		
		self.entry = Entry(self.chatbg,bd=5,textvariable=self.string,placeholder="  Message",fg="gray40",bg="gray95")
		self.entry.place(x=20,y=1150,width=self.w-200,height=100)
		
		self.enterbtn = Button(self.chatbg,bg="#765AFC",bd=0,fg="white",text="《》",font=("Halvatica",10,"bold"),command=self.send)
		self.enterbtn.place(x=self.w-180,y=1150,width=170,height=100)
		
	def send(self):
		self.label1 = Label(self.frame,text=(" You :   "+self.string.get()+" "),bg="#765AFC",fg="white",font=("Arial",10,"bold"))
		self.label1.pack(anchor="e")
		
		try:
			txt=self.dict[self.string.get().lower()]
		except:
			txt="Plz ask another question"
			
		self.label2 = Label(self.frame,text=(" Bot :   ")+txt+" ",bg="gray90",fg="gray30",font=("Arial",10,"bold"))
		self.label2.pack(anchor="w")
		
		self.string.set("")
		
		pass
		
root=Tk()
obj=App(root)
obj.main()
root.mainloop()