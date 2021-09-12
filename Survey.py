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




root=Tk()
root.geometry=("400X400")
root.title("Survey App")
main=survey(root)
main.mainloop()