import pandas as pd
from sys import argv

def process(input):
    exoplanets = pd.read_csv(input)

    T_sun = 5800  # K

    exoplanets["daylight_strength"] = (
        (exoplanets["star_radius"])**2 * 
        (exoplanets["star_teff"] / T_sun)**4 * 
        (exoplanets["semi_major_axis"])**(-2)
    )

    exoplanets["mass_earth"] = exoplanets["mass"] * 320

    earth_like = exoplanets[
        (exoplanets["mass_earth"] > 0.5) & 
        (exoplanets["mass_earth"] < 1.5) & 
        (exoplanets["daylight_strength"] > 0.5) & 
        (exoplanets["daylight_strength"] < 1.5)
    ]


    return earth_like.head(10)

if __name__ == "__main__":
    if len(argv) < 2:
        print("Usage: python planets.py <input_file>")
        exit(1)

    IN = argv[1]
    print(process(IN))