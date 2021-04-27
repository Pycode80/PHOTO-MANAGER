"""
Made by Illies AKNAZZAY for the use of QWANDA
"""
from tkinter import *
import tkinter
from tkinter import filedialog
import glob, os
from PIL import Image,ImageTk
import tkinter.font as tkFont
from tkinter import ttk



window = Tk()
window.title("QWANDA PHOTO-MANAGER")
window.iconbitmap("ico.ico")
window.geometry("500x500")
window.config(bg="white")


helv36 = tkFont.Font(family='Helvetica', size=20, weight='bold')


fichier = open("size_data.txt", "w")
 
img_taille_s = PhotoImage(file = "taille_s.png")
img_taille_m = PhotoImage(file = "taille_m.png")
img_taille_l = PhotoImage(file = "taille_l.png")
img_taille_xl = PhotoImage(file = "taille_xl.png") 


def start():
    def taille_s():
        b.pack(expand=YES)
        frame.forget()
        choisir.forget()
        fichier = open("size_data.txt", "w")
        fichier.write("1")
        fichier.close()
    def taille_m():
        b.pack(expand=YES)
        frame.forget()
        choisir.forget()
        fichier = open("size_data.txt", "w")
        fichier.write("2")
        fichier.close()
    def taille_l():
        b.pack(expand=YES)
        frame.forget()
        choisir.forget()
        fichier = open("size_data.txt", "w")
        fichier.write("3")
        fichier.close()
    def taille_xl():
        b.pack(expand=YES)
        frame.forget()
        choisir.forget()
        fichier = open("size_data.txt", "w")
        fichier.write("4")
        fichier.close()
    
    def select():
        taille = open("size_data.txt", "r").read()
        folder =  tkinter.filedialog.askdirectory(title='Choose a directory')
        os.chdir(folder)
        os.mkdir('Compress')
        for file in glob.glob("*.png"):
            if taille == "1":
                size = 200,200
                im = Image.open(file)
                im.thumbnail(size, Image.ANTIALIAS)
                im.save('Compress/'+file , im.format)

            if taille == "2":
                size = 300,300
                im = Image.open(file)
                im.thumbnail(size, Image.ANTIALIAS)
                im.save('Compress/'+file , im.format)

            if taille == "3":
                size = 500,500
                im = Image.open(file)
                im.thumbnail(size, Image.ANTIALIAS)
                im.save('Compress/'+file , im.format)

            if taille == "4":
                size = 1000,1000
                im = Image.open(file)
                im.thumbnail(size, Image.ANTIALIAS)
                im.save('Compress/'+file , im.format)



            
        for file in glob.glob("*.jpg"):
            if taille == "1":
                size = 200,200
                im = Image.open(file)
                im.thumbnail(size, Image.ANTIALIAS)
                im = im.rotate(180, expand = 1)
                im.save('Compress/'+file , im.format)

            if taille == "2":
                size = 300,300
                im = Image.open(file)
                im.thumbnail(size, Image.ANTIALIAS)
                im = im.rotate(180, expand = 1)
                im.save('Compress/'+file , im.format)

            if taille == "3":
                size = 500,500
                im = Image.open(file)
                im.thumbnail(size, Image.ANTIALIAS)
                im = im.rotate(180, expand = 1)
                im.save('Compress/'+file , im.format)

            if taille == "4":
                size = 1000,1000
                im = Image.open(file)
                im.thumbnail(size, Image.ANTIALIAS)
                im = im.rotate(180, expand = 1)
                im.save('Compress/'+file , im.format)


                
        for file in glob.glob("*.jpeg"):
            if taille == "1":
                size = 200,200
                im = Image.open(file)
                im.thumbnail(size, Image.ANTIALIAS)
                im.save('Compress/'+file , im.format)

            if taille == "2":
                size = 300,300
                im = Image.open(file)
                im.thumbnail(size, Image.ANTIALIAS)
                im.save('Compress/'+file , im.format)

            if taille == "3":
                size = 500,500
                im = Image.open(file)
                im.thumbnail(size, Image.ANTIALIAS)
                im.save('Compress/'+file , im.format)

            if taille == "4":
                size = 1000,1000
                im = Image.open(file)
                im.thumbnail(size, Image.ANTIALIAS)
                im.save('Compress/'+file , im.format)


            
        for c in window.winfo_children():
            c.destroy()
        frame = Frame(window)
        frame.config(bg="white")
        frame.pack(expand=YES)
        fini = Label(frame, text="Finished image compression", bg="white")
        e = Entry(frame, width=40, bg="white")
        e.delete(0,END)
        e.insert(0, folder + '/Compress/')
        fini.grid(column=0,row=0)
        e.grid(column=1,row=0)
        restart = Button(frame, text="RESTART ?", command=start, bg="blue", fg="white")
        quitter = Button(frame, text="EXIT ?", command=quit, bg="blue", fg="white")
        restart.grid(column=0,row=1)
        quitter.grid(column=1,row=1)

        
    for c in window.winfo_children():
        c.destroy()        
    b = Button(window, text="SELECT A DIRECTORY", command=select, font=helv36, bg="blue", fg="white")


            
    
    l = Label(window, text="MADE BY ILLIES AKNAZZAY FOR QWANDA", bg="white")
    l.pack(side=LEFT and BOTTOM)
    choisir = Label(window , text="Choose your level of compress", font=helv36, bg="white")
    choisir.pack(expand=YES)
    frame = Frame(window)
    frame.config(bg="white")
    frame.pack(expand=YES)
    taille_s = Button(frame ,image=img_taille_s,bg="white", relief="groove", command=taille_s)
    taille_m = Button(frame,image=img_taille_m,bg="white", relief="groove", command=taille_m)
    taille_l = Button(frame, image=img_taille_l,bg="white", relief="groove", command=taille_l)
    taille_xl = Button(frame ,image=img_taille_xl,bg="white", relief="groove", command=taille_xl)
    
    taille_s.grid(column=0,row=1)
    taille_m.grid(column=1,row=1)
    taille_l.grid(column=2,row=1)
    taille_xl.grid(column=3,row=1)


    
start()
window.mainloop()
