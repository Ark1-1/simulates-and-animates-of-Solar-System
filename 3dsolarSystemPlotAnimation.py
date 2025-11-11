from astropy.time import Time
from astropy.coordinates import solar_system_ephemeris, get_body_barycentric_posvel
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.animation as animation

# Set the ephemeris to 'builtin'
solar_system_ephemeris.set('builtin')

# Define the time period over which we want to calculate positions
start_time = Time("2024-01-01")
end_time = Time("2204-01-01")
delta_t = end_time - start_time
times = start_time + delta_t * np.linspace(0, 1, 365)

# Calculate positions of the planets
neptune = get_body_barycentric_posvel('neptune', times)[0]
uranus = get_body_barycentric_posvel('uranus', times)[0]
saturn = get_body_barycentric_posvel('saturn', times)[0]
jupiter = get_body_barycentric_posvel('jupiter', times)[0]
mars = get_body_barycentric_posvel('mars', times)[0]
earth = get_body_barycentric_posvel('earth', times)[0]
venus = get_body_barycentric_posvel('venus', times)[0]
mercury = get_body_barycentric_posvel('mercury', times)[0]

# Create a new figure for the 3D plot
fig = plt.figure(figsize=(20, 20))
ax = fig.add_subplot(111, projection='3d')

# Initialize the plots with the first data point and store the line objects
line_neptune, = ax.plot(neptune.x[0], neptune.y[0], neptune.z[0], label="Neptune")
line_uranus, = ax.plot(uranus.x[0], uranus.y[0], uranus.z[0], label="Uranus")
line_saturn, = ax.plot(saturn.x[0], saturn.y[0], saturn.z[0], label='Saturn')
line_jupiter, = ax.plot(jupiter.x[0], jupiter.y[0], jupiter.z[0], label="Jupiter")
line_mars, = ax.plot(mars.x[0], mars.y[0], mars.z[0], label='Mars')
line_earth, = ax.plot(earth.x[0], earth.y[0], earth.z[0], label='Earth')
line_venus, = ax.plot(venus.x[0], venus.y[0], venus.z[0], label='Venus')
line_mercury, = ax.plot(mercury.x[0], mercury.y[0], mercury.z[0], label='Mercury')

# Add labels and title
ax.set_xlabel('x [au]')
ax.set_ylabel('y [au]')
ax.set_zlabel('z [au]')
plt.title('3D Positions of Planets over One Year')
plt.legend()
plt.grid(True)

# Set the limits of the 3D plot
ax.set_xlim([-35, 35])
ax.set_ylim([-35, 35])
ax.set_zlim([-35, 35])

# Define the update function
def update(num):
    line_neptune.set_data(neptune.x[:num], neptune.y[:num])
    line_neptune.set_3d_properties(neptune.z[:num])
    
    line_uranus.set_data(uranus.x[:num], uranus.y[:num])
    line_uranus.set_3d_properties(uranus.z[:num])
    
    line_saturn.set_data(saturn.x[:num], saturn.y[:num])
    line_saturn.set_3d_properties(saturn.z[:num])
    
    line_jupiter.set_data(jupiter.x[:num], jupiter.y[:num])
    line_jupiter.set_3d_properties(jupiter.z[:num])
    
    line_mars.set_data(mars.x[:num], mars.y[:num])
    line_mars.set_3d_properties(mars.z[:num])
    
    line_earth.set_data(earth.x[:num], earth.y[:num])
    line_earth.set_3d_properties(earth.z[:num])
    
    line_venus.set_data(venus.x[:num], venus.y[:num])
    line_venus.set_3d_properties(venus.z[:num])
    
    line_mercury.set_data(mercury.x[:num], mercury.y[:num])
    line_mercury.set_3d_properties(mercury.z[:num])

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=len(times), interval=100, blit=False, repeat=False)

plt.show()
