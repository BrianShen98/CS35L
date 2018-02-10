#!/bin/bash

echo -n "Enter a number between 1 and 3 inclusive > "
read character
if [ "$character" = "1" ]; then
    echo "You entered one."
else
    if [ "$character" = "2" ]; then
        echo "You entered two."
    else
        if [ "$character" = "3" ]; then
            echo "You entered three."
        else
            echo "You did not enter a number"
            echo "between 1 and 3."
        fi
    fi
fi