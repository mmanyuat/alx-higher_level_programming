#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - function to check for loop in linked list
 * @list:a pointer
 * Return:0 if no loop and 1 otherwise
 */

int check_cycle(listint_t *list)
{
	listint_t *once = list;
	listint_t *twice = list;

	while (once != NULL && twice != NULL && twice->next != NULL)
	{
	once = once->next;
	twice = twice->next->next;
	if (once == twice)
	{
	return (1);
	}
	}
	return (0);
}
