#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * There is a cycle in a linked list if there is some node in the
 * list that can be reached again by continuously following the next pointer.
 * @list: the singly linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *first;
	listint_t *second;

	first = list;
	second = list->next;

	if (list == NULL)
		return (0);

	while (first != NULL && second->next != NULL && second != NULL)
	{
		if (first == second)
			return (1);
		first = first->next;
		second = second->next->next;
	}
	return (0);
}
