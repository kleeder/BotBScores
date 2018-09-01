import codecs
from tkinter import *
from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw()
filename = askopenfilename()

if filename:
    try:
        f = codecs.open(filename, 'r', encoding="utf8")
        title = "not found"
        score = 0.0
        i=0
        for x in f:
            titleR = re.search('title&gt;</span>(.+?) :: a BotB Battle', x)
            if titleR:
                title = "Major: "+titleR.group(1)
            titleR = re.search('BotB OHB :: (.+?)<span class="html-tag">', x)
            if titleR:
                title = "OHB: "+titleR.group(1)
            m = re.search('Sigma;<span class=\"html-tag\">&lt;/sub&gt;</span>(.+?)		&amp;', x)
            if m:
                score1 = score
                score = m.group(1)
                score = score1+float(score)

                i = i+1

        scoreDurch = score/i
        scoreDurch = round(scoreDurch,3)
        display = (title+"\n"+str(i)+" Entries"+"\n"+"Average Score: "+str(scoreDurch))
        root = Tk()
        root.minsize(width=250, height=100)
        root.iconbitmap('favicon.ico')
        root.title("BotB Average")
        frame = Frame(root)
        frame.pack()
        label = Label(frame, text=display)
        label.pack()
        quitButton = Button(frame, text="Oki ^o^", command=frame.quit)
        quitButton.pack()
        root.mainloop()

    except:
        print("Could not open file.")