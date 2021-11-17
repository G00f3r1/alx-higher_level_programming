#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: the new node to be added
 * @number: the value of the new node
 * Return: the new linked list
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;

	current = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL)
		*head = new;
	else if (current == NULL)
	{
		new->next = current->next;
		current->next = new;
	}
	else if (current->n > number)
	{
		new->next = current;
		*head = new;
	}
	else
	{
		while (current->next != NULL)
		{
			if ((current->n < number && current->next->n >= number))
			{
				new->next = current->next;
				current->next = new;
			}
			current = current->next;
		}
		if (current->n < number && current->next == NULL)
		{
			current->next = new;
		}
	}
	return (new);
}
