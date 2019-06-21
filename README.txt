Compiling C:
	gcc -c -fPIC main.c -o main.o
	gcc main.o -shared -o main.so

Compiling CPP:
	g++ -c -fPIC main.cpp -o main.o
	g++ main.o -shared -o main.so

Compiling Go:
	go build -o main.so -buildmode=c-shared main.go

Programming python:
	use numpy only
	use numba jit decorator
	use typing

	@jit(nopython=True)
	def adder(a: np.ndarray,b: np.ndarray):
		np.add(a,b)
	
	import ctypes
	external = ctypes.cdll.LoadLibrary('path/to/example.so')
	
	
Declare return types of C functions as ctypes assumes they are ints

	external.function_a.restype = c_float

ctypes does not accept most python native types dict, float

	value_a = c_types.c_float(value_a)

