#!/bin/bash

read -p "Please enter a string: " str;

reversed=`echo $str | rev`;

if [ "$reversed" == "$str" ]; then
echo $reversed >> palindrome.txt
fi

