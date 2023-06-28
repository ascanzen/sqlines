BINFILE = sqlline

ifdef VERBOSE
	Q =
	E = @true 
else
	Q = @
	E = @echo 
endif

CFILES := $(shell find sqlparser -mindepth 1 -maxdepth 4 -name "*.c")
CXXFILES := $(shell find sqlparser -mindepth 1 -maxdepth 4 -name "*.cpp")

INFILES := $(CFILES) $(CXXFILES)

OBJFILES := $(CXXFILES:sqlparser/%.cpp=%) $(CFILES:sqlparser/%.c=%)
DEPFILES := $(CXXFILES:sqlparser/%.cpp=%) $(CFILES:sqlparser/%.c=%)
OFILES := $(OBJFILES:%=obj/%.o)


COMMONFLAGS := -Wall -Wextra -pedantic -O3 
DEFINES := -fpic -Wl,-rpath=.
INCLUDE := -I. 
LDFLAGS := -L/usr/libx86_64-linux-gnu/  -L/usr/lib/x86_64-linux-gnu -L/usr/local/lib -L.
LIBS	:= -lcurl 

ifdef DEBUG
	COMMONFLAGS := $(COMMONFLAGS) -g
endif
CFLAGS := $(COMMONFLAGS) --std=c99 $(DEFINES) $(INCLUDE)
CXXFLAGS := $(COMMONFLAGS) --std=c++0x $(DEFINES) $(INCLUDE)
DEPDIR := deps

all: $(BINFILE)
ifeq ($(MAKECMDGOALS),)
-include Makefile.dep
endif
ifneq ($(filter-out clean, $(MAKECMDGOALS)),)
-include Makefile.dep
endif

CC = gcc
CXX = g++


-include Makefile.local

.PHONY: clean all depend
.SUFFIXES:
obj/%.o: sqlparser/%.c
	$(E)C-compiling $<
	$(Q)if [ ! -d `dirname $@` ]; then mkdir -p `dirname $@`; fi
	$(Q)$(CC) -o $@ -c $< $(CFLAGS)
obj/%.o: sqlparser/%.cpp
	$(E)C++-compiling $<
	$(Q)if [ ! -d `dirname $@` ]; then mkdir -p `dirname $@`; fi
	$(Q)$(CXX) -o $@ -c $< $(CXXFLAGS)
Makefile.dep: $(CFILES) $(CXXFILES)
	$(E)Depend
	$(Q)for i in $(^); do $(CXX) $(CXXFLAGS) -MM "$${i}" -MT obj/`basename $${i%.*}`.o; done > $@


$(BINFILE): $(OFILES)
	$(E)Linking $@
	$(Q)$(CXX) -o $@ $(OFILES) $(LDFLAGS) $(LIBS)
clean:
	$(E)Removing files
	$(Q)rm -f $(BINFILE) obj/* Makefile.dep

run:
	@make DEBUG=true && ./sqlline

python:
	swig -python -c++ -o ./sqlparser/sqlines_wrap.cpp ./sqlparser/sqlines.i
	python3.9 setup.py build_ext --inplace