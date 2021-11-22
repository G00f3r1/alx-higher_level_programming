#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: the linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
void reverse(listint_t **head_ref);


int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	listint_t *prev = NULL;
	listint_t *next = NULL;
	listint_t *new_head = NULL;

	listint_t *start = *head;
	listint_t *end = NULL;
/*	int count = 0;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	new_head = prev;
	end = new_head;
*/

	reverse(&head);
	end = head;
	while (start->next != NULL && end->next != NULL)
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

void reverse(listint_t **head_ref)
{
    struct Node* prev = NULL;
    struct Node* current = *head_ref;
    struct Node* next = NULL;
    while (current != NULL) {
        // Store next
        next = current->next;
 
        // Reverse current node's pointer
        current->next = prev;
 
        // Move pointers one position ahead.
        prev = current;
        current = next;
    }
    *head_ref = prev;
}
