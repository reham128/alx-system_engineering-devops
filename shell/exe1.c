#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
int main(int argc, char *argv[])
{
	printf("PID of exe1.c is %d\n", getpid());
	char *args[] = {"Hello", "Reham", "World", NULL};
	execv("./exe2", args);
	printf("Back to exe1.c\n");
	return (0);
}
