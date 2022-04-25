#include "lists.h"
/**
 * check_cycle - checks if cycle exists
 *
 * @list: linked list input
 * Return: 1 if cycle exists, 0 if cycle doesn't exist
 */
int check_cycle(listint_t *list)
{
	listint_t *ptr;
	listint_t *holder;

	ptr = list;
	holder = list;

	while (ptr->next != NULL)
	{
		if (ptr->next == holder)
			return (1);
		ptr = ptr->next;
	}
	return (0);
}
