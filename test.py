from tkinter import *
from PIL import Image, ImageTk
import csv
import os
okno = Tk()
okno.attributes('-fullscreen', True)
obrazok = Image.open("img/pozadie.jpg")
pozadie = ImageTk.PhotoImage(obrazok)
label=Label(okno, image=pozadie)
label.place(x=0, y=0, relwidth=1, relheight=1)

nadpis=Label(okno, text="City Quiz", font=("Arial", 50, "bold"), bg="#59c2e5", fg="#000000",)
nadpis.pack(pady=50)

meno_label=Label(okno, text="Meno: ", font=("Arial", 20), bg="#59c2e5", fg="#000000")
meno_label.pack(pady=10)
meno_entry=Entry(okno, font=("Arial", 20), bg="#ffffff", fg="#000000")
meno_entry.pack(pady=10)

vek_label=Label(okno, text="Vek: ", font=("Arial", 20), bg="#59c2e5", fg="#000000")
vek_label.pack(pady=10)
vek_entry=Entry(okno, font=("Arial", 20), bg="#ffffff", fg="#000000")
vek_entry.pack(pady=10)

mesto_label=Label(okno, text="Mesto: ", font=("Arial", 20), bg="#59c2e5", fg="#000000")
mesto_label.pack(pady=10)
mesto_entry=Entry(okno, font=("Arial", 20), bg="#ffffff", fg="#000000")
mesto_entry.pack(pady=10)


exit_button=Image.open("img/exit.png")
exit_button=ImageTk.PhotoImage(exit_button)
exit__button = Button(okno, image=exit_button, command=okno.destroy,bg="#87CEEB", borderwidth=0, highlightthickness=0,)
exit__button.place(relx=1.0, x=-10, y=10, anchor=NE)

body=0
meno=""
vek=""
mesto=""

def bod():
    global body
    body +=1


def potvrd_meno():
    global meno, vek, mesto
    meno=meno_entry.get()
    vek=vek_entry.get()
    mesto=mesto_entry.get()
    nadpis.destroy()
    meno_label.destroy()
    meno_entry.destroy()
    vek_label.destroy()
    vek_entry.destroy()
    mesto_label.destroy()
    mesto_entry.destroy()
    submit_button.destroy()
    priprava() 

def priprava():

    nadpis1=Label(okno, text="City Quiz", font=("Arial", 50, "bold"), bg="#59c2e5", fg="#000000",)
    nadpis1.pack(pady=50)

    ready=Label(okno, text=f"Ahoj ! Si pripravený uhádnuť všetky hlavné mestá?", font=("Arial", 30,), bg="#59c2e5", fg="#000000",)
    ready.pack(pady=100)

    frame=Frame(okno, bg="#59c2e5")
    frame.pack(pady=50)
    
    ano_button=Button(frame, text="    Ano    ", font=("Arial", 30), bg="#ffffff", fg="#000000", 
                      command=lambda: [frame.destroy(), ready.destroy(), otazka_1()])
    ano_button.pack(pady=50, padx=50, side=LEFT)
    nie_button=Button(frame, text="    Nie   ", font=("Arial", 30), bg="#ffffff", fg="#000000", command=okno.destroy)
    nie_button.pack(pady=50, padx=50, side=LEFT)

def otazka_1():
    nadpis2=Label(okno, text="Aké je hlavné mesto Austrálie?", font=("Arial", 30,), bg="#59c2e5", fg="#000000",)
    nadpis2.pack(pady=30)
    frame1=Frame(okno, bg="#59c2e5")
    frame1.pack(pady=50)
    A_button=Button(frame1, text="Sydney", font=("Arial", 30), bg="#ffffff", fg="#000000", command=lambda: [frame1.destroy(), nadpis2.destroy(), otazka_2(),])
    A_button.pack(pady=50, padx=50, side=LEFT)
    B_button=Button(frame1, text="Melbourne", font=("Arial", 30), bg="#ffffff", fg="#000000", command=lambda: [frame1.destroy(), nadpis2.destroy(), otazka_2()])
    B_button.pack(pady=50, padx=50, side=LEFT)
    C_button=Button(frame1, text="Canberra", font=("Arial", 30), bg="#ffffff", fg="#000000", command=lambda: [frame1.destroy(), nadpis2.destroy(), otazka_2(), bod(),])
    C_button.pack(pady=50, padx=50, side=LEFT)
    D_button=Button(frame1, text="Denpassar", font=("Arial", 30), bg="#ffffff", fg="#000000", command=lambda: [frame1.destroy(), nadpis2.destroy(), otazka_2()])
    D_button.pack(pady=50, padx=50, side=LEFT)


