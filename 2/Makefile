# change to your Gecode installation path here:
GECODE_HOME=/usr/local/include
# Assumes standard installation of Qt via apt-get
QT_LIB = /usr/lib/x86_64-linux-gnu
QT_INCL = /usr/include/qt4
QT_LINKS = -lQtGui -lQtCore

GECODE_LINKS=-lgecodeflatzinc -lgecodedriver -lgecodegist -lgecodesearch -lgecodeminimodel -lgecodeset -lgecodefloat -lgecodeint -lgecodekernel -lgecodesupport

LINKER=g++
COMPILER=g++
CXXFLAGS=-std=c++0x

open-shop: open-shop.cpp
	${COMPILER} ${CXXFLAGS} -I${GECODE_HOME} -I/usr/lib/x86_64-linux-gnu -I/usr/share/qt4/mkspecs/linux-g++-64 -I${QT_INCL}/QtCore -I${QT_INCL}/QtGui -I/usr/include/qt4 -I. -c -o $@.o $@.cpp
	${LINKER} -o $@ $@.o -L${GECODE_HOME} ${QT_LINKS} ${GECODE_LINKS} -lpthread 

clean:
	rm -rf *.o 

# -Wl,-rpath,${GECODE_HOME} 
