from ctypes import *

goLibPath = "../build/go_lib.so"

# Load the shared library that contains the exported Go functions
goLib = CDLL(goLibPath)

# Call one of the exported functions
goLib.Hello()


