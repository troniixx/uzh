import pandas as pd

exoplanets = pd.read_csv("/Users/merterol/Desktop/VSCode/uzh/Computational Science/Sem 4/PHY124/Exercise 5/exoplanet.eu_catalog.csv")

T_sun = 5800  # K

exoplanets['daylight_strength'] = (
    (exoplanets['star_radius'])**2 * 
    (exoplanets['star_teff'] / T_sun)**4 * 
    (exoplanets['semi_major_axis'])**(-2)
)

exoplanets['mass_earth'] = exoplanets['mass'] * 320

earth_like = exoplanets[
    (exoplanets['mass_earth'] > 0.5) & 
    (exoplanets['mass_earth'] < 1.5) & 
    (exoplanets['daylight_strength'] > 0.5) & 
    (exoplanets['daylight_strength'] < 1.5)
]


print(earth_like.head(10))