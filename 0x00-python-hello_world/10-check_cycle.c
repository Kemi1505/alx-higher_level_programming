#include "lists.h"

/**
 * check_cycle - testing for loop
 * @list: first on the list
 * Description - testing for loop
 * Return: 1 for success
 */

int check_cycle(listint_t *list)
{
	listint_t *present, *previous;

	if (!list)
	{
		return (0);
	}
	present = list;
	previous = list->next;
	while (previous && present && previous->next)
	{
		if (present == previous)
		{
			return (1);
		}
		present = present->next;
		previous = previous->next->next;
	}
	return (0);
}
