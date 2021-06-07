import os
from numpy import array, sin, linspace

def main():

    OUTPUT: str = os.path.abspath("./output.bin")
    SAMPLING_RATE: float = 48000
    CMD: str = f'ffplay -f -showmod 1 f32le -ar {SAMPLING_RATE} {OUTPUT}'
    STEP: float = 0.01
    WAVE: array = sin(linspace(0.0, SAMPLING_RATE*STEP, SAMPLING_RATE))

    with open(OUTPUT, 'wb') as f:
        f.write(WAVE)

    

if __name__ == "__main__":
    main()
