import requests
import datetime
import tkinter
import matplotlib.pyplot as plt
import sys
import numpy as np
print (sys.version)
response= requests.get("http://api.open-notify.org/iss-now.json")
parameters= {"lat": 41.543555, "lon": 1.670935, "alt": 350.00, "n": 3}
lets=requests.get("http://api.open-notify.org/iss-pass.json",parameters)
pers=requests.get("http://api.open-notify.org/astros.json")
numb=pers.json()
k=numb.keys()
passs=lets.json()
print(passs["response"])
print(numb["number"])
print(numb["people"])
peop=numb["people"]
#print(peop[0])
dii=lets.json()
#print(dii.keys())
#print(dii["request"])

weather = requests.get("https://api.darksky.net/forecast/138a7ea2f7e6dbafd0d1544d4a84f73d/41.543555,1.670935?units=si")
print(weather)
weather = weather.json()
h= weather["hourly"]
dat=h["data"]
hora_0=dat[0]
timee=hora_0["time"]
curr=weather["currently"]
print(curr["time"])

timeer=datetime.datetime.fromtimestamp(curr["time"]+3600).strftime('%Y-%m-%d %H:%M:%S')
print(timeer)
print(timee)
#root1=tkinter.Tk()
#labell2=tkinter.Label(root1,text=timeer)
#labell2.pack()
#root1.mainloop()
timeer=datetime.datetime.fromtimestamp(timee+3600).strftime('%Y-%m-%d %H:%M:%S')
print(timeer)
#tkinter._test()
def printName():
    print("Hello my name is Tete!")
def printName2(event):
    print("Hello")

root=tkinter.tk()
one = tkinter.Label(root, text = "Name")
two = tkinter.Label(root, text = "Password")
button = tkinter.Button(root, text = "Print", command = printName)
button2 = tkinter.Button(root, text = "Print2")
button2.bind("<Button-1>", printName2)
button2.grid(row = 3, column = 1)
entry_1 = tkinter.Entry(root)
entry_2 = tkinter.Entry(root)

one.grid(row = 0, column = 0, sticky = tkinter.E)
two.grid(row = 1, column = 0, sticky = tkinter.E)

entry_1.grid(row = 0, column = 1)
entry_2.grid(row = 1, column = 1)

c = tkinter.Checkbutton(root, text = "do you are")
c.grid(columnspan = 2)
button.grid(row = 2, column = 0)
#labell=tkinter.Label(root,text=timeer)
#labell.pack()
root.mainloop()

plt.plot([1, 2, 3, 4, 5])
plt.show()
