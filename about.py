import tkinter 
import sys
from time import sleep
import webbrowser

root = tkinter.Tk()
root.title("About")
root.geometry("400x550")
root.resizable(0, 0)

def info_po(button1):
    sleep(0.5)
    webbrowser.open("https://github.com/Hisaki714/Communication-Software-SSH-")

def exit(button6):
    sys.exit()
    root.destroy()

label = tkinter.Label(text="                                          About                                          ", background='#7fffd4', font=("MSゴシック", "45", "bold"), foreground='#000000')
label.pack()

label = tkinter.Label(root, text="Now, even if your computer breaks, you won't be responsible for it. ")
label.pack()
label = tkinter.Label(root, text="Also, whether this works well depends on the operating system ")
label.pack()
label = tkinter.Label(root, text="of your computer.")
label.pack()
label = tkinter.Label(root, text="                                                                    ")
label.pack()
label = tkinter.Label(root, text="Version.2.3")
label.pack()

button1 = tkinter.Button(text='Go to github page.', width=2000)
button1.pack()
button1.bind("<Button-1>",info_po)

button6 = tkinter.Button(text='Exit', width=1000)
button6.pack()
button6.bind("<Button-1>",exit)

root.mainloop()
