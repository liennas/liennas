all:
        gcc Hello.c -o hello.exe
install:
        gcc Hello.c -o $(prefix)/hello.exe
