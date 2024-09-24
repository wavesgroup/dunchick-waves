import matplotlib.pyplot as plt
import numpy as np
import datetime

def plot_WindD(txtfile, title, save_name):
    file = open(txtfile, "r") #44097h2023.txt
    time=[]
    winddirection=[]   
    for line in file.readlines()[2:]:
        x=line.split()
        year=int(x[0])
        month=int(x[1])
        day=int(x[2])
        hour=int(x[3])
        minute=int(x[4])
        time.append(datetime.datetime(year, month, day, hour, minute))
        winddirection.append(float(x[5]))
    print(time[0])
    print(winddirection)

    fig = plt.figure()
    ax = fig.add_subplot(111)

    plt.plot(time, winddirection, "k.", ms=1)
    plt.plot(np.nan, np.nan, "ko", ms=5, label="Wind Direction")
    ax.legend()
    plt.ylim(0,360)
    plt.xlabel("Time")
    plt.ylabel("Wind Direction")
    plt.grid()
    plt.xticks([datetime.datetime(2023, month, 1) for month in range(1, 13)])
    ax.set_xticklabels(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
    plt.xlim(time[0], time[-1])
    plt.margins(0.2)
    plt.subplots_adjust(bottom=0.15)
    plt.title(title)
    plt.savefig(save_name)
    plt.show()

plot_WindD("B_44008.txt", "NDBC Buoy 44008 Wind Direction", "Buoy 44008_wind_direction.png")