#!/bin/bash

echo '***Basic prints***'

#Current home directory
echo ~

#Current username
whoami

#Today's date is
echo $(date +'%m/%d/%Y');

#Number of users
who | wc -l;

