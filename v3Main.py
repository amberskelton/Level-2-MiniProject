# the following program is a simple multichoice quiz to help you decide which breed of cat/dog to get

import v2Functions#to access functions from the other file containing questions, breeds, and info
import sys#sys.exit() to exit program
import tkinter as tk
from PIL import Image, ImageTk

root=tk.Tk()
root.title("Ideal Cat/Dog Breed Quiz")
root.geometry("1000x1000")

def show_frame(frame):
    frame.tkraise()

#create frames
fr_instructions=tk.Frame(root)
fr_catordog=tk.Frame(root)
fr_catoption=tk.Frame(root)
fr_dogoption=tk.Frame(root)
#using for loop to bring forward frame 
for frame in (fr_instructions,fr_catordog,fr_catoption,fr_dogoption):
    frame.place(relwidth=1,relheight=1)

#frame 1 instructions
img1=Image.open("placeholder.png")#image
img1=img1.resize((250,250))
photo1=ImageTk.PhotoImage(img1)

tk.Label(fr_instructions,justify="left", anchor="w", padx=20,pady=20,text="About this quiz:\nThe following program is a simple multi-choice quiz to help owners that have difficulty deciding which breed of cat/dog to get!\nThis quiz will find a breed that is suitable to your physical and behavioural preferences.\nPlease note that the questions asked are based on generalised breed traits and that individual pets may differ!\nAlso, please remember to research more about your suggested breed to ensure you are confident and know the correct requirements to meet its needs.").pack()
tk.Label(fr_instructions,image=photo1).pack()
tk.Button(fr_instructions,text="Questions",command=lambda:show_frame(fr_catordog)).pack()

#frame 2 cat or dog question
img2=Image.open("placeholder.png")#image
img2=img2.resize((250,150))
photo2=ImageTk.PhotoImage(img2)

tk.Label(fr_catordog,text='Do you want a cat or a dog?').pack()
tk.Label(fr_catordog,image=photo2).pack()
tk.Button(fr_catordog,text="Cat",command=lambda:show_frame(fr_catoption)).pack()
tk.Button(fr_catordog,text="Dog",command=lambda:show_frame(fr_dogoption)).pack()

#frame 3 cat option
img3=Image.open("placeholder.png")#image
img3=img3.resize((150,100))
photo3=ImageTk.PhotoImage(img3)

tk.Label(fr_catoption,text="---").pack()
tk.Label(fr_catoption,image=photo3).pack()
tk.Button(fr_catoption,text="---",
          command=lambda:show_frame(fr_dogoption)).pack()

#frame 4
img4=Image.open("placeholder.png")#image
img4=img4.resize((150,100))
photo4=ImageTk.PhotoImage(img4)

tk.Label(fr_dogoption,text="---").pack()
tk.Label(fr_dogoption,image=photo4).pack()
tk.Button(fr_dogoption,text="---",
          command=lambda:show_frame(fr_instructions)).pack()

show_frame(fr_instructions)
root.mainloop()
