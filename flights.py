import tkinter as tk
from PIL import ImageTk, Image
import requests

url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/"

querystring = {"inboundpartialdate":"2021-12-01"}

headers = {
    'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
    'x-rapidapi-key': "fddc2605admsh9a8e76335f7477ep13c63ajsn21ce03eaa80a"
    }

flights = tk.Tk()
flights.title("Flights")
canv = tk.Canvas(flights,height=600,width=600).pack()
image = ImageTk.PhotoImage(Image.open("D:\\Desktop\\Projects\\Covid GUI\\clouds.jpg"))
background = tk.Label(flights, image=image)
background.place(x=0, y=0, relwidth=1, relheight=1)
flights.mainloop()

