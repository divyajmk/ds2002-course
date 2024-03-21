#!/bin/bash 

# Echo the exit status 
date 
echo $?

# Or nullify the exit status and pass it to nothing 
date 
echo $? > /dev/null
