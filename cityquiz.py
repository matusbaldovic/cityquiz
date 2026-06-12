from tkinter import *
from PIL import Image, ImageTk
import csv

#window
window = Tk()
window.attributes('-fullscreen', True)
image = Image.open("img/pozadie.jpg")
background = ImageTk.PhotoImage(image)
label=Label(window, image=background)
label.place(x=0, y=0, relwidth=1, relheight=1)

#first page
h=Label(window, text="City Quiz", font=("Arial", 50, "bold"), bg="#59c2e5", fg="#000000",)
h.pack(pady=50)

name_label=Label(window, text="Meno: ", font=("Arial", 20), bg="#59c2e5", fg="#000000")
name_label.pack(pady=10)
name_entry=Entry(window, font=("Arial", 20), bg="#ffffff", fg="#000000")
name_entry.pack(pady=10)

age_label=Label(window, text="Vek: ", font=("Arial", 20), bg="#59c2e5", fg="#000000")
age_label.pack(pady=10)
age_entry=Entry(window, font=("Arial", 20), bg="#ffffff", fg="#000000")
age_entry.pack(pady=10)
city_label=Label(window, text="Mesto: ", font=("Arial", 20), bg="#59c2e5", fg="#000000")
city_label.pack(pady=10)
city_entry=Entry(window, font=("Arial", 20), bg="#ffffff", fg="#000000")
city_entry.pack(pady=10)

#exit button
exit_button=Image.open("img/exit.png")
exit_button=ImageTk.PhotoImage(exit_button)
exit__button = Button(window, image=exit_button, command=window.destroy,bg="#87CEEB", borderwidth=0, highlightthickness=0,)
exit__button.place(relx=1.0, x=-10, y=10, anchor=NE)


#variables to record
points=0
name=""
age=""
city=""

#adding points function
def point():
    global points
    points +=1

#removing forms
def personal_info():
    global name, age, city
    name=name_entry.get()
    age=age_entry.get()
    city=city_entry.get()
    name_label.destroy()
    name_entry.destroy()
    age_label.destroy()
    age_entry.destroy()
    city_label.destroy()
    city_entry.destroy()
    submit_button.destroy()
    preparation() 

#second page "ready?"
def preparation():

    ready=Label(window, text=f"Ahoj ! Si pripravený uhádnuť všetky hlavné mestá?", font=("Arial", 30,), bg="#59c2e5", fg="#000000",)
    ready.pack(pady=100)

    frame=Frame(window, bg="#59c2e5")
    frame.pack(pady=50)
    
    yes_button=Button(frame, text="    Ano    ", font=("Arial", 30), bg="#ffffff", fg="#000000", 
                      command=lambda: [frame.destroy(), ready.destroy(), question_1()])
    yes_button.pack(pady=50, padx=50, side=LEFT)
    no_button=Button(frame, text="    Nie   ", font=("Arial", 30), bg="#ffffff", fg="#000000", command=window.destroy)
    no_button.pack(pady=50, padx=50, side=LEFT)

#questions
def question_1():
    h1=Label(window, text="Aké je hlavné mesto Austrálie?", font=("Arial", 30,), bg="#59c2e5", fg="#000000",)
    h1.pack(pady=30)
    frame1=Frame(window, bg="#59c2e5")
    frame1.pack(pady=50)
    A_button=Button(frame1, text="Sydney", font=("Arial", 30), bg="#ffffff", fg="#000000", command=lambda: [frame1.destroy(), h1.destroy(), question_2(),])
    A_button.pack(pady=50, padx=50, side=LEFT)
    B_button=Button(frame1, text="Melbourne", font=("Arial", 30), bg="#ffffff", fg="#000000", command=lambda: [frame1.destroy(), h1.destroy(), question_2()])
    B_button.pack(pady=50, padx=50, side=LEFT)
    C_button=Button(frame1, text="Canberra", font=("Arial", 30), bg="#ffffff", fg="#000000", command=lambda: [frame1.destroy(), h1.destroy(), question_2(), point(), ])
    C_button.pack(pady=50, padx=50, side=LEFT)
    D_button=Button(frame1, text="Denpassar", font=("Arial", 30), bg="#ffffff", fg="#000000", command=lambda: [frame1.destroy(), h1.destroy(), question_2()])
    D_button.pack(pady=50, padx=50, side=LEFT)


