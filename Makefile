PROJECT=sais
PLIBNAME=lib$(PROJECT)
PVER=2.7.1
PSOVER=2
UNAME_S := $(shell uname -s)

ifeq ($(UNAME_S),Darwin)
  PLIBSHARED=$(PLIBNAME).$(PVER).dylib
else ifeq ($(OS),Windows_NT)
  PLIBSTATIC=$(PROJECT).a
  PLIBSHARED=$(PLIBNAME)-$(PVER).dll
else
  PLIBSTATIC=$(PLIBNAME).a
  PLIBSHARED=$(PLIBNAME).so.$(PSOVER)
endif
PLIBS=$(PLIBSTATIC) $(PLIBSHARED)
CC=gcc
CFLAGS?=-Wall -O2 -fopenmp
LDFLAGS?=-lm -fopenmp
AR?=ar
INSTALL?=install
RM?=rm -f
RMD?=$(RM) -r
PREFIX?=/usr/local
SRCS=libsais/src
DOCS?=share/doc/$(PLIBNAME)
LIBS?=lib
INCLUDES?=include
MANS?=man/man1

all: $(PLIBS)

$(SRCS)/libsais.o: $(SRCS)/libsais.c
	$(CC) $(CFLAGS) -c -o $@ $^

$(SRCS)/libsais16.o: $(SRCS)/libsais16.c
	$(CC) $(CFLAGS) -c -o $@ $^

$(SRCS)/libsais64.o: $(SRCS)/libsais64.c
	$(CC) $(CFLAGS) -c -o $@ $^

$(PLIBSTATIC): $(SRCS)/libsais.o $(SRCS)/libsais16.o $(SRCS)/libsais64.o
	$(AR) rcs $@ $^

ifeq ($(UNAME_S),Darwin)
$(PLIBSHARED): $(SRCS)/libsais.o $(SRCS)/libsais16.o $(SRCS)/libsais64.o
	$(CC) $(CFLAGS) -dynamiclib -install_name $(PLIBSHARED) -current_version $(PVER) -compatibility_version $(PSOVER) -o $@ $^
else
$(PLIBSHARED): $(SRCS)/libsais.o $(SRCS)/libsais16.o $(SRCS)/libsais64.o
	$(CC) $(CFLAGS) -shared -Wl,-soname,$@ $^ -o $@
endif

install:
	$(INSTALL) -d $(PREFIX)/$(LIBS)
	$(INSTALL) -d $(PREFIX)/$(INCLUDES)
	$(INSTALL) -d $(PREFIX)/$(MANS)
	$(INSTALL) -d $(PREFIX)/$(DOCS)
	$(INSTALL) -m 0644 $(PLIBS) $(PREFIX)/$(LIBS)
	$(INSTALL) -m 0644 $(SRCS)/libsais.h $(SRCS)/libsais16.h $(SRCS)/libsais64.h $(PREFIX)/$(INCLUDES)
	$(INSTALL) -m 0644 libsais/CHANGES libsais/LICENSE libsais/README.md libsais/VERSION $(PREFIX)/$(DOCS)

uninstall:
	$(RM) $(addprefix $(PREFIX)/$(LIBS)/,$(notdir $(PLIBS)))
	$(RM) $(PREFIX)/$(INCLUDES)/libsais.h $(PREFIX)/$(INCLUDES)/libsais16.h $(PREFIX)/$(INCLUDES)/libsais64.h
	$(RM) $(PREFIX)/$(DOCS)/CHANGES $(PREFIX)/$(DOCS)/LICENSE $(PREFIX)/$(DOCS)/README.md $(PREFIX)/$(DOCS)/VERSION
	$(RMD) $(PREFIX)/$(DOCS)

clean:
	$(RM) $(SRCS)/libsais.o $(SRCS)/libsais16.o $(SRCS)/libsais64.o $(PLIBS)
	
