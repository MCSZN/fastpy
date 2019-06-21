cd C;
echo "Compiling";
gcc -c -fPIC main.c -o main.o;
gcc main.o -shared -o main.so;
cd ..;
echo "Launching Python benchmark";
python3 bench.py;
echo "Launching Julia benchmark";
julia bench.jl;