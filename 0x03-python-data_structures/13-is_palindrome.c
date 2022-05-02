#include "lists.h"
/**
 * is_palindrome - checks if list is palindrome
 * @head: head node
 * Return: 1 if palindrome 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *fast = *head, *slow = *head;
	listint_t *mid, *beforeSlow, *split;
	int res;

	if (head == NULL)
		return (0);
	if (*head == NULL)
		return (1);
	while (fast && fast->next)
	{
		beforeSlow = slow;
		slow = slow->next;
		fast = fast->next->next;
	}
	if (fast != NULL)
	{
		mid = slow;
		slow = slow->next;
	}

	split = slow;
	beforeSlow->next = NULL;

	reverseList(&split);
	res = compareLists(head, split);
	reverseList(&split);

	if (mid != NULL)
	{
		beforeSlow->next = mid;
		mid->next = split;
	}
	else
		beforeSlow->next = split;

	return (res);
}
/**
 * reverseList - reverses list
 * @split: 2nd half
 * Return: void
 */
void reverseList(listint_t **split)
{
	listint_t *prev = NULL;
	listint_t *current = *split;
	listint_t *next;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*split = prev;
}
/**
 * compareLists - compare
 *
 * @head: head of list
 * @split: 2nd half
 * Return: 1 if yes 0 if not
 */
int compareLists(listint_t **head, listint_t *split)
{
	listint_t *temp1 = *head;
	listint_t *temp2 = split;

	while (temp1 && temp2)
	{
		if (temp1->n == temp2->n)
		{
			temp1 = temp1->next;
			temp2 = temp2->next;
		}
		else
			return (0);
	}
	if (temp1 == NULL && temp2 == NULL)
		return (1);
	return (0);
}
