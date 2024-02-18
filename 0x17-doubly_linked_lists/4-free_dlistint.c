#include "lists.h"

/**
 * free_dlistint - free a doubly linked list
 * @head:the head
 * Return:nothing
 */

void free_dlistint(dlistint_t *head)
{
	dlistint_t *current, *Next;

	current = head;
	while (current != NULL)
	{
	Next = current->next;
	free(current);
	current = Next;
	}

}
