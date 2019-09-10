#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"
/**
 * check_cycle - check the code for Holberton School students.
 * @list:head
 * Return: 1 or 0.
 */
int check_cycle(listint_t *list)
{
	listint_t *ojo;

	if (!list)
		return (0);
	if (list->next == NULL)
		return (0);
	if (list->next->next == NULL)
		return (0);


	ojo = list->next->next;
	while (ojo->next->next)
	{
		list = list->next;
		ojo = ojo->next->next;
		if (ojo == list)
			return (1);
	}

	return (0);
}