def otazka_2():
    nadpis3=Label(okno, text="Aké je hlavné mesto Českej reoubliky?", font=("Arial", 30,), bg="#59c2e5", fg="#000000",)
    nadpis3.pack(pady=30)
    frame2=Frame(okno, bg="#59c2e5")
    frame2.pack(pady=50)
    A_button=Button(frame2, text="Praha", font=("Arial", 30), bg="#ffffff", fg="#000000", command=lambda: [frame2.destroy(), nadpis3.destroy(), otazka_3(), bod(),])
    A_button.pack(pady=50, padx=50, side=LEFT)
    B_button=Button(frame2, text="Brno", font=("Arial", 30), bg="#ffffff", fg="#000000", command=lambda: [frame2.destroy(), nadpis3.destroy(), otazka_3(),])
    B_button.pack(pady=50, padx=50, side=LEFT)
    C_button=Button(frame2, text="Plzeň", font=("Arial", 30), bg="#ffffff", fg="#000000", command=lambda: [frame2.destroy(), nadpis3.destroy(), otazka_3(),])
    C_button.pack(pady=50, padx=50, side=LEFT)
    D_button=Button(frame2, text="Drážďany", font=("Arial", 30), bg="#ffffff", fg="#000000", command=lambda: [frame2.destroy(), nadpis3.destroy(), otazka_3(),])
    D_button.pack(pady=50, padx=50, side=LEFT)

def otazka_3():
    nadpis4=Label(okno, text="Aké je hlavné mesto Slovenskej reoubliky?", font=("Arial", 30,), bg="#59c2e5", fg="#000000",)
    nadpis4.pack(pady=30)
    frame3=Frame(okno, bg="#59c2e5")
    frame3.pack(pady=50)
    A_button=Button(frame3, text="Praha", font=("Arial", 30), bg="#ffffff", fg="#000000", command=lambda: [frame3.destroy(), nadpis4.destroy(), otazka_4(),])
    A_button.pack(pady=50, padx=50, side=LEFT)
    B_button=Button(frame3, text="Bratislava", font=("Arial", 30), bg="#ffffff", fg="#000000", command=lambda: [frame3.destroy(), nadpis4.destroy(), otazka_4(), bod(),])
    B_button.pack(pady=50, padx=50, side=LEFT)
    C_button=Button(frame3, text="Košice", font=("Arial", 30), bg="#ffffff", fg="#000000", command=lambda: [frame3.destroy(), nadpis4.destroy(), otazka_4(),])
    C_button.pack(pady=50, padx=50, side=LEFT)
    D_button=Button(frame3, text="Banská bystrica", font=("Arial", 30), bg="#ffffff", fg="#000000", command=lambda: [frame3.destroy(), nadpis4.destroy(), otazka_4(),])
    D_button.pack(pady=50, padx=50, side=LEFT)

def otazka_4():
    nadpis5=Label(okno, text="Aké je hlavné mesto Talianska?", font=("Arial", 30,), bg="#59c2e5", fg="#000000",)
    nadpis5.pack(pady=30)
    frame4=Frame(okno, bg="#59c2e5")
    frame4.pack(pady=50)
    A_button=Button(frame4, text="Neapol", font=("Arial", 30), bg="#ffffff", fg="#000000", command=lambda: [frame4.destroy(), nadpis5.destroy(), otazka_5(),])
    A_button.pack(pady=50, padx=50, side=LEFT)
    B_button=Button(frame4, text="Rím", font=("Arial", 30), bg="#ffffff", fg="#000000", command=lambda: [frame4.destroy(), nadpis5.destroy(), otazka_5(), bod(),])
    B_button.pack(pady=50, padx=50, side=LEFT)
    C_button=Button(frame4, text="Benátky", font=("Arial", 30), bg="#ffffff", fg="#000000", command=lambda: [frame4.destroy(), nadpis5.destroy(), otazka_5(),])
    C_button.pack(pady=50, padx=50, side=LEFT)
    D_button=Button(frame4, text="Palermo", font=("Arial", 30), bg="#ffffff", fg="#000000", command=lambda: [frame4.destroy(), nadpis5.destroy(), otazka_5(),])
    D_button.pack(pady=50, padx=50, side=LEFT)

