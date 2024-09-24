
from datetime import datetime
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import numpy as np
import os
import matplotlib.patches as mpatches
from ndbc import Station
from datetime import datetime

#lat_44008=40.496 N 69.250 W

buoy_ids = [44008, 44011, 44097]

buoy = Station(buoy_ids[0], datetime(2023,1,1), datetime(2023,12,1))

crs = ccrs.LambertConformal(central_longitude=buoy.lon, central_latitude=buoy.lat) # Set central lat/lon of map
fig, ax = plt.subplots(figsize=(8, 6), subplot_kw={'projection': ccrs.PlateCarree()})
ax.set_extent([-75, -65, 35, 45])
ax.add_feature(cfeature.COASTLINE.with_scale('50m'), linewidth=1) # Set coastline
gl = ax.gridlines(draw_labels=True, linewidth=0.5, color='gray', alpha=0.6, linestyle='--')
#gl.top_labels = False
#gl.right_labels = False
plt.title("Bouy's: 44088,44011,44097 Positioning")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
for buoy_id in buoy_ids:
    buoy = Station(buoy_id, datetime(2023,1,1), datetime(2023,12,1))
    ax.plot(buoy.lon, buoy.lat, "ro")
    ax.text(buoy.lon, buoy.lat, buoy.id)
  
    #TODO: Draw text with the buoy ID next to the buoy marker circle
plt.savefig("buoy_positionings.png")
plt.show()

#plt.close()