import v3Functions  # to access functions from the other file containing questions, breeds, and info
import sys  # sys.exit() to exit program
import tkinter as tk
from PIL import Image, ImageTk

animal = None
score = 0

root = tk.Tk()
root.title("Ideal Cat/Dog Breed Quiz")
root.geometry("1000x700")

# create frames
fr_instructions = tk.Frame(root)
fr_catordog = tk.Frame(root)
fr_catq1 = tk.Frame(root)
fr_catq2 = tk.Frame(root)
fr_catq3 = tk.Frame(root)
fr_result = tk.Frame(root)

# using for loop to bring forward frame 
for frame in (fr_instructions, fr_catordog, fr_catq1, fr_catq2, fr_catq3, fr_result):
    frame.place(relwidth=1, relheight=1)

def show_frame(frame):
    frame.tkraise()

def add_score(value, nextframe):
    global score
    score += value
    show_frame(nextframe)
    if nextframe==fr_result:
        show_result()

def reset_quiz():
    global score,animal
    score=0
    animal=None
    show_frame(fr_catordog)

def show_result():
    global animal,score
    try:
        if animal=="cat":
            result=v3Functions.catResult(score)
        elif animal=="dog":
            result=v3Functions.dogResult(score)
        else:
            result="Error: no animal selected. Please restart."
    except:
        result="Error: Could not get result. Please check v3Functions file."
    
    label_result.config(text=result)
    show_frame(fr_result)

def choose_cat():
    global animal,score
    animal="cat"
    score=0
    show_frame(fr_catq1)

def choose_dog():
    global animal,score
    animal="dog"
    score=0
    show_frame(fr_catq1)

# frame 1 instructions
img1 = Image.open("placeholder.png")  # image
img1 = img1.resize((250, 250))
photo1 = ImageTk.PhotoImage(img1)

tk.Label(fr_instructions, justify="left", anchor="w", padx=20, pady=20, 
         text="About this quiz:\nThe following program is a simple multi-choice quiz to help owners that have difficulty deciding which breed of cat/dog to get!\nThis quiz will find a breed that is suitable to your physical and behavioural preferences.\nPlease note that the questions asked are based on generalised breed traits and that individual pets may differ!\nAlso, please remember to research more about your suggested breed to ensure you are confident and know the correct requirements to meet its needs.").pack()
tk.Label(fr_instructions, image=photo1).pack()
tk.Button(fr_instructions, text="Questions", command=lambda: show_frame(fr_catordog)).pack()

# frame 2 cat or dog question
img2 = Image.open("placeholder.png")  # image
img2 = img2.resize((250, 150))
photo2 = ImageTk.PhotoImage(img2)

tk.Label(fr_catordog, justify="left", anchor="w", padx=20, pady=20, text='Do you want a cat or a dog?').pack()
tk.Label(fr_catordog, image=photo2).pack()
tk.Button(fr_catordog, text="Cat", command=choose_cat).pack()
tk.Button(fr_catordog, text="Dog", command=choose_dog).pack()

# frame 3 cat question 1
img3 = Image.open("placeholder.png")  # image
img3 = img3.resize((150, 100))
photo3 = ImageTk.PhotoImage(img3)

tk.Label(fr_catq1, justify="left", anchor="w", padx=20, pady=20, 
         text="Would you prefer a more mellow or active cat?\n\n಄ Mellow cats are more relaxed\n಄ Active cats are more energetic and playful").pack()
tk.Label(fr_catq1, image=photo3).pack()
tk.Button(fr_catq1, text="Mellow", command=lambda: add_score(1, fr_catq2)).pack()
tk.Button(fr_catq1, text="Active", command=lambda: add_score(2, fr_catq2)).pack()

# frame 4 cat question 2
img4 = Image.open("placeholder.png")  # image
img4 = img4.resize((150, 100))
photo4 = ImageTk.PhotoImage(img4)

tk.Label(fr_catq2, justify="left", anchor="w", padx=20, pady=20, 
         text="Would you prefer a vocal or less vocal cat?\n\n಄ Vocal cats are more loud and expressive\n಄ Less vocal cats are more quiet and less communicative").pack()
tk.Label(fr_catq2, image=photo4).pack()
tk.Button(fr_catq2, text="Vocal", command=lambda: add_score(4, fr_catq3)).pack()
tk.Button(fr_catq2, text="Less Vocal", command=lambda: add_score(8, fr_catq3)).pack()

# frame 5 cat question 3
img5 = Image.open("placeholder.png")  # image
img5 = img5.resize((150, 100))
photo5 = ImageTk.PhotoImage(img5)

tk.Label(fr_catq3, justify="left", anchor="w", padx=20, pady=20, 
         text="Would you prefer a cat with lower maintenance short hair or higher maintenance long hair?\n\n಄ Short-haired cats tend to be sleek and need less brushing\n಄ Long-haired cats tend to be more fluffy and need more brushing").pack()
tk.Label(fr_catq3, image=photo5).pack()
tk.Button(fr_catq3, text="Short hair", command=lambda: add_score(16,fr_result)).pack()
tk.Button(fr_catq3, text="Long hair", command=lambda: add_score(32,fr_result)).pack()

# frame 6 result
label_result = tk.Label(fr_result,text="Result")
label_result.pack()
tk.Button(fr_result, text="Restart?", command=reset_quiz).pack()

show_frame(fr_instructions)
root.mainloop()
