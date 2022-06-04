#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

char name[12];
int sub_main(){
  char buffer[420];
  int characters_read;
  printf("Feed Me A Stray String:\n");
  characters_read = read(0, buffer, 1000);

  return 0;
}

int main() {
	char buf[0x400] = {0};
	sub_main();
}

void call_me() {
	printf("I am called!\n");
}

void can_you_call_me() {
  call_me();
}
