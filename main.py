import os
from numpy import array, sin, linspace

def main():
    DURATION:float = 4
    VOLUME:float = 2
    OUTPUT: str = os.path.abspath("./output.bin")
    SAMPLING_RATE: float = 48000
    CMD: str = f'ffplay -f f32le -showmode 1 -ar {SAMPLING_RATE} {OUTPUT}'
    STEP: float = 0.01
    WAVE: array = sin(VOLUME*linspace(0.0, SAMPLING_RATE*STEP*4, 4*SAMPLING_RATE))

    with open(OUTPUT, 'wb') as f:
        f.write(WAVE)

    os.system(CMD + "&")
    

if __name__ == "__main__":
    main()
