# Created by chb
# Last update 1/17/2022
from tkinter import *

# Create the window
root = Tk(className="Dust calculator")
root.geometry("550x300")

# Variables used later
message = StringVar()
message2 = StringVar()
m1 = StringVar()
m2 = StringVar()
m3 = StringVar()

# All objects for left side
e1 = Entry(root)
e2 = Entry(root)
e3 = Entry(root)
e4 = Entry(root)
e5 = Entry(root)
e6 = Entry(root)
e7 = Entry(root)
e8 = Entry(root)
e9 = Entry(root)
e10 = Entry(root)
t1 = Label(root, text="Current Rate in Billions")
t2 = Label(root, text="Time Left")
hg = Label(root, text="Number of 2x 30 min")
hg2 = Label(root, text="Number of 2x 2 hour")
hg3 = Label(root, text="Number of 10x 5 min")
hg4 = Label(root, text="Number of 10x 30 min")
hg5 = Label(root, text="Number of 20x 5 min")
hg6 = Label(root, text="Number of 20x 30 min")
hg7 = Label(root, text="Number of 50x 5 min")
t4 = Label(root, text="Current Dust in Billions")
l1 = Label(root, text="")
t5 = Label(root, text="Total in Trillions")

# All objects for right side
e21 = Entry(root)
e22 = Entry(root)
e23 = Entry(root)
e24 = Entry(root)
t21 = Label(root, text="Current Rate in Billions")
t22 = Label(root, text="Time Left")
t23 = Label(root, text="Dust Goal in Billions")
t24 = Label(root, text="Current Dust in Billions")
l21 = Label(root, text="")
t25 = Label(root, text="Total Hours of Dust Needed")
col1 = Label(root, text="Number of $2.99 packs")
col2 = Label(root, text="Number of $4.99 packs")
col3 = Label(root, text="Number of $9.99 packs")
col4 = Label(root, text="")
col5 = Label(root, text="")
col6 = Label(root, text="")


# Function for pressing left submit button
def press():
    if e1.get().replace(".", "", 1).isnumeric() and e2.get().replace(".", "", 1).isnumeric() \
            and e3.get().replace(".", "", 1).isnumeric() \
            and e4.get().replace(".", "", 1).isnumeric() and e5.get().replace(".", "", 1).isnumeric()\
            and e6.get().replace(".", "", 1).isnumeric() and e7.get().replace(".", "", 1).isnumeric()\
            and e8.get().replace(".", "", 1).isnumeric() and e9.get().replace(".", "", 1).isnumeric()\
            and e4.get().replace(".", "", 1).isnumeric():
        totalglass = glassCalc()
        message.set(str(((float(e1.get()) * 60 * (float(e2.get()) + totalglass) + float(e10.get())) / 1000)))
        l1.config(text=message.get())
    else:
        l1.config(text="Invalid Entry")

# Function for pressing right submit button
def press2():
    if e21.get().replace(".", "", 1).isnumeric() and e22.get().replace(".", "", 1).isnumeric() \
            and e23.get().replace(".", "", 1).isnumeric() and e24.get().replace(".", "", 1).isnumeric():
        message2.set(str((-60*float(e21.get())*float(e22.get()) - float(e24.get()) +
                          float(e23.get()))/(60*float(e21.get()))))
        l21.config(text=message2.get())
        current = float(e24.get())
        rate = float(e21.get())
        total = float(e23.get())
        maxTime = float(e22.get()) * 60
        final, countFreePack, countPack1, countPack2, countPack3, totalDust = calc(current, rate, total, maxTime)
        m1.set(countPack1)
        m2.set(countPack2)
        m3.set(countPack3)
        col4.config(text=m1.get())
        col5.config(text=m2.get())
        col6.config(text=m3.get())
    else:
        l21.config(text="Invalid Entry")


# Function to calculate glass totals for left side
def glassCalc():
    total = 0.0
    r = []
    g1 = ((float(e3.get()) * 30) / 60) * 2
    x1 = (float(e3.get()) * 30 / 60)
    r.append(x1)

    g2 = ((float(e4.get()) * 120) / 60) * 2
    x2 = (float(e4.get()) * 120 / 60)
    r.append(x2)

    g3 = ((float(e5.get()) * 5) / 60) * 10
    x3 = (float(e5.get()) * 5 / 60)
    r.append(x3)

    g4 = ((float(e6.get()) * 30) / 60) * 10
    x4 = (float(e6.get()) * 30 / 60)
    r.append(x4)

    g5 = ((float(e7.get()) * 5) / 60) * 20
    x5 = (float(e7.get()) * 5 / 60)
    r.append(x5)

    g6 = ((float(e8.get()) * 30) / 60) * 20
    x6 = (float(e8.get()) * 30 / 60)
    r.append(x6)

    g7 = ((float(e9.get()) * 5) / 60) * 50
    x7 = (float(e9.get()) * 5 / 60)
    r.append(x7)

    total = (g1+g2+g3+g4+g5+g6+g7) - max(r)
    return total

