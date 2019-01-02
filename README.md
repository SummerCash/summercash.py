# summercash.py
Python 3 go-summercash API wrapper.

# Building
First, `cd src/`
<br>
Before doing anything you must compile the shared library (.so) and header file in C. To do this use `make go_lib`
<br>
To use the shared library (.so) in C, compile `c_src` with `make c_api`. Run it with `cd build && ./c_api.out`
