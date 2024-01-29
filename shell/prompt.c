#include <stdio.h>
#include <stdlib.h>
/**
 * to show prompet with getline
 * don't use malloc because getline have realloc
 * don't have to printf buffer size
 * */
int main(void)
{
	size_t n = 10;
	char *buf = NULL;

	printf("$ ");
	getline(&buf, &n, stdin);
	printf("%s", buf);
	printf("Buffer Size: %ld\n", n);

	free(buf);
	return (0);
}