def otazka_5():
    nadpis6=Label(okno, text="Aké je hlavné mesto Mexika?", font=("Arial", 30,), bg="#59c2e5", fg="#000000",)
    nadpis6.pack(pady=30)
    frame5=Frame(okno, bg="#59c2e5")
    frame5.pack(pady=50)
    A_button=Button(frame5, text="Mexiko city", font=("Arial", 30), bg="#ffffff", fg="#000000", command=lambda: [frame5.destroy(), nadpis6.destroy(), otazka_6(), bod(),])
    A_button.pack(pady=50, padx=50, side=LEFT)
    B_button=Button(frame5, text="Guadalachara", font=("Arial", 30), bg="#ffffff", fg="#000000", command=lambda: [frame5.destroy(), nadpis6.destroy(), otazka_6(),])
    B_button.pack(pady=50, padx=50, side=LEFT)
    C_button=Button(frame5, text="Rio de Janeiro", font=("Arial", 30), bg="#ffffff", fg="#000000", command=lambda: [frame5.destroy(), nadpis6.destroy(), otazka_6(),])
    C_button.pack(pady=50, padx=50, side=LEFT)
    D_button=Button(frame5, text="Sinaloa", font=("Arial", 30), bg="#ffffff", fg="#000000", command=lambda: [frame5.destroy(), nadpis6.destroy(), otazka_6(),])
    D_button.pack(pady=50, padx=50, side=LEFT)

def otazka_6():
    nadpis7=Label(okno, text="Aké je hlavné mesto Uzbekistanu?", font=("Arial", 30,), bg="#59c2e5", fg="#000000",)
    nadpis7.pack(pady=30)
    frame6=Frame(okno, bg="#59c2e5")
    frame6.pack(pady=50)
    A_button=Button(frame6, text="Teherán", font=("Arial", 30), bg="#ffffff", fg="#000000", command=lambda: [frame6.destroy(), nadpis7.destroy(), otazka_7(),])
    A_button.pack(pady=50, padx=50, side=LEFT)
    B_button=Button(frame6, text="Bagdad", font=("Arial", 30), bg="#ffffff", fg="#000000", command=lambda: [frame6.destroy(), nadpis7.destroy(), otazka_7(),])
    B_button.pack(pady=50, padx=50, side=LEFT)
    C_button=Button(frame6, text="Taraz", font=("Arial", 30), bg="#ffffff", fg="#000000", command=lambda: [frame6.destroy(), nadpis7.destroy(), otazka_7(),])
    C_button.pack(pady=50, padx=50, side=LEFT)
    D_button=Button(frame6, text="Taškent", font=("Arial", 30), bg="#ffffff", fg="#000000", command=lambda: [frame6.destroy(), nadpis7.destroy(), otazka_7(), bod(),])
    D_button.pack(pady=50, padx=50, side=LEFT)

def otazka_7():
    nadpis8=Label(okno, text="Aké je hlavné mesto Turecka?", font=("Arial", 30,), bg="#59c2e5", fg="#000000",)
    nadpis8.pack(pady=30)
    frame7=Frame(okno, bg="#59c2e5")
    frame7.pack(pady=50)
    A_button=Button(frame7, text="Antalya", font=("Arial", 30), bg="#ffffff", fg="#000000", command=lambda: [frame7.destroy(), nadpis8.destroy(), otazka_8(),])
    A_button.pack(pady=50, padx=50, side=LEFT)
    B_button=Button(frame7, text="Ankara", font=("Arial", 30), bg="#ffffff", fg="#000000", command=lambda: [frame7.destroy(), nadpis8.destroy(), otazka_8(), bod(),])
    B_button.pack(pady=50, padx=50, side=LEFT)
    C_button=Button(frame7, text="Side", font=("Arial", 30), bg="#ffffff", fg="#000000", command=lambda: [frame7.destroy(), nadpis8.destroy(), otazka_8(),])
    C_button.pack(pady=50, padx=50, side=LEFT)
    D_button=Button(frame7, text="Istanbul", font=("Arial", 30), bg="#ffffff", fg="#000000", command=lambda: [frame7.destroy(), nadpis8.destroy(), otazka_8(),])
    D_button.pack(pady=50, padx=50, side=LEFT)

