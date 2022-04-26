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

	if ((*head) == NULL)
	{
		(*head) = malloc(sizeof(listint_t));
		if ((*head) == NULL)
			return (NULL);
		(*head)->n = number;
		(*head)->next = NULL;
		return (*head);
	}

	if (number < (*head)->n)
	{
		addNodeBegin(head, number);
		return (*head);
	}

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
/**
 * addNodeBegin - adding node to beginning
 * @head: head of node
 * @n: data of node
 * Return: address of new element or null
 */
listint_t *addNodeBegin(listint_t **head, const int n)
{
	listint_t *tmp;

	tmp = malloc(sizeof(listint_t));
	if (tmp == NULL)
		return (NULL);
	tmp->n = n;
	tmp->next = NULL;

	tmp->next = *head;
	*head = tmp;

	return (*head);
}
