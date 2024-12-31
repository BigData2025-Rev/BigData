#!/bin/bash

read -p "Insert a score from 0 to 100 for Math, Science and English: " math english science;

if ((math < 0 || math > 100 || english < 0 || english > 100 || science < 0 || science > 100 )); then
echo 'Please input scores from 0 to a 100';
fi

sum=$((math + english + science));
avg=$((sum/3));

if((avg >= 90 && avg <= 100)); then
echo "Your avg is A ($avg)";
else if((avg >= 80 && avg < 90)); then
echo "Your avg is B ($avg)";
else if((avg >= 70 && avg < 80)); then
echo "Your avg is C ($avg)";
else if((avg >= 60 && avg < 70)); then
echo "Your avg is D ($avg)";
else
echo "Your avg is F ($avg)";
fi
fi
fi
fi
