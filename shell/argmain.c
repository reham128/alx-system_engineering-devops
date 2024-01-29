#include <stdio.h>
#include <stdlib.h>
int main(int ac, char **av)
{
	int i, sum = 0;

	printf("args is = %d\n", ac);
	for (i = 0; i < ac; i++)
	{
		printf("argv[%d] = %s\n", i, av[i]);
		sum = sum + atoi(av[i]);
	}
	printf("sum = %d\n", sum);
	return (0);
}
