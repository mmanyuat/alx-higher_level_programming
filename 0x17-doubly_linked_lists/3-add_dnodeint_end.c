#include "lists.h"
#include <stdio.h>

/**
 * add_dnodeint_end - adds a node to end of a list
 * @head:the head of a list
 * @n:the data
 * Return:the address
 */

dlistint_t *add_dnodeint_end(dlistint_t **head, const int n)
{
	dlistint_t *new_node;
	dlistint_t *current;

	new_node = malloc(sizeof(dlistint_t));

	new_node->n = n;
	new_node->next = NULL;

	if (*head == NULL)
	{
	new_node->prev = NULL;
	*head = new_node;
	return (new_node);
	}

	current = *head;
	while (current->next != NULL)
	{
	current = current->next;
	}
	current->next = new_node;
	new_node->prev = current;
	return (new_node);
}
