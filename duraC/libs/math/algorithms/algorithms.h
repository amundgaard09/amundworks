/* Algorithms prototype file - DURENDAL ENGINEERING ALGORITHMS LIBRARY - V.1*/

#include <stdint.h>
#include "../../types/dl_list/dllist.h"

#ifndef ALGORITHMS.H
#define ALGORITHMS.H

bool is_prime(int Number);
DLList prime_factorize(int Number);
uint64_t factorial(int I);
uint64_t fibonacci(int I);

#endif