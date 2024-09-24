import matplotlib.pyplot as plt
import numpy as np
import datetime

def plot_WaveH_DomiP_AvgP(txtfile, title, save_name):
    file = open(txtfile, "r") #44097h2023.txt
    time=[]
    waveheight=[]   
    dominantperiod=[]
    averageperiod=[]
    for line in file.readlines()[2:]:
        x=line.split()
        year=int(x[0])
        month=int(x[1])
        day=int(x[2])
        hour=int(x[3])
        minute=int(x[4])
        time.append(datetime.datetime(year, month, day, hour, minute))
        waveheight.append(float(x[8]))
        dominantperiod.append(float(x[9]))
        averageperiod.append(float(x[10]))
    print(time[0])

    fig = plt.figure()
    ax = fig.add_subplot(111)

    plt.plot(time, waveheight, "k.", ms=1)
    plt.plot(time, dominantperiod, "r.", ms=1)
    plt.plot(time, averageperiod, "b.", ms=1)
    plt.plot(np.nan, np.nan, "ko", ms=5, label="Sig. Wave Height [m]")
    plt.plot(np.nan, np.nan, "ro", ms=5, label="Dominant Period [s]")
    plt.plot(np.nan, np.nan, "bo", ms=5, label="Average Period [s]")
    ax.legend()
    plt.ylim(0,20)
    plt.xlabel("Time")
    plt.ylabel("Wave Height, Dominant Period, Average Period")
    plt.grid()
    plt.xticks([datetime.datetime(2012, month, 15) for month in range(1, 13)])
    ax.set_xticklabels(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
    plt.xlim(time[0], time[-1])
    plt.margins(0.2)
    plt.subplots_adjust(bottom=0.15)
    plt.title(title)
    plt.savefig(save_name)
    #plt.savefig("wave_height.png")
    return plt.show()

plot_WaveH_DomiP_AvgP("44011_2012.txt", "NDBC Bouy 44011(2012)", "Bouy 44011(2012).png")