def otazka_8():
    nadpis9=Label(okno, text="Aké je hlavné mesto Japonska?", font=("Arial", 30,), bg="#59c2e5", fg="#000000",)
    nadpis9.pack(pady=30)
    frame8=Frame(okno, bg="#59c2e5")
    frame8.pack(pady=50)
    A_button=Button(frame8, text="Tokio", font=("Arial", 30), bg="#ffffff", fg="#000000", command=lambda: [frame8.destroy(), nadpis9.destroy(), otazka_9(), bod(),])
    A_button.pack(pady=50, padx=50, side=LEFT)
    B_button=Button(frame8, text="Kjoto", font=("Arial", 30), bg="#ffffff", fg="#000000", command=lambda: [frame8.destroy(), nadpis9.destroy(), otazka_9(),])
    B_button.pack(pady=50, padx=50, side=LEFT)
    C_button=Button(frame8, text="Osaka", font=("Arial", 30), bg="#ffffff", fg="#000000", command=lambda: [frame8.destroy(), nadpis9.destroy(), otazka_9(),])
    C_button.pack(pady=50, padx=50, side=LEFT)
    D_button=Button(frame8, text="Fukušima", font=("Arial", 30), bg="#ffffff", fg="#000000", command=lambda: [frame8.destroy(), nadpis9.destroy(), otazka_9(),])
    D_button.pack(pady=50, padx=50, side=LEFT)

def otazka_9():
    nadpis10=Label(okno, text="Aké je hlavné mesto Španielska?", font=("Arial", 30,), bg="#59c2e5", fg="#000000",)
    nadpis10.pack(pady=30)
    frame9=Frame(okno, bg="#59c2e5")
    frame9.pack(pady=50)
    A_button=Button(frame9, text="Barcelona", font=("Arial", 30), bg="#ffffff", fg="#000000", command=lambda: [frame9.destroy(), nadpis10.destroy(), otazka_10(),])
    A_button.pack(pady=50, padx=50, side=LEFT)
    B_button=Button(frame9, text="Valencia", font=("Arial", 30), bg="#ffffff", fg="#000000", command=lambda: [frame9.destroy(), nadpis10.destroy(), otazka_10(),])
    B_button.pack(pady=50, padx=50, side=LEFT)
    C_button=Button(frame9, text="Malaga", font=("Arial", 30), bg="#ffffff", fg="#000000", command=lambda: [frame9.destroy(), nadpis10.destroy(), otazka_10(),])
    C_button.pack(pady=50, padx=50, side=LEFT)
    D_button=Button(frame9, text="Madrid", font=("Arial", 30), bg="#ffffff", fg="#000000", command=lambda: [bod(), frame9.destroy(), nadpis10.destroy(), otazka_10(),])
    D_button.pack(pady=50, padx=50, side=LEFT)

def otazka_10():
    nadpis11=Label(okno, text="Aké je hlavné mesto Kanady?", font=("Arial", 30,), bg="#59c2e5", fg="#000000",)
    nadpis11.pack(pady=30)
    frame10=Frame(okno, bg="#59c2e5")
    frame10.pack(pady=50)
    A_button=Button(frame10, text="Toronto", font=("Arial", 30), bg="#ffffff", fg="#000000", command=lambda: [frame10.destroy(), nadpis11.destroy(), hodnotenie(),])
    A_button.pack(pady=50, padx=50, side=LEFT)
    B_button=Button(frame10, text="Ottawa", font=("Arial", 30), bg="#ffffff", fg="#000000", command=lambda: [bod(), frame10.destroy(), nadpis11.destroy(), hodnotenie(),])
    B_button.pack(pady=50, padx=50, side=LEFT)
    C_button=Button(frame10, text="Vencouver", font=("Arial", 30), bg="#ffffff", fg="#000000", command=lambda: [frame10.destroy(), nadpis11.destroy(), hodnotenie(),])
    C_button.pack(pady=50, padx=50, side=LEFT)
    D_button=Button(frame10, text="Edmonton", font=("Arial", 30), bg="#ffffff", fg="#000000", command=lambda: [frame10.destroy(), nadpis11.destroy(), hodnotenie(),])
    D_button.pack(pady=50, padx=50, side=LEFT)

def vysledok():
    with open('vysledky.csv', mode='a', newline='', encoding='utf-8') as file:
     writer = csv.writer(file)
     writer.writerow([meno, vek, mesto, body])
     print("zapisane")



def hodnotenie():
    nadpis12=Label(okno, text=f"Gratulujem! Získal si {body} bodov", font=("Arial", 30,), bg="#59c2e5", fg="#000000",)
    nadpis12.pack(pady=30)
    frame11=Frame(okno, bg="#59c2e5")
    frame11.pack(pady=50)
    quit_button=Button(frame11, text="Koniec", font=("Arial", 30), bg="#ffffff", fg="#000000", command=lambda: [okno.destroy(), vysledok(), ])
    quit_button.pack(pady=150, padx=200, side=LEFT)

submit_button=Button(okno, text="Submit", font=("Arial", 20), command=potvrd_meno)
submit_button.pack(pady=10)
okno.mainloop()

