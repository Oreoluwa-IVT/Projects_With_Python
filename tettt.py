import tkinter as tk


parent = tk.Tk()
button = tk.Button(text="QUIT",
bd=10,
bg="grey",
fg="red",
command=quit,
activeforeground="Orange",
activebackground="blue",
font="Andalus",
height=2,
highlightcolor="purple",
justify="right",
padx=10,
pady=10,
relief="groove",
)

parent.mainloop()