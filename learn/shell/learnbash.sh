#!/usr/bin/env bash

echo Hello world!

echo "This is the first line"; echo "This is the second line"

Variable="Some string"
Variable = "Some string"

echo $Variable
echo "$Variable"
echo '$Variable'

echo ${Variable}
echo ${Variable/Some/A}

PACKAGES=(
    git
)

CASKS=(
    alfred3
    appcleaner
    calibre
    docker
    disk-inventory-x
    dropbox
    emacs
    expressvpn
    firefox-developer-edition
    flycut
    github
    google-chrome
    inna
    istat-menus
    iterm2
    logitech-options
    karabiner-elements
    macvim
    neteasemusic
    uu-booster
    qbittorrent
    slack
    squirrel
    spectacle
    telegram
    visual-studio-code
)


Length=7
echo ${Variable:0:Length}
echo ${Variable: -5}

echo ${#Variable}
array0=(one two three four five six)

echo $CASKS
echo ${CASKS[0]}
echo "${CASKS[@]}"
echo "${#CASKS[@]}"
echo "${#CASKS[2]}"

for i in "${CASKS[@]}"; do
    echo "$i"
done

echo {1..11}

echo "Last program's return value: $?"
echo "Script's PID: $$"
echo "Number of arguments passed to script: $#"
echo "All arguments passed to script: $@"
echo "Script's arguments separated into different variables: $1 $2..."


echo "I'm in $(pwd) ${PWD}" # execs `pwd` and interpolates output
echo "I'm in $PWD" # interpolates the variable

clear

echo "What's your name?"
read Name
echo Hello, $Name!

if [ $Name == $USER ]; then
    echo "Your name is your username"
else
    echo "Your name isn't your username"
fi
