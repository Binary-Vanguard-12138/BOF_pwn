#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

char name[12];
typedef struct node_t {
        int x;
        char y;
        float z;
} weird_node;

void call_me() {
	printf("I am called!\n");
}

void unsafe() {
  int characters_read;
  int some_other_value = 0xFFFF;
  int* protector = (int *)malloc(sizeof(weird_node)*11);
  char buffer[10];
  printf("Give me some strings (Mind your values!):\n");
  characters_read = read(0, buffer, 1000);
  if (*(&protector + some_other_value) == 0xdeadbeef) {
    call_me();
  }
}

int main(){
  char* args[] = {"xdg-open","img.jpg",NULL};
  extern char** environ;
  int pid = fork();
  if (pid == 0) {
        execve("/usr/bin/xdg-open",args,environ);
  }
  printf("%d\n",PTRACE_TRACEME);
  unsafe();
  return 0;
}
