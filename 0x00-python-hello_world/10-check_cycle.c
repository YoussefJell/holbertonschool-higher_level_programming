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

	if (list == NULL || list->next == NULL)
		return (0);

	ptr = list;
	holder = list;

	while (holder && holder->next)
	{
		ptr = ptr->next;
		holder = holder->next->next;

		if (ptr == holder)
			return (1);
	}
	return (0);
}