def question_2():
    h2=Label(window, text="Aké je hlavné mesto Českej reoubliky?", font=("Arial", 30,), bg="#59c2e5", fg="#000000",)
    h2.pack(pady=30)
    frame2=Frame(window, bg="#59c2e5")
    frame2.pack(pady=50)
    A_button=Button(frame2, text="Praha", font=("Arial", 30), bg="#ffffff", fg="#000000", command=lambda: [frame2.destroy(), h2.destroy(), question_3(), point(), ])
    A_button.pack(pady=50, padx=50, side=LEFT)
    B_button=Button(frame2, text="Brno", font=("Arial", 30), bg="#ffffff", fg="#000000", command=lambda: [frame2.destroy(), h2.destroy(), question_3(),])
    B_button.pack(pady=50, padx=50, side=LEFT)
    C_button=Button(frame2, text="Plzeň", font=("Arial", 30), bg="#ffffff", fg="#000000", command=lambda: [frame2.destroy(), h2.destroy(), question_3(),])
    C_button.pack(pady=50, padx=50, side=LEFT)
    D_button=Button(frame2, text="Drážďany", font=("Arial", 30), bg="#ffffff", fg="#000000", command=lambda: [frame2.destroy(), h2.destroy(), question_3(),])
    D_button.pack(pady=50, padx=50, side=LEFT)

def question_3():
    h3=Label(window, text="Aké je hlavné mesto Slovenskej reoubliky?", font=("Arial", 30,), bg="#59c2e5", fg="#000000",)
    h3.pack(pady=30)
    frame3=Frame(window, bg="#59c2e5")
    frame3.pack(pady=50)
    A_button=Button(frame3, text="Praha", font=("Arial", 30), bg="#ffffff", fg="#000000", command=lambda: [frame3.destroy(), h3.destroy(), question_4(),])
    A_button.pack(pady=50, padx=50, side=LEFT)
    B_button=Button(frame3, text="Bratislava", font=("Arial", 30), bg="#ffffff", fg="#000000", command=lambda: [frame3.destroy(), h3.destroy(), question_4(), point(), ])
    B_button.pack(pady=50, padx=50, side=LEFT)
    C_button=Button(frame3, text="Košice", font=("Arial", 30), bg="#ffffff", fg="#000000", command=lambda: [frame3.destroy(), h3.destroy(), question_4(),])
    C_button.pack(pady=50, padx=50, side=LEFT)
    D_button=Button(frame3, text="Banská bystrica", font=("Arial", 30), bg="#ffffff", fg="#000000", command=lambda: [frame3.destroy(), h3.destroy(), question_4(),])
    D_button.pack(pady=50, padx=50, side=LEFT)

def question_4():
    h4=Label(window, text="Aké je hlavné mesto Talianska?", font=("Arial", 30,), bg="#59c2e5", fg="#000000",)
    h4.pack(pady=30)
    frame4=Frame(window, bg="#59c2e5")
    frame4.pack(pady=50)
    A_button=Button(frame4, text="Neapol", font=("Arial", 30), bg="#ffffff", fg="#000000", command=lambda: [frame4.destroy(), h4.destroy(), question_5(),])
    A_button.pack(pady=50, padx=50, side=LEFT)
    B_button=Button(frame4, text="Rím", font=("Arial", 30), bg="#ffffff", fg="#000000", command=lambda: [frame4.destroy(), h4.destroy(), question_5(), point(), ])
    B_button.pack(pady=50, padx=50, side=LEFT)
    C_button=Button(frame4, text="Benátky", font=("Arial", 30), bg="#ffffff", fg="#000000", command=lambda: [frame4.destroy(), h4.destroy(), question_5(),])
    C_button.pack(pady=50, padx=50, side=LEFT)
    D_button=Button(frame4, text="Palermo", font=("Arial", 30), bg="#ffffff", fg="#000000", command=lambda: [frame4.destroy(), h4.destroy(), question_5(),])
    D_button.pack(pady=50, padx=50, side=LEFT)

