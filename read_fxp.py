import argparse
import numpy as np

#arguments to pars
parser = argparse.ArgumentParser(description='Pro')
parser.add_argument('-f1', type=str, help='File 1 to read')
parser.add_argument('-f2', type=str, help='File 2 to read')
args = parser.parse_args()

#initialize list of bytes from fxp file
byte_array1 = list()

#read fxp file
try:
    with open(args.f1, "rb") as f:
        byte = f.read(1)
        while byte:
            byte_array1.append(byte)
            # zero_array.append(hex(int.from_bytes(byte,"big")))
            byte = f.read(1)
except IOError:
    print('Error While Opening the file!')  


#initialize list of bytes from fxp file
byte_array2 = list()

#read fxp file
try:
    with open(args.f2, "rb") as f:
        byte = f.read(1)
        while byte:
            byte_array2.append(byte)
            # zero_array.append(hex(int.from_bytes(byte,"big")))
            byte = f.read(1)
except IOError:
    print('Error While Opening the file!') 

smaller = min(len(byte_array1),len(byte_array2))

for i in range(100):
    print(int.from_bytes(byte_array1[i], "big") - int.from_bytes(byte_array2[i], "big"))