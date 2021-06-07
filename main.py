import os
from numpy import array, sin, linspace
import struct

def main():
    DURATION:float = 2 
    VOLUME:float = 2
    LOG:str = os.path.abspath("./debug.log")
    OUTPUT: str = os.path.abspath("./output.bin")
    SAMPLING_RATE: float = 48000 # number of samples per seconds from output.bin
    CMD: str = f'ffplay -f f32le -showmode 1 -ar {SAMPLING_RATE} {OUTPUT}'
    STEP: float = 0.01
    WAVE: array = sin(VOLUME*linspace(0.0, SAMPLING_RATE*STEP*DURATION, int(SAMPLING_RATE*DURATION)))

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
