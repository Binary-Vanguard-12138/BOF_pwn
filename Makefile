all: flag1 flag2

flag1:
	gcc flag1.c -o flag1 -m32 -fno-stack-protector

flag2:
	gcc flag2.c -o flag2 -m32 -fno-stack-protector
