# Animation demo for matplotlib.animation
# I.Stoianov, 26 Nov 2024, CNR, Italy

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from datetime import datetime

class AnimClock():
    def __init__(self):
        # Figure for the animation
        self.fig, self.ax = plt.subplots()
        self.ax.set_xlim(-1,1)
        self.ax.set_ylim(-1,1)
        self.ax.set_aspect("equal","box")
        self.ax.set_axis_off()

        # Static content: clock numbers
        for f in range(12):
            ang = ( (f*5+15) % 60) / 60 * 2 * np.pi
            x = np.cos(ang)*1
            y = np.sin(ang)*1
            self.ax.text(x,y,f"{f*5}",horizontalalignment="center",verticalalignment="center")

        # Create graphical objects to be animated, setting some initial state
        self.line, = self.ax.plot([],[], lw=2)
        self.text  = self.ax.text(0, 0, "", horizontalalignment="center", verticalalignment="center",fontsize=20)

    # Define an init function that sets some initial state
    def init_clock(self):
        self.line.set_data([],[])       # Empty hand
        self.text.set_text("")          # No digital time
        return self.line,self.text      # Initialize (again) the animated objects

    # Define update method which update the state of the dynamic objects
    def update_clock(self,frame):
        T=datetime.now()                # Get the real time.
        # Convert time into hand angle. So in this example time is what determines the clock position
        ang = ( (T.second+T.microsecond/1e6 + 15) ) / 60 * 2 * np.pi
        # Define the line which represents the clock-hand
        X = [0, np.cos(ang) * 0.9]
        Y = [0, np.sin(ang) * 0.9]
        # Update the position of the object that represent the clock-hand
        self.line.set_data(X,Y)
        # Update the text that show the real time with digits, and also frame number
        self.text.set_text(T.strftime("%H:%M:%S")+f" frame {frame}")
        # Return the two animated objects as a tuple
        return self.line, self.text

    # Define the main animation that works on the graphical objects.
    def run(self, steps):
        anim = FuncAnimation(self.fig,
                             self.update_clock,
                             init_func = self.init_clock,
                             frames = steps,  # How many times to run
                             interval = 10,   # time interval between every two frames, in milliseconds
                             blit=True)
        plt.show()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    CLK=AnimClock().run(12000)                  # Create a clock object and run it for 12000 frames.
