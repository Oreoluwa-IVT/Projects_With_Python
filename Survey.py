from tkinter import *
class survey(Frame):
    def __init__(self,master):
        super(survey,self).__init__(master)
        self.grid()
        self.createsurvey()
    
    def createsurvey(self):
        self.lbl=Label(self,text="Please Answer the Survey Appropriately, Thanks you").grid(row=0,column=0)
        self.q1=Label(self,text="Your Full Name").grid(row=1,column=0, sticky=W)
        self.a1=Entry(self).grid(row=2,column=0, sticky=W)
        self.q2=Label(self,text="Email Address").grid(row=3,column=0,sticky=W)
        self.a2=Entry(self).grid(row=4,column=0,sticky=W)
        self.q3=Label(self,text="Residence").grid(row=5,column=0,sticky=W)
        self.a3=Entry(self).grid(row=6,column=0,sticky=W)
        
    
    



root=Tk()
root.geometry=("900X900")
root.title("Survey App")
main=survey(root)
main.mainloop()