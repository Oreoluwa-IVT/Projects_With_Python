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
        self.q4=Label(self,text="Gender").grid(row=7,column=0,sticky=W)
        self.checkb=["male","female"]
        Checkbutton(self,text="Male",command=self.male).grid(row=8,column=0,sticky=W)
        Checkbutton(self,text="Female",command=self.female).grid(row=9,column=0,sticky=W)
        
        
    
        
    def male(self):
        print("male")
    
    def female(self):
        print("female")
        
        
        
    
    



root=Tk()
root.geometry=("900X900")
root.title("Survey App")
main=survey(root)
main.mainloop()