#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
int main(int argc, char *argv[])
{
	printf("We Are in exe2.c\n");
	printf("HEllo World\n");
	printf("PID of exe2.c is: %d\n", getpid());
	printf("End of exe2.c\n");
	return (0);
}
