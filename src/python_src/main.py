from ctypes import *

goLibPath = "../build/go_lib.so"

# Load the shared library that contains the exported Go functions
goLib = CDLL(goLibPath)
goLib.NewPersonTestStructAsJSON.restype = c_char_p

# Call one of the exported functions
goLib.Hello()


dowland = goLib.NewPersonTestStructAsJSON(
    c_wchar_p("dowland"),
    c_float(66.5),
    c_int(14)
)

# matt = goLib.NewPersonTestStructAsJSON(
#     "matt",
#     68.0,
#     15
# )

print(dowland)
# print("matt: " + matt)