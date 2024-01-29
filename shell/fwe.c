#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
int main(void)
{
	pid_t child_pid;
	int i, status;
	char *argv[] = {"ls", "-l", "/tmp", NULL};

	for (i = 1; i <=2; i++)
	{
		child_pid = fork();
		if (child_pid == -1)
		{
			perror("ERROR:");
			return (1);
		}
	}
	if (child_pid == 0)
	{
		execve("/bin/ls", argv, NULL);
		perror("Error:");
		return (1);
	}
	else
	{
		wait(&status);
	}
}
