import matplotlib.pyplot as plt
import numpy as np
import datetime

def plot_WindD_WindS_Gust(txtfile, title, save_name):
    file = open(txtfile, "r") #44097h2023.txt
    time=[]
    winddirection=[]   
    windspeed=[]
    gustspeed=[]
    for line in file.readlines()[2:]:
        x=line.split()
        year=int(x[0])
        month=int(x[1])
        day=int(x[2])
        hour=int(x[3])
        minute=int(x[4])
        time.append(datetime.datetime(year, month, day, hour, minute))
        winddirection.append(float(x[5]))
        windspeed.append(float(x[6]))
        gustspeed.append(float(x[7]))
    print(time[0])
    print(winddirection)
    fig = plt.figure()
    ax = fig.add_subplot(111)

    #plt.plot(time, winddirection, "k.", ms=1)
    plt.plot(time, windspeed, "r.", ms=1)
    plt.plot(time, gustspeed, "b.", ms=1)
    #plt.plot(np.nan, np.nan, "ko", ms=5, label="Wind Direction")
    plt.plot(np.nan, np.nan, "ro", ms=5, label="Wind Speed")
    plt.plot(np.nan, np.nan, "bo", ms=5, label="Gust Speed")
    ax.legend()
    plt.ylim(0,25)
    plt.xlabel("Time")
    plt.ylabel("Wind Speed, Gust Speed")
    plt.grid()
    plt.xticks([datetime.datetime(2023, month, 1) for month in range(1, 13)])
    ax.set_xticklabels(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
    plt.xlim(time[0], time[-1])
    plt.margins(0.2)
    plt.subplots_adjust(bottom=0.15)
    plt.title(title)
    plt.savefig(save_name)
    #plt.savefig("wave_height.png")
    return plt.show()

plot_WindD_WindS_Gust("B_44008.txt", "NDBC Bouy 44008 Wind Data", "Bouy 44008_wind.png")