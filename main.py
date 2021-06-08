import os
from numpy import array, sin, linspace
import struct

def generate_sound(duration: float, volume: float, sampling_rate: float, step:float):
    wave: array = sin(volume*linspace(0.0, sampling_rate*step*duration, int(sampling_rate*duration)))
    return wave

def main():
    ################################# Variable Declaration ##############################
    DURATION:float = 2 
    VOLUME:float = 2
    LOG:str = os.path.abspath("./debug.log")
    OUTPUT: str = os.path.abspath("./output.bin")
    SAMPLING_RATE: float = 48000 # number of samples per seconds from output.bin
    CMD: str = f'ffplay -f f32le -showmode 1 -ar {SAMPLING_RATE} {OUTPUT}'
    STEP: float = 0.01
    ############################# Variable Declaration ends #############################
    WAVE:array = generate_wave(duration = DURATION, volume = VOLUME, sampling_rate = SAMPLING_RATE, step = STEP)

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
