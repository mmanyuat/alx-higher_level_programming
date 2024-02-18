#include "lists.h"
#include <stdio.h>

/**
 * dlistint_len - function to find the length of linked list
 * @h:pointer to the head
 * Return: number of the nodes
 */

size_t dlistint_len(const dlistint_t *h)
{
	size_t count = 0;

	while (h != NULL)
	{
	h = h->next;
	count++;
	}
	return (count);
}

