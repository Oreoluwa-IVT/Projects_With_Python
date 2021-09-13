from tkinter import *
from typing import Collection
class survey(Frame):
    def __init__(self,master):
        super(survey,self).__init__(master)
        self.grid()
        self.createsurvey()
    
    def createsurvey(self):
        self.lbl=Label(self,text="Please Answer the Survey Appropriately, Thanks you").grid(row=0,column=0,sticky=W)
        self.q1=Label(self,text="Your Full Name").grid(row=1,column=0, sticky=W)
        self.a1=Entry(self).grid(row=2,column=0, sticky=W)
        self.q2=Label(self,text="Email Address").grid(row=3,column=0,sticky=W)
        self.a2=Entry(self).grid(row=4,column=0,sticky=W)
        self.q3=Label(self,text="Residence").grid(row=5,column=0,sticky=W)
        self.a3=Entry(self).grid(row=6,column=0,sticky=W)
        self.q4=Label(self,text="Gender").grid(row=7,column=0,sticky=W)
        self.fav=StringVar()
        self.fav.set(None)
        Radiobutton(self,text="Male",variable=self.fav,value="Male",command=self.getvalue).grid(row=8,column=0,sticky=W)
        Radiobutton(self,text="Female",variable=self.fav,value="Female",command=self.getvalue).grid(row=9,column=0,sticky=W)
        self.checkm=BooleanVar()
        self.checkp=BooleanVar()
        self.q5=Label(self,text="Courses").grid(row=12,column=0,sticky=W)
        Checkbutton(self,text="Mathematics",variable=self.checkm,command=self.math).grid(row=15,column=0,sticky=W)
        Checkbutton(self,text="Physics",variable=self.checkp,command=self.physics).grid(row=16,column=0,sticky=W)
        self.q6=Label(self,text="Your Religion").grid(row=17,column=0,sticky=W)
        self.a4=Entry(self).grid(row=18,column=0,sticky=W)
        self.ent=Text(self,width=40,height=0,wrap=WORD).grid(row=19,column=0,sticky=E)
        self.bttn=Button(self,text="Submit",command=self.compose).grid(row=20,column=0,sticky=W)
        
    def getvalue(self):
       okay= self.fav.get()
       print(okay)
    
      
    def math(self): #this part runs when checkbutton "Mathematics" is selected
        if self.checkm.get():#this part  checks if if the checkbutton was selected
            message="Mathematics"
            self.ent.insert(0.0,message)
            
            
             
    def physics(self):
        print("Female")
        
    def compose(self):
        sum="all"
        self.ent.insert(0.0,sum)
        
        
    
        
        
root=Tk()
root.geometry=("900X900")
root.title("Survey App")
main=survey(root)
main.mainloop()