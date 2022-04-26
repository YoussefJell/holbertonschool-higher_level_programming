#include "lists.h"
/**
 * insert_node - inserts node in a sorted list
 * @head: head of list
 * @number: number data
 * Return: PTR to new node
 */
listint_t *insert_node(listint_t **head, int number)
{

	listint_t *newNode;
	listint_t *ptr;

	if (head == NULL || (*head)->next == NULL)
		return (NULL);

	newNode = malloc(sizeof(listint_t));
	if (newNode == NULL)
		return (NULL);
	newNode->n = number;
	newNode->next = NULL;

	ptr = *head;

	while (number > ptr->next->n && ptr->next != NULL)
	{
		ptr = ptr->next;
	}
	newNode->next = ptr->next;
	ptr->next = newNode;

	return (newNode);
}
