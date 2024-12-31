#!/bin/bash

echo 'EvenOrOdd(n)'

read -p 'Please enter a number: ' n;

if (( n % 2 == 0)); then
echo "The number $n is even";
else
echo "The number $n is odd";
fi
