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
	listint_t *ojo2;

	if (!list || list->next == NULL || list->next->next == NULL)
		return (0);
	ojo2 = list->next->next;
	while (ojo2->next->next)
	{
		list = list->next;
		ojo2 = ojo2->next->next;
		if (ojo2 == list)
			return (1);
	}
	return (0);
}