def question_5():
    h5=Label(window, text="Aké je hlavné mesto Mexika?", font=("Arial", 30,), bg="#59c2e5", fg="#000000",)
    h5.pack(pady=30)
    frame5=Frame(window, bg="#59c2e5")
    frame5.pack(pady=50)
    A_button=Button(frame5, text="Mexiko city", font=("Arial", 30), bg="#ffffff", fg="#000000", command=lambda: [frame5.destroy(), h5.destroy(), question_6(), point(), ])
    A_button.pack(pady=50, padx=50, side=LEFT)
    B_button=Button(frame5, text="Guadalachara", font=("Arial", 30), bg="#ffffff", fg="#000000", command=lambda: [frame5.destroy(), h5.destroy(), question_6(),])
    B_button.pack(pady=50, padx=50, side=LEFT)
    C_button=Button(frame5, text="Rio de Janeiro", font=("Arial", 30), bg="#ffffff", fg="#000000", command=lambda: [frame5.destroy(), h5.destroy(), question_6(),])
    C_button.pack(pady=50, padx=50, side=LEFT)
    D_button=Button(frame5, text="Sinaloa", font=("Arial", 30), bg="#ffffff", fg="#000000", command=lambda: [frame5.destroy(), h5.destroy(), question_6(),])
    D_button.pack(pady=50, padx=50, side=LEFT)

def question_6():
    h6=Label(window, text="Aké je hlavné mesto Uzbekistanu?", font=("Arial", 30,), bg="#59c2e5", fg="#000000",)
    h6.pack(pady=30)
    frame6=Frame(window, bg="#59c2e5")
    frame6.pack(pady=50)
    A_button=Button(frame6, text="Teherán", font=("Arial", 30), bg="#ffffff", fg="#000000", command=lambda: [frame6.destroy(), h6.destroy(), question_7(),])
    A_button.pack(pady=50, padx=50, side=LEFT)
    B_button=Button(frame6, text="Bagdad", font=("Arial", 30), bg="#ffffff", fg="#000000", command=lambda: [frame6.destroy(), h6.destroy(), question_7(),])
    B_button.pack(pady=50, padx=50, side=LEFT)
    C_button=Button(frame6, text="Taraz", font=("Arial", 30), bg="#ffffff", fg="#000000", command=lambda: [frame6.destroy(), h6.destroy(), question_7(),])
    C_button.pack(pady=50, padx=50, side=LEFT)
    D_button=Button(frame6, text="Taškent", font=("Arial", 30), bg="#ffffff", fg="#000000", command=lambda: [frame6.destroy(), h6.destroy(), question_7(), point(), ])
    D_button.pack(pady=50, padx=50, side=LEFT)

def question_7():
    h7=Label(window, text="Aké je hlavné mesto Turecka?", font=("Arial", 30,), bg="#59c2e5", fg="#000000",)
    h7.pack(pady=30)
    frame7=Frame(window, bg="#59c2e5")
    frame7.pack(pady=50)
    A_button=Button(frame7, text="Antalya", font=("Arial", 30), bg="#ffffff", fg="#000000", command=lambda: [frame7.destroy(), h7.destroy(), question_8(),])
    A_button.pack(pady=50, padx=50, side=LEFT)
    B_button=Button(frame7, text="Ankara", font=("Arial", 30), bg="#ffffff", fg="#000000", command=lambda: [frame7.destroy(), h7.destroy(), question_8(), point(), ])
    B_button.pack(pady=50, padx=50, side=LEFT)
    C_button=Button(frame7, text="Side", font=("Arial", 30), bg="#ffffff", fg="#000000", command=lambda: [frame7.destroy(), h7.destroy(), question_8(),])
    C_button.pack(pady=50, padx=50, side=LEFT)
    D_button=Button(frame7, text="Istanbul", font=("Arial", 30), bg="#ffffff", fg="#000000", command=lambda: [frame7.destroy(), h7.destroy(), question_8(),])
    D_button.pack(pady=50, padx=50, side=LEFT)

