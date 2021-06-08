import os
from numpy import array, arange, linspace
from math import pi, sin
import struct

def generate_sound(duration: float, volume: float, sampling_rate:float, freq: float):
    wave: array = array([sin(freq*i) for i in linspace(0, duration, int(duration*sampling_rate))])
    return wave

def main():
    ################################# Variable Declaration ##############################
    DURATION:float = 8 
    FREQ: float = 440
    VOLUME:float = 4
    LOG:str = os.path.abspath("./debug.log")
    OUTPUT: str = os.path.abspath("./output.bin")
    SAMPLING_RATE: float = 48000 # number of samples per seconds from output.bin
    CMD: str = f'ffplay -f f32le -showmode 1 -ar {SAMPLING_RATE} {OUTPUT}'
    ############################# Variable Declaration ends #############################
    WAVE:array = generate_sound(duration = DURATION, volume = VOLUME, sampling_rate = SAMPLING_RATE, freq = FREQ)

    bytestring = ''
    for wave in WAVE:
        bytestring += str(wave) + '\n'

    with open(OUTPUT, 'wb') as f:
        f.write(struct.pack(f"<{len(WAVE)}f", *WAVE))

    with open(LOG, 'w') as f:
        f.write(bytestring)

    os.system(CMD + "&")
    

if __name__ == "__main__":
    main()
