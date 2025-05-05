import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from matplotlib.animation import FuncAnimation

beta_day = np.pi * 2 / 365
axis_rad = np.radians(23.5)

def Rx(theta):
    return np.array([[1, 0, 0],
                    [0, np.cos(theta), np.sin(theta)],
                    [0, -np.sin(theta), np.cos(theta)]])

def Ry(theta):
    return np.array([[np.cos(theta), 0, -np.sin(theta)],
                    [0, 1, 0],
                    [np.sin(theta), 0, np.cos(theta)]])

def Rz(theta):
    return np.array([[np.cos(theta), np.sin(theta), 0],
                    [-np.sin(theta), np.cos(theta), 0],
                    [0, 0, 1]])

def daylight(latitude, longitude, date, time):
    lat = np.radians(latitude)
    lon = np.radians(longitude)

    sigma = lon + 2 * np.pi * time + beta_day * date

    e_x = np.array([1, 0, 0])

    e_o = Rx(beta_day * date) @ Rz(-axis_rad) @ e_x

    e_perp = Ry(lat) @ Rz(sigma) @ e_x

    return np.dot(e_o, e_perp)

lats = np.linspace(-90, 90, 180)
lons = np.linspace(-180, 180, 360)
lon_grid, lat_grid = np.meshgrid(lons, lats)

day_of_year = 172

fig = plt.figure(figsize=(10, 5))
ax = plt.axes(projection=ccrs.PlateCarree())
ax.coastlines()
img = ax.imshow(np.zeros_like(lat_grid), extent=[-180, 180, -90, 90],
                origin='lower', cmap='plasma', vmin=-1, vmax=1, transform=ccrs.PlateCarree())

def update(frame):
    time_fraction = frame / 24  # from 0 to 1 (representing the day)
    daylight_vals = np.vectorize(daylight)(lat_grid, lon_grid, day_of_year, time_fraction)
    img.set_data(daylight_vals)
    ax.set_title(f"Daylight Map - Hour {frame}:00 (Day {day_of_year})")
    return [img]

anim = FuncAnimation(fig, update, frames=24, interval=300)

plt.show()