def question_8():
    h8=Label(window, text="Aké je hlavné mesto Japonska?", font=("Arial", 30,), bg="#59c2e5", fg="#000000",)
    h8.pack(pady=30)
    frame8=Frame(window, bg="#59c2e5")
    frame8.pack(pady=50)
    A_button=Button(frame8, text="Tokio", font=("Arial", 30), bg="#ffffff", fg="#000000", command=lambda: [frame8.destroy(), h8.destroy(), question_9(), point(), ])
    A_button.pack(pady=50, padx=50, side=LEFT)
    B_button=Button(frame8, text="Kjoto", font=("Arial", 30), bg="#ffffff", fg="#000000", command=lambda: [frame8.destroy(), h8.destroy(), question_9(),])
    B_button.pack(pady=50, padx=50, side=LEFT)
    C_button=Button(frame8, text="Osaka", font=("Arial", 30), bg="#ffffff", fg="#000000", command=lambda: [frame8.destroy(), h8.destroy(), question_9(),])
    C_button.pack(pady=50, padx=50, side=LEFT)
    D_button=Button(frame8, text="Fukušima", font=("Arial", 30), bg="#ffffff", fg="#000000", command=lambda: [frame8.destroy(), h8.destroy(), question_9(),])
    D_button.pack(pady=50, padx=50, side=LEFT)

def question_9():
    h9=Label(window, text="Aké je hlavné mesto Španielska?", font=("Arial", 30,), bg="#59c2e5", fg="#000000",)
    h9.pack(pady=30)
    frame9=Frame(window, bg="#59c2e5")
    frame9.pack(pady=50)
    A_button=Button(frame9, text="Barcelona", font=("Arial", 30), bg="#ffffff", fg="#000000", command=lambda: [frame9.destroy(), h9.destroy(), question_10(),])
    A_button.pack(pady=50, padx=50, side=LEFT)
    B_button=Button(frame9, text="Valencia", font=("Arial", 30), bg="#ffffff", fg="#000000", command=lambda: [frame9.destroy(), h9.destroy(), question_10(),])
    B_button.pack(pady=50, padx=50, side=LEFT)
    C_button=Button(frame9, text="Malaga", font=("Arial", 30), bg="#ffffff", fg="#000000", command=lambda: [frame9.destroy(), h9.destroy(), question_10(),])
    C_button.pack(pady=50, padx=50, side=LEFT)
    D_button=Button(frame9, text="Madrid", font=("Arial", 30), bg="#ffffff", fg="#000000", command=lambda: [frame9.destroy(), h9.destroy(), question_10(), point(), ])
    D_button.pack(pady=50, padx=50, side=LEFT)

def question_10():
    h10=Label(window, text="Aké je hlavné mesto Kanady?", font=("Arial", 30,), bg="#59c2e5", fg="#000000",)
    h10.pack(pady=30)
    frame10=Frame(window, bg="#59c2e5")
    frame10.pack(pady=50)
    A_button=Button(frame10, text="Toronto", font=("Arial", 30), bg="#ffffff", fg="#000000", command=lambda: [frame10.destroy(), h10.destroy(), summary(),])
    A_button.pack(pady=50, padx=50, side=LEFT)
    B_button=Button(frame10, text="Ottawa", font=("Arial", 30), bg="#ffffff", fg="#000000", command=lambda: [point(), frame10.destroy(), h10.destroy(), summary(),  ])
    B_button.pack(pady=50, padx=50, side=LEFT)
    C_button=Button(frame10, text="Vencouver", font=("Arial", 30), bg="#ffffff", fg="#000000", command=lambda: [frame10.destroy(), h10.destroy(), summary(),])
    C_button.pack(pady=50, padx=50, side=LEFT)
    D_button=Button(frame10, text="Edmonton", font=("Arial", 30), bg="#ffffff", fg="#000000", command=lambda: [frame10.destroy(), h10.destroy(), summary(),])
    D_button.pack(pady=50, padx=50, side=LEFT)

#result summary
def result():
    with open('results.csv', mode='a', newline='', encoding='utf-8') as file:
     writer = csv.writer(file)
     writer.writerow([name, age, city, points])


#last page
def summary():
    h11=Label(window, text=f"Gratulujem! Získal si {points} bodov", font=("Arial", 30,), bg="#59c2e5", fg="#000000",)
    h11.pack(pady=30)
    frame11=Frame(window, bg="#59c2e5")
    frame11.pack(pady=50)
    quit_button=Button(frame11, text="Koniec", font=("Arial", 30), bg="#ffffff", fg="#000000", command=lambda: [window.destroy(), result(), ])
    quit_button.pack(pady=150, padx=200, side=LEFT)

#submit button 
submit_button=Button(window, text="Potvrdit", font=("Arial", 20), command=personal_info)
submit_button.pack(pady=10)
window.mainloop()
