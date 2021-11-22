#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	listint_t *prev = NULL;
	listint_t *next = NULL;
	listint_t *new_head = NULL;

	listint_t *start = *head;
	listint_t *end = NULL;
	int count = 0;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	new_head = prev;
	end = new_head;


	while(start->next != NULL && end->next != NULL)
	{
		if (start->n == end->n)
		{
			start = start->next;
			end = end->next;
		}
		else
		{
			return (0);
		}
		count++;
	}
	printf("count = %i\n", count);
	return (1);
}


