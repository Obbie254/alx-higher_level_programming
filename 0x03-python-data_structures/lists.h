#ifndef LISTS_H
#define LISTS_H

def print_list_integer(my_list=[]):
def element_at(my_list, idx):
def replace_in_list(my_list, idx, element):
def print_reversed_list_integer(my_list=[]):
def new_in_list(my_list, idx, element):
def no_c(my_string):
def print_matrix_integer(matrix=[[]]):
def add_tuple(tuple_a=(), tuple_b=()):


#include <stdio.h>
#include <stdlib.h>

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 * for Holberton project
 */
typedef struct listint_s
{
		int n;
			struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int n);
void free_listint(listint_t *head);
int is_palindrome(listint_t **head);

#endif
