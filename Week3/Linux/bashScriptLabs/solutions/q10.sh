#!/bin/bash

read -p 'Please enter 3 numbers: ' n1 n2 n3;

declare -a numbers=($n1 $n2 $n3);

max=-32796767
for number in "${numbers[@]}"; do
if (( number > max )); then
let max=number;
fi
done

echo "The max number is: $max";
