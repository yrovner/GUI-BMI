# Import Module
from tkinter import *
from tkinter import messagebox
import customtkinter
from PIL import ImageTk, Image
import pywinstyles


#Erstellen des CTk-Fensters, Titel , Maße & Geometry(widthxheight)
root = customtkinter.CTk()
root.title("BMI-Rechner")
root.geometry(f"600x800")
root.resizable(False,False)
customtkinter.set_default_color_theme("green")

#Funktion-BMI

def calculate_bmi():
    try:
        height = float(height_entry.get())
        weight = float(weight_entry.get())
        if variable2.get() == "ft":
            height *= 30.48
        if variable1.get() == "ibs":
            weight *= 0.453592
        bmi = weight / ((height/100) ** 2)
        result_label.configure(text="Dein BMI ist {:.1f}".format(bmi))
    except ValueError:
        messagebox.showerror("Error", "Bitte gib eine valide Nummer ein!")
    except ZeroDivisionError:
        messagebox.showerror("Error", "Die Größe kann nicht 0 sein!")

    if bmi < 17.5:
        gewicht_label.configure(text="Du bist untergewichtig :(")
        
    elif bmi >=17.5 and bmi < 25:
        gewicht_label.configure(text="Du bist im Normalgewicht :-)")
        
    elif bmi >=25 and bmi < 29:
        gewicht_label.configure(text="Du bist übergewichtig ")
        
    elif bmi >=29 and bmi < 34:
        gewicht_label.configure(text="Du hast starkes Übergewicht")
        
    elif bmi >=34:
        gewicht_label.configure(text="Wtf Adipositas")
        
    
    
 
#Hintergrundbild

img1=ImageTk.PhotoImage(Image.open("PurpleWave.jpg"))
Label1=customtkinter.CTkLabel(master=root, text="", image=img1, width=1440, height=2960)
Label1.pack()

#Frame

frame = customtkinter.CTkFrame(master=root,
                               width=400,
                               height=400,
                               corner_radius=50,
                               bg_color="#000001")

frame.place(relx=0.5, rely=0.5, anchor=CENTER)

#Opacity/Transparency of frame

pywinstyles.set_opacity(frame, value=0.6, color="#000001")

#Fonts

font1 = ("Arial",30,"bold")
font2 = ("Arial",25,"bold")
font3 = ("Arial",25,"bold")

#Titel

title_label = customtkinter.CTkLabel(root, font=font1,
                                     text="BMI-Rechner",
                                     text_color="white",
                                     bg_color="#000001",
                                     corner_radius=50)

pywinstyles.set_opacity(title_label, value=0.9, color="#000001")
title_label.place(x=200, y=220)

#Gewicht

weight_label = customtkinter.CTkLabel(root, font=font2,
                                     text="Gewicht",
                                     text_color="white",
                                     bg_color="#000001",
                                     corner_radius=50)

pywinstyles.set_opacity(weight_label, value=0.9, color="#000001")
weight_label.place(x=110, y=290)


#Hoehe

height_label = customtkinter.CTkLabel(root,font=font2,
                                      text="Höhe",
                                      text_color="white",
                                      bg_color="#000001",
                                      corner_radius=50)

pywinstyles.set_opacity(height_label, value=0.9, color="#000001")
height_label.place(x=110, y=400)
                                    

#Eingabefeld Gewicht


weight_entry = customtkinter.CTkEntry(root, font=font2,
                                      text_color="#49bf7a",
                                      fg_color="white",
                                      bg_color="#000001")

pywinstyles.set_opacity(weight_entry, value=0.9, color="#000001")

weight_entry.place(x=240, y=290)


#Eingabefeld Höhe

height_entry = customtkinter.CTkEntry(root, font=font2,
                                      text_color="#49bf7a",
                                      fg_color="white",
                                      bg_color="#000001")

pywinstyles.set_opacity(height_entry, value=0.9, color="#000001")

height_entry.place(x=240, y=400)


#GewichtOptionen

weight_options = ["kg", "ibs"]
height_options = ["cm", "ft"]
variable1 = StringVar()
variable2 = StringVar()
                                      
weight_option = customtkinter.CTkComboBox(root, font=font2,
                                          text_color="#49bf7a",
                                          bg_color="#000001",
                                          fg_color="white",
                                          dropdown_hover_color="#000001",
                                          values=weight_options,
                                          variable=variable1,
                                          width=80)

weight_option.place(x=400, y=290)
weight_option.set("kg")

pywinstyles.set_opacity(weight_option, value=0.9, color="#000001")

#HoeheOptionen

height_option = customtkinter.CTkComboBox(root, font=font2,
                                          text_color="#49bf7a",
                                          bg_color="#000001",
                                          fg_color="white",
                                          dropdown_hover_color="#000001",
                                          values=height_options,
                                          variable=variable2,
                                          width=80)

height_option.place(x=400, y=400)
height_option.set("cm")

pywinstyles.set_opacity(height_option, value=0.9, color="#000001")


#Button

calculate_button = customtkinter.CTkButton(root,
                                           font=font2,command=calculate_bmi,
                                           text_color="White",
                                           text="BMI berechnen",
                                           hover_color="#ab49bf",
                                           bg_color="#000001",
                                           cursor='hand2',
                                           corner_radius=5,
                                           width=200)
calculate_button.place(x=200, y=500)

pywinstyles.set_opacity(calculate_button, value=0.9, color="#000001")



#Ergebnis Label

result_label = customtkinter.CTkLabel(root, text="",
                                      font=font3,
                                      text_color="white",
                                      bg_color="#000001")


result_label.place(x=200, y=650)

pywinstyles.set_opacity(result_label, value=0.9, color="#000001")

#Normalgewicht/Übergewicht/Stark übergewichtig

gewicht_label = customtkinter.CTkLabel(root, text="",
                                       font=font3,
                                       text_color="white",
                                      bg_color="#000001")

gewicht_label.place(x=300, y=700, anchor=CENTER)

pywinstyles.set_opacity(gewicht_label, value=0.9, color="#000001")



                                           

#Execute Tkinter

root.mainloop()

