import argparse
import os

ap = argparse.ArgumentParser()
ap.add_argument("-f", "--frequency", required=True, help="set frequency")
ap.add_argument("-t", "--tick", required=True, help="time duration")
ap.add_argument("-n", "--sample", required=True, help="set the sample rate")

args = vars(ap.parse_args())

print(args)

print('DONE')
