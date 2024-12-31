#!/bin/bash

echo 'Fibonacci(n)';

read -p 'Please enter a number: ' n;

if((n < 0))
then
echo 'Can not calculate fibonacci of a negative number';
exit
fi

fibonacciNumbers[0]=0;
fibonacciNumbers[1]=1;

for i in $(seq 2 $n)
do
let fibonacciNumbers[i]=fibonacciNumbers[i-1]+fibonacciNumbers[i-2];
done

#Print them all
echo ${fibonacciNumbers[@]};
