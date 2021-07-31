from tkinter import *
import random
# import tkinter.messagebox as tmsg
import pyttsx3

# This list is collection of correct words
answers = [
    "python",
    "java",
    "swift",
    "canada",
    "india",
    "america",
    "london",
    "patna",
    "bihar",
    "pen",
    "laptop"
]
# This list is collection of garbagee word
words = [
    "nptoyh",
    "avja",
    "wfsit",
    "cdanaa",
    "aidin",
    "aiearcm",
    "odnlon",
    "tapan",
    "ihabr",
    "enp",
    "ptpalo "
]

num = random.randrange(0, len(words), 1)
score = 0


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Function for speak text


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# This Funtion is runs when the answer is corerct


def speakScore(gameScore):
    speak(f"Well Done Your Score is {gameScore}")

# This Funtion is runs when the answer is wrong


def speakWrongAnswer():
    speak("Wrong Answer try again")

# This Function is for dispaly the words


def defaultWord():
    global words, num
    lbl.config(text=words[num])


def resetWord():
    global words, answers, num, score
    num = random.randrange(0, len(words), 1)
    lbl.config(text=words[num])
    e1.delete(0, END)


def checkAnswer():
    global words, answers, num, score
    var = e1.get()
    if var == answers[num]:
        score = score + 1
        speakScore(score)
        # tmsg.showinfo("Success", "This is a correct answer")
        resetWord()
    else:
        # tmsg.showerror("Error", "This is not Correct")
        speakWrongAnswer()
        e1.delete(0, END)


def checkScore():
    global words, answers, num, score
    top = Toplevel()
    top.title("Score")
    top.geometry("250x300")
    top.config(bg="#E71C23")
    lbl = Label(top, text="Your Score", font="Verdana 18", bg="#E71C23")
    lbl.pack(pady=50)

    Label(top, text=(f'{score}'),
          bg="#E71C23", font="Verdana 16").pack()
    top.mainloop()


root = Tk()
root.geometry("444x600+400+100")
root.title("Jumbled")
root.config(bg="#000000")


lbl = Label(root, text="Your Text Here",
            font="Verdana 18", bg="#000000", fg="#FFFFFF")
lbl.pack(pady=30)


ans1 = StringVar()
e1 = Entry(root, font="Verdana 16", textvariable=ans1)
e1.pack()

btncheck = Button(root, text="Check", activebackground="Red", font="comicsansms 16",
                  width=16, bg="Black", fg="#6ab04c", relief=SUNKEN, command=checkAnswer)
btncheck.pack(pady=10)


btnreset = Button(root, text="Reset", font="comicsansms 16",
                  width=16, bg="Black", fg="#E71C23", relief=SUNKEN, command=resetWord)
btnreset.pack(pady=10)

scorecheck = Button(root, text="Score", font="comicsansms 16", width=16,
                    bg="Black", fg="#10A881", relief=SUNKEN, command=checkScore)
scorecheck.pack(pady=10)

endgame = Button(root, text="Quite Game", font="comicsansms 16",
                 width=16, bg="Black", fg="#F3B431", relief=SUNKEN, command=quit)
endgame.pack()

defaultWord()
root.mainloop()
