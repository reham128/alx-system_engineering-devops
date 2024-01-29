#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(void)
{
	char *str = "This is the string to be devide";
	char *src = malloc(sizeof(char) * strlen(str));
	char delim[6] = " ";
	char *truncs;
	int i;

	strcpy(src, str);
	truncs = strtok(src, delim);
	while (truncs != NULL)
	{
		printf("%s\n", truncs);
		truncs = strtok(NULL, delim);
	}
	for (i = 0; i < strlen(str); i++)
	{
		if (src[i] == '\0')
		{
			printf("\\0");
		}
		else
		{
			printf("%C", src[i]);
		}
	}
	printf("\n");
	return (0);
}
