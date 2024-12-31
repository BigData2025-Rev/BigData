#!/bin/bash

read -p "Please enter a string: " str;

reversed=`echo $str | rev`;

if [ "$reversed" == "$str" ]; then
echo "The word $str is palindrome";
else
echo "The word $str is not palindrome";
fi
