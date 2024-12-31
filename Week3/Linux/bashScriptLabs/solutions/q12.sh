#!/bin/bash

read -p "Please input ten numbers: " n1 n2 n3 n4 n5 n6 n7 n8 n9 n10;

declare -a numbers=($n1 $n2 $n3 $n4 $n5 $n6 $n7 $n8 $n9 $n10);

#Empty files
echo '' > even.txt;
echo '' > odd.txt;

for number in "${numbers[@]}"
do
if ((number % 2 == 0)); then
echo $number >> even.txt;
else
echo $number >> odd.txt
fi
done

