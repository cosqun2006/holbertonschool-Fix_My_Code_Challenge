#include <stdlib.h>
#include "lists.h"

/**
 * delete_dnodeint_at_index - Deletes the node at index index of a dlistint_t list
 * @head: Pointer to the head pointer of the list
 * @index: Index of the node that should be deleted
 *
 * Return: 1 if it succeeded, -1 if it failed
 */
int delete_dnodeint_at_index(dlistint_t **head, unsigned int index)
{
	dlistint_t *saved_head;
	dlistint_t *p1;
	unsigned int i;

	if (*head == NULL)
		return (-1);

	saved_head = *head;
	p1 = *head;
	i = 0;

	while (p1 != NULL && i < index)
	{
		p1 = p1->next;
		i++;
	}

	if (p1 == NULL)
		return (-1);

	if (index == 0)
	{
		*head = p1->next;
		if (*head != NULL)
			(*head)->prev = NULL;
		free(p1);
		return (1);
	}

	p1->prev->next = p1->next;
	if (p1->next != NULL)
		p1->next->prev = p1->prev;

	free(p1);
	return (1);
}
