try:
    import numpy as np
    import matplotlib.pyplot as plt

    print("NumPy and Matplotlib are installed correctly.")
    print(f"NumPy version: {np.__version__}")
    print(f"Matplotlib version: {plt.matplotlib.__version__}")

except ImportError as e:
    print(f"Error: {e}")
    print("NumPy and/or Matplotlib are not installed correctly.")
