from  tkinter import *
class Restaurant(Frame):
    def __init__(self,master):
        super(Restaurant,self).__init__(master)
        self.grid()
        self.createwidget()
        
    def createwidget(self):
        self.pw_ent=Entry(self)
        self.pw_ent.grid(row=1,column=1,sticky=W)
        self.submit_bttn=Button(self,text="Submit",command=self.reveal) #command here simply triggers the event handler
        self.submit_bttn.grid(row=2,column=0, sticky=W)
        self.secret_txt=Text(self,width=35,height=5,wrap=WORD) #wrap WORD here simply means that once you get the end of the line , 
        #the next word you type goes to the next line
        self.secret_txt.grid(row=3,column=0,columnspan=2,sticky=W)
        
    def reveal(self):
        """Display message based on password"""
        contents=self.pw_ent.get() #this get() method simply gets the values from the pw_ent variable assigned to the Entry Widget
        

root=Tk()
root.geometry=("400X400")
root.title("Okay")
okay=Restaurant(root)
okay.mainloop()