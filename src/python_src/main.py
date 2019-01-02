from ctypes import *

goLibPath = "../build/go_lib.so"

# Load the shared library that contains the exported Go functions
goLib = CDLL(goLibPath)

# Call one of the exported functions
goLib.Hello()

dowland = NewPersonTestStructAsJSON(
    "dowland",
    66.5,
    14
)

matt = NewPersonTestStructAsJSON(
    "matt",
    68.0,
    15
)