# Calculate how much to buy from shop
def calc(current, rate, total, maxTime, counts=[0, 0, 0, 0], final=-1.0, fC0=0, fC1=0, fC2=0, fC3=0, tDust=0):
    x2Time = 30 * counts[0] + 120 * counts[1]
    x10Time = 5 * counts[1] + 30 * counts[2]
    x20Time = 5 * counts[2] + 30 * counts[3]
    x50Time = 5 * counts[3]

    highTime = max(x2Time, x10Time, x20Time, x50Time)

    tCurrent = current + (rate) * (maxTime + 2 * x2Time + 10 * x10Time + 20 * x20Time + 50 * x50Time - highTime)
    cost = counts[1] * 3.00 + counts[2] * 5.00 + counts[3] * 10.00

    if tCurrent >= total and (cost < final or final == -1.0):
        final = cost
        finalCounts = counts
        return cost, counts[0], counts[1], counts[2], counts[3], tCurrent

    elif cost > final and final >= 0.0:
        return final, fC0, fC1, fC2, fC3, tDust

    elif cost == final and final >= 0.0:
        return cost, counts[0], counts[1], counts[2], counts[3], tCurrent

    else:
        if counts[0] < 0:
            counts[0] += 1
            final, fC0, fC1, fC2, fC3, tDust = calc(current, rate, total, maxTime, counts, final, fC0, fC1, fC2, fC3,
                                                    tDust)
            counts[0] -= 1
        if counts[1] < 10:
            counts[1] += 1
            final, fC0, fC1, fC2, fC3, tDust = calc(current, rate, total, maxTime, counts, final, fC0, fC1, fC2, fC3,
                                                    tDust)
            counts[1] -= 1
        if counts[2] < 10:
            counts[2] += 1
            final, fC0, fC1, fC2, fC3, tDust = calc(current, rate, total, maxTime, counts, final, fC0, fC1, fC2, fC3,
                                                    tDust)
            counts[2] -= 1
        if counts[3] < 10:
            counts[3] += 1
            final, fC0, fC1, fC2, fC3, tDust = calc(current, rate, total, maxTime, counts, final, fC0, fC1, fC2, fC3,
                                                    tDust)
            counts[3] -= 1
        return final, fC0, fC1, fC2, fC3, tDust


# Adding buttons to UI
b1 = Button(root, text="Submit", command=press).grid(row=10, column=1)
b2 = Button(root, text="Submit", command=press2).grid(row=4, column=3)

# Adding left side to UI
t1.grid(row=0, column=0)
e1.grid(row=0, column=1)
t2.grid(row=1, column=0)
e2.grid(row=1, column=1)
hg.grid(row=2, column=0)
e3.grid(row=2, column=1)
hg2.grid(row=3, column=0)
e4.grid(row=3, column=1)
hg3.grid(row=4, column=0)
e5.grid(row=4, column=1)
hg4.grid(row=5, column=0)
e6.grid(row=5, column=1)
hg5.grid(row=6, column=0)
e7.grid(row=6, column=1)
hg6.grid(row=7, column=0)
e8.grid(row=7, column=1)
hg7.grid(row=8, column=0)
e9.grid(row=8, column=1)
t4.grid(row=9, column=0)
e10.grid(row=9, column=1)
t5.grid(row=11, column=0)
l1.grid(row=11, column=1)

# Adding right side to UI
t21.grid(row=0, column=2)
e21.grid(row=0, column=3)
t22.grid(row=1, column=2)
e22.grid(row=1, column=3)
t23.grid(row=2, column=2)
e23.grid(row=2, column=3)
t24.grid(row=3, column=2)
e24.grid(row=3, column=3)
t25.grid(row=5, column=2)
l21.grid(row=5, column=3)
col1.grid(row=6, column=2)
col4.grid(row=6, column=3)
col2.grid(row=7, column=2)
col5.grid(row=7, column=3)
col3.grid(row=8, column=2)
col6.grid(row=8, column=3)


# Keep window open
root.mainloop()