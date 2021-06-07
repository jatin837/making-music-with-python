import os
from numpy import array, sin

def main():
    STEP: float = 0.01
    SAMPLING_RATE: float = 48000
    WAVE: array = np.sin(np.linspace(0.0, SAMPLING_RATE*STEP, SAMPLING_RATE))
    print(WAVE)
    

if __name__ = "__main__":
    main()
