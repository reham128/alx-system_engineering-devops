#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
/**
 * infinite_while - creates an infinite loop to make the program hang
 * Return: always 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
/**
 * main - entry point
 * Return: 0 for success
 */
int main(void)
{
	int a;
	pid_t zmb;

	for (a = 0; a < 5; a++)
	{
		zmb = fork();
		if (!zmb)
			return (0);
		printf("Zombie process created, PID: %d\n", zmb);
	}
	infinite_while();
	return (0);
}
