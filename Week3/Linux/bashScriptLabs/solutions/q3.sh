#!/bin/bash

function factorial {
n=$1;

if(( n < 0 ))
then
echo "Can not calculate factorial of a negative number."
exit;
fi

if(( n > 1 ))
then
last=$(factorial $[$n-1])
echo $((n * last))
else
echo 1
fi
}

echo 'Factorial(n)';
read -p 'Please enter a number: ' n;
echo "Factorial of $n:"

factorial $n;
