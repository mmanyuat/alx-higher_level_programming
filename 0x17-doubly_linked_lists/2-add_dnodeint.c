#include "lists.h"
#include <stdio.h>

/**
 * add_dnodeint - adding new node to the begining of list
 * @head:the head
 * @n:the data
 * Return:address of the linked list
 */

dlistint_t *add_dnodeint(dlistint_t **head, const int n)
{
	dlistint_t *new_node;

	new_node = malloc(sizeof(dlistint_t));

	if (new_node == NULL)
	{
	return (NULL);
	}

	new_node->n = n;
	new_node->prev = NULL;
	new_node->next = *head;
	if (*head != NULL)
	{
	(*head)->prev = new_node;
	}
	*head = new_node;
	return (new_node);

}
