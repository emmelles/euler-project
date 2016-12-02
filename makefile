CFLAGS= -Wall -g
LFLAGS= -Wall -g
CXX=g++

PROGRAMS=main

all: $(PROGRAMS)
	@echo "DONE"

obj=main.o
main: $(obj)
	$(CXX) $(LFLAGS) $(obj) -o main

main.o: main.cc 
	$(CXX) $(CFLAGS) -c main.cc

#%.o: %.cc %.h
#	$(CXX) $(CFLAGS) -c $<

clean:
	rm -f *.o *.mod $(PROGRAMS)

realclean: clean
	rm -f *~
