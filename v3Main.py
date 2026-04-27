# the following program is a simple multichoice quiz to help you decide which breed of cat/dog to get
import v3Functions  # to access functions from the other file containing questions, breeds, and info
import sys  # sys.exit() to exit program
import tkinter as tk
from PIL import Image, ImageTk

animal = None
score = 0

root = tk.Tk()
root.title("Ideal Cat/Dog Breed Quiz")
root.geometry("1000x400")

# create frames
fr_instructions = tk.Frame(root)
fr_catordog = tk.Frame(root)
fr_catq1 = tk.Frame(root)
fr_catq2 = tk.Frame(root)
fr_catq3 = tk.Frame(root)
fr_dogq1=tk.Frame(root)
fr_dogq2=tk.Frame(root)
fr_dogq3=tk.Frame(root)
fr_result = tk.Frame(root)

# using for loop to bring forward frame 
for frame in (fr_instructions, fr_catordog, fr_catq1, fr_catq2, fr_catq3, fr_dogq1, fr_dogq2, fr_dogq3, fr_result):
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
            breed = v3Functions.catBreeds.get(score) 
            result=v3Functions.catResult(score)
            breed_img=v3Functions.catPhotos.get(breed)
        elif animal=="dog":
            breed = v3Functions.dogBreeds.get(score)
            result=v3Functions.dogResult(score)
            breed_img=v3Functions.dogPhotos.get(breed)
        else:
            result="Error: no animal selected. Please restart."
            breed_img="placeholder.png"
        image_breed = Image.open(breed_img)  # image
        image_breed.thumbnail((250,300))
        photobreed = ImageTk.PhotoImage(image_breed)
        label_result.config(text=result)#frame changes
        label_image.config(image=photobreed)
        label_image.image=photobreed
    except Exception as e:
        label_result.config(text=str(e))
    
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
    show_frame(fr_dogq1)

# frame 1 instructions
img1 = Image.open("placeholder.png")  # image
img1.thumbnail((350,200))
photo1 = ImageTk.PhotoImage(img1)

tk.Label(fr_instructions, padx=20, pady=20, 
         text="About this quiz:\nThe following program is a simple multi-choice quiz to help owners that have difficulty deciding which breed of cat/dog to get!\nThis quiz will find a breed that is suitable to your physical and behavioural preferences.\nPlease note that the questions asked are based on generalised breed traits and that individual pets may differ!\nAlso, please remember to research more about your suggested breed to ensure you are confident and know the correct requirements to meet its needs.").pack()
tk.Label(fr_instructions, image=photo1).pack()
tk.Button(fr_instructions, text="Questions", command=lambda: show_frame(fr_catordog)).pack()

# frame 2 cat or dog question
img2 = Image.open("catanddog.png")  # image
img2.thumbnail((350,200))
photo2 = ImageTk.PhotoImage(img2)

tk.Label(fr_catordog, justify="left", anchor="w", padx=20, pady=20, text='Do you want a cat or a dog?').pack()
tk.Label(fr_catordog, image=photo2).pack()
tk.Button(fr_catordog, text="Cat", command=choose_cat).pack()
tk.Button(fr_catordog, text="Dog", command=choose_dog).pack()
#----------------------------------------------------------------------------------------------------------------------
#CAT QUESTIONS
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
#----------------------------------------------------------------------------------------------------------------------
#DOG QUESTIONS
#frame 6 dog question 1
img6 = Image.open("placeholder.png")  # image
img6 = img6.resize((150, 100))
photo6 = ImageTk.PhotoImage(img6)

tk.Label(fr_dogq1, justify="left", anchor="w", padx=20, pady=20, 
         text="Would you prefer a friendly or more independent dog?\n\n಄ Friendly dogs may be very dependent and affectionate\n಄ Independent dogs may be more comfortable on their own and be more stubborn").pack()
tk.Label(fr_dogq1, image=photo6).pack()
tk.Button(fr_dogq1, text="Friendly", command=lambda: add_score(1, fr_dogq2)).pack()
tk.Button(fr_dogq1, text="Independent", command=lambda: add_score(2, fr_dogq2)).pack()

# frame 7 dog question 2
img7 = Image.open("placeholder.png")  # image
img7 = img7.resize((150, 100))
photo7 = ImageTk.PhotoImage(img7)

tk.Label(fr_dogq2, justify="left", anchor="w", padx=20, pady=20, 
         text="Would you prefer a smaller or larger dog?\n\n಄ Smaller dogs are better for smaller living spaces\n಄ Larger dogs are better for being active and protection").pack()
tk.Label(fr_dogq2, image=photo7).pack()
tk.Button(fr_dogq2, text="Smaller", command=lambda: add_score(4, fr_dogq3)).pack()
tk.Button(fr_dogq2, text="Larger", command=lambda: add_score(8, fr_dogq3)).pack()

# frame 8 dog question 3
img8 = Image.open("placeholder.png")  # image
img8 = img8.resize((150, 100))
photo8 = ImageTk.PhotoImage(img8)

tk.Label(fr_dogq3, justify="left", anchor="w", padx=20, pady=20, 
         text="Would you prefer a dog that sheds more but needs less grooming or a dog that sheds less but needs regular grooming?").pack()
tk.Label(fr_dogq3, image=photo5).pack()
tk.Button(fr_dogq3, text="More shedding, less grooming", command=lambda: add_score(16,fr_result)).pack()
tk.Button(fr_dogq3, text="Less shedding, regular grooming", command=lambda: add_score(32,fr_result)).pack()
#----------------------------------------------------------------------------------------------------------------------
#RESULTS
# frame 9 result
label_image = tk.Label(fr_result)
label_image.pack(pady=20,padx=20)

label_result = tk.Label(fr_result,text="Result")
label_result.pack()
tk.Button(fr_result, text="Restart?", command=reset_quiz).pack()

show_frame(fr_instructions)
root.mainloop()
