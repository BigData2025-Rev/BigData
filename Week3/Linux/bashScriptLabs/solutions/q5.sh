#!/bin/bash

read -p "Please input ten numbers: " n1 n2 n3 n4 n5 n6 n7 n8 n9 n10;

declare -a numbers=($n1 $n2 $n3 $n4 $n5 $n6 $n7 $n8 $n9 $n10);

for number in "${numbers[@]}"
do
if ((number < 0)); then
let negatives++;
else
let positives++;
fi
done

echo "Positives: $positives";
echo "Negatives: $negatives";
