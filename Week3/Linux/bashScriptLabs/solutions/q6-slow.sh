#!/bin/bash

echo 'Prime(n)'

read -p 'Please enter a number: ' n;

if(( n < 1 )); then
echo 'Please insert a positive number';
exit;
fi

for i in $(seq 2 $[$n-1]); do
if (( n % i == 0 )); then
echo "The number $n is not prime";
echo "First divisor: $i";
exit;
fi
done

echo "The number $n is prime";
