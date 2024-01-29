#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
int main()
{
	fork();
	fork();
	printf("\nThis is Reham Project\nPID = %d\n", getpid());
       return (0);
}       
