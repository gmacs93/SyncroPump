
import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interactive
import IPython.display as display

# Define a simple function that creates a sine wave plot with an adjustable frequency
def plot_sine_wave(frequency=1):
    x = np.linspace(0, 2 * np.pi, 1000)
    y = np.sin(frequency * x)

    plt.figure(figsize=(8, 4))
    plt.plot(x, y, label=f'Sine wave with frequency {frequency} Hz')
    plt.xlabel('x')
    plt.ylabel('sin(x)')
    plt.title('Interactive Sine Wave Plot')
    plt.legend()
    plt.grid(True)
    plt.show()

# Create an interactive widget that allows the user to adjust the frequency
interactive_plot = interactive(plot_sine_wave, frequency=(0.5, 5.0, 0.1))

# Display the widget for interaction
display.display(interactive_plot)

