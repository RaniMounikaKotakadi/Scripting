#!/bin/sh

#This funtion will tell you what is the given variable type
TellVariableType() {
    echo $n
    return type($n)
}

#Tried if we can do the same as in python. There are not types in bash. Variables in Bash are untyped. how ever you can assign any number/character/string/array to any variable.
