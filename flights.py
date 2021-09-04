import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import requests

url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/{}/v1.0/{}/{}/{}/{}/{}/{}"

headers = {
    'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
    'x-rapidapi-key': "fddc2605admsh9a8e76335f7477ep13c63ajsn21ce03eaa80a"
    }

if(__name__ == "__main__"):
    flights = tk.Tk()
    flights.title("Flight Searcher")
    canv = tk.Canvas(flights,height=600,width=600).pack()

    image = ImageTk.PhotoImage(Image.open("D:\\Desktop\\Projects\\Flights\\clouds.jpg"))
    background = tk.Label(flights, image=image)
    background.place(x=0, y=0)

    title = tk.Frame(flights, bg='navajo white',highlightbackground="black" , highlightthickness=2)
    title.place(relx = 0.5, rely = 0.03, relwidth = 0.32, relheight = 0.08, anchor='n')
    guiTitle = tk.Label(title, text ="Flight Searcher",font= ("Arial",19,'bold'), bg = "navajo white")
    guiTitle.place(relx = 0.5,rely = 0.14, anchor ="n" )

    inputbox = tk.Frame(flights, bg='navajo white',highlightbackground="black" , highlightthickness=2)
    inputbox.place(relx = 0.5, rely = 0.13, relwidth = 0.8, relheight = 0.5, anchor='n')

    inputTitle = tk.Label(inputbox, text = "Input Box" , font=("Arial",16,'bold'),bg='navajo white')
    inputTitle.place(relx = 0.14,anchor='n')


    inputbox2 = tk.Frame(inputbox,bg='orange')
    inputbox2.place(relx = 0.5, rely = 0.10, relwidth = 0.95, relheight = 0.85, anchor='n')

    modeSelect = tk.Frame(inputbox2, bg='dark orange2')
    modeSelect.place(relx = 0.33, rely = 0.04, relwidth = 0.6, relheight = 0.12, anchor='n')

    dropdownTitle = tk.Label(inputbox,text = "Search Method:",font=("Arial",13),bg='navajo white')
    dropdownTitle.place(relx = 0.6,rely = 0.015,anchor='n')
    initial = tk.StringVar()
    initial.set("Cheapest Date")
    options = ["Cheapest Date","Cheapest Quote","Cheapest Route"]
    dropdown = ttk.Combobox(inputbox, values = options)
    dropdown.place(relx=0.85,rely = 0.02,relwidth = 0.25,anchor='n')


    flights.mainloop()

