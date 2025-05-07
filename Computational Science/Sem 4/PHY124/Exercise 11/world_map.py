import numpy as np
import matplotlib.pyplot as plt

def load_and_plot_height_data():
    terrain = np.loadtxt('terrain.xyz', skiprows=1)
    surface = np.loadtxt('surface.xyz', skiprows=1)


    x_terrain, y_terrain, z_terrain = terrain[:, 0], terrain[:, 1], terrain[:, 2]
    x_surface, y_surface, z_surface = surface[:, 0], surface[:, 1], surface[:, 2]
    
    # 1000m / 0.5m = 2000 points per side
    grid_size = 2000
    
    # Reshape the 1D arrays into 2D grids
    z_terrain_grid = z_terrain.reshape((grid_size, grid_size))
    z_surface_grid = z_surface.reshape((grid_size, grid_size))
    
    # Create meshgrid for plotting
    x_grid = x_terrain.reshape((grid_size, grid_size))
    y_grid = y_terrain.reshape((grid_size, grid_size))
    
    # Plot the surface data
    plt.figure(figsize=(12, 10))
    
    # Contour plot of the surface
    plt.subplot(2, 2, 1)
    contours = plt.contourf(x_grid, y_grid, z_surface_grid, levels=20, cmap='terrain')
    plt.colorbar(contours, label='Height (m)')
    plt.title('Surface Height (with vegetation and buildings)')
    plt.xlabel('X coordinate (m)')
    plt.ylabel('Y coordinate (m)')
    plt.gca().set_aspect('equal')
    
    # Contour plot of the terrain
    plt.subplot(2, 2, 2)
    contours = plt.contourf(x_grid, y_grid, z_terrain_grid, levels=20, cmap='terrain')
    plt.colorbar(contours, label='Height (m)')
    plt.title('Terrain Height (without vegetation and buildings)')
    plt.xlabel('X coordinate (m)')
    plt.ylabel('Y coordinate (m)')
    plt.gca().set_aspect('equal')
    
    # Calculate and plot the difference (vegetation and buildings height)
    plt.subplot(2, 2, 3)
    height_diff = z_surface_grid - z_terrain_grid
    contours = plt.contourf(x_grid, y_grid, height_diff, levels=20, cmap='viridis')
    plt.colorbar(contours, label='Height difference (m)')
    plt.title('Vegetation and Buildings Height Above Terrain')
    plt.xlabel('X coordinate (m)')
    plt.ylabel('Y coordinate (m)')
    plt.gca().set_aspect('equal')

    plt.tight_layout()
    plt.show()

load_and_plot_height_data()