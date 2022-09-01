#include "lists.h"
#include <stdio.h>

/** 
 * print_dlistint - prints elements all elements of the list
 * @h: pointer to the list
 * Return: number of nodes
*/
size_t print_dlistint(const dlistint_t *h)
{
    size_t i;

    for (i = 0; h != NULL; i++)
    {
        printf("%dn", h->n);
        h = h->next;
    }
    return(i);
}
