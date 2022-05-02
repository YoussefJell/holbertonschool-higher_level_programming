#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
 * is_palindrome - checks if list is palindrome
 * @head: head node
 * Return: 1 if palindrome 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *start = NULL, *end = NULL;
	unsigned int i = 0, len = 0, len_list = 0;

	if (head == NULL)
		return (0);
	if (*head == NULL)
		return (1);

	start = *head;
	len = list_len(start);
	len_list = len - 2;
	end = *head;

	for (; i < len; i = i + 2)
	{
		if (start[i].n != end[len_list].n)
			return (0);

		len_list = len_list - 2;
	}

	return (1);
}
/**
 * list_len - list count
 * @head: list head
 *
 * Return: count of elems
 */
size_t list_len(const listint_t *head)
{
	int len = 0;

	while (head != NULL)
	{
		++len;
		head = head->next;
	}

	return (len * 2);
}
