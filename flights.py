import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import requests

url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/{}/v1.0/CA/{}/en-CA/{}/{}/{}"

headers = {
    'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
    'x-rapidapi-key': "fddc2605admsh9a8e76335f7477ep13c63ajsn21ce03eaa80a"
    }

def searchFlights():
    mode = dropdown.get()
    if(mode == "Cheapest Quote"):
        mode = "browsequotes"
    elif(mode == "Cheapest Date"):
        mode = "browsedates"
    elif(mode == "Cheapest Route"):
        mode = "browseroutes"

    currency = currencyEntry.get()

    origin = originEntry.get()
    origin += "-sky"

    destination = destinationEntry.get()
    destination += "-sky"

    departure = departureEntry.get()

    global url
    url = url.format(mode,currency,origin,destination,departure)

    flightList = requests.request("GET", url, headers=headers)

    updateOutput(flightList)


def updateOutput(list):
    listJson = list.json()
    print(listJson)


if(__name__ == "__main__"):
    flights = tk.Tk()
    flights.title("Flight Searcher")
    canv = tk.Canvas(flights,height=600,width=600).pack()
    flights.resizable(False,False)

    image = ImageTk.PhotoImage(Image.open("D:\\Desktop\\Projects\\Flights\\clouds.jpg"))
    background = tk.Label(flights, image=image)
    background.place(x=0, y=0)

    title = tk.Frame(flights, bg='navajo white',highlightbackground="black" , highlightthickness=2)
    title.place(relx = 0.5, rely = 0.03, relwidth = 0.32, relheight = 0.08, anchor='n')
    guiTitle = tk.Label(title, text ="Flight Searcher",font= ("Arial",19,'bold'), bg = "navajo white")
    guiTitle.place(relx = 0.5,rely = 0.5, anchor ="center" )

    inputbox = tk.Frame(flights, bg='navajo white',highlightbackground="black" , highlightthickness=2)
    inputbox.place(relx = 0.5, rely = 0.13, relwidth = 0.8, relheight = 0.5, anchor='n')

    inputTitle = tk.Label(inputbox, text = "Input Box" , font=("Arial",16,'bold'),bg='navajo white')
    inputTitle.place(relx = 0.5,anchor='n')


    inputbox2 = tk.Frame(inputbox,bg='orange')
    inputbox2.place(relx = 0.5, rely = 0.10, relwidth = 0.95, relheight = 0.85, anchor='n')

    modeSelect = tk.Frame(inputbox2, bg='dark orange2')
    modeSelect.place(relx = 0.3, rely = 0.12, relwidth = 0.55, relheight = 0.12, anchor='center')

    dropdownTitle = tk.Label(modeSelect,text = "Search Method:",font=("Arial",13),bg='dark orange2')
    dropdownTitle.place(relx = 0.25,rely = 0.5,anchor='center')
    options = ["Cheapest Date","Cheapest Quote","Cheapest Route"]
    dropdown = ttk.Combobox(modeSelect, values = options)
    dropdown.place(relx=0.74,rely = 0.5,relwidth = 0.45,anchor='center')


    currencySelect = tk.Frame(inputbox2, bg='dark orange2')
    currencySelect.place(relx = 0.8, rely = 0.12, relwidth = 0.37, relheight = 0.12, anchor='center')

    currencyTitle = tk.Label(currencySelect,text = "Currency:",font=("Arial",13),bg='dark orange2')
    currencyTitle.place(relx = 0.29,rely = 0.5, anchor = "center")
    currencyEntry = tk.Entry(currencySelect,justify='center')
    currencyEntry.place(relx = 0.75,rely=0.5,relwidth=0.4,anchor='center')


    originSelect = tk.Frame(inputbox2,bg='dark orange2')
    originSelect.place(relx = 0.5, rely = 0.30, relwidth = 0.6, relheight = 0.12, anchor='center')

    originTitle = tk.Label(originSelect,text = "Origin Airport Code(IATA):",font=("Arial",13),bg='dark orange2')
    originTitle.place(relx = 0.38,rely = 0.5, anchor = "center")
    originEntry = tk.Entry(originSelect,justify='center')
    originEntry.place(relx = 0.86,rely=0.5,relwidth=0.2,anchor='center')


    destinationSelect = tk.Frame(inputbox2,bg='dark orange2')
    destinationSelect.place(relx = 0.5, rely = 0.48, relwidth = 0.69, relheight = 0.12, anchor='center')

    destinationTitle = tk.Label(destinationSelect,text = "Destination Airport Code(IATA):",font=("Arial",13),bg='dark orange2')
    destinationTitle.place(relx = 0.38,rely = 0.5, anchor = "center")
    destinationEntry = tk.Entry(destinationSelect,justify='center')
    destinationEntry.place(relx = 0.87,rely=0.5,relwidth=0.19,anchor='center')


    departureSelect = tk.Frame(inputbox2,bg='dark orange2')
    departureSelect.place(relx = 0.5, rely = 0.66, relwidth = 0.75, relheight = 0.12, anchor='center')

    departureTitle = tk.Label(departureSelect,text = "Departure Date(YYYY-MM-DD):",font=("Arial",13),bg='dark orange2')
    departureTitle.place(relx = 0.36,rely = 0.5, anchor = "center")
    departureEntry = tk.Entry(departureSelect,justify='center')
    departureEntry.place(relx = 0.84,rely=0.5,relwidth=0.25,anchor='center')


    searchButton = tk.Button(inputbox2,activebackground="dark orange3",relief='ridge',text = "Search",font=("Arial",13),bg='dark orange2',command=searchFlights)
    searchButton.place(relx = 0.5,rely=0.88, anchor='center')

    flights.mainloop()

