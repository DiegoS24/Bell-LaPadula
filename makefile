temp: main.o user.o object.o
	g++ user.cpp object.cpp main.cpp -o temp

main.o: main.cpp user.cpp object.cpp
	g++ -c main.cpp

user.o: user.hpp user.cpp
	g++ -c user.cpp

object.o: object.hpp object.cpp
	g++ -c object.cpp

clean: 
	rm *.o
