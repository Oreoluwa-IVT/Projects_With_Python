from  tkinter import *
class Restaurant(Frame):
    def __init__(self,master):
        super(Restaurant,self).__init__(master)
        self.grid()
        self.createwidget()
        
    def createwidget(self):
        self.lbl=Label(self,text="Enter Username")
        self.lbl.grid(row=1,column=0, sticky=W)
        self.pw_ent=Entry(self)
        self.pw_ent.grid(row=2,column=0,sticky=W)
        self.submit_bttn=Button(self,text="Submit",command=self.reveal) #command here simply triggers the event handler
        self.submit_bttn.grid(row=3,column=0, sticky=W)
        self.secret_txt=Text(self,width=35,height=5,wrap=WORD) #wrap WORD here simply means that once you get the end of the line , 
        #the next word you type goes to the next line
        self.secret_txt.grid(row=9,column=0,columnspan=2,sticky=W)
        
    def reveal(self):
        """Display message based on password"""
        contents=self.pw_ent.get() #this get() method simply gets the values from the pw_ent variable assigned to the Entry Widget
        
        if contents=="secret":
            message="Flight Ticket No: 1538438 \n Ticket Owner: James Okunde \n Ticket Price: $540"
        
        else:
            message="Invalid Credentials. Make sure your details are entered correctly"
            
        #now that I have the string that I want to show to the user , all I 
        # all i need to do now is insert it into the Text Widget.
        
        self.secret_txt.delete(0.0,END)

root=Tk()
root.geometry=("400X400")
root.title("FlyAnywhere")
okay=Restaurant(root)
okay.mainloop()