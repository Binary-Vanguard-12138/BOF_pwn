all: flag1 flag2

flag1: flag1.c
	gcc flag1.c -o flag1 -m32 -fno-stack-protector -g

flag2: flag2.c
	gcc flag2.c -o flag2 -m32 -fno-stack-protector -g

clean: clean_flag1 clean_flag2

clean_flag1:
	rm -f flag1

clean_flag2:
	rm -f flag2
