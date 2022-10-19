import imp
from tkinter import Tk, messagebox

root = Tk()

root.geometry("300x300")

messagebox.showinfo("Info","Saved Succefully")
messagebox.showerror("Error","OOps Something went wrong")

root.mainloop()