# Pylon

A HotS Discord bot. Call in Discord with [hero/modifier], where modifier is hotkey or talent tier. Data is pulled from HotS wiki. 

This project was forked from https://github.com/Asddsa76/Probius , who did a fantastic amount of work that helped me learn more about discord bots.

# File description

1. **application**: The main file that calls all the other files
1. **aliases**: Spellcheck and alternate names for heroes
1. **trimBrackets**: Trims < from text
1. **printFunctions**: The functions that output the things to print
1. **heroPage**: The function that imports the hero pages
1. **emojis**: Emojis
1. **miscFunctions**: Edge cases and help message
1. **elitesparkleGuide**: Hero guides
1. **downloadHero**: Downloads a hero page. Not called by main loop, must be run after each patch.

# Config Files 

## .env 

This is an environmental file that hold the dicord token, instead of storing it in a file that gets added to the repo. 

1. in the parent directory, create a file called `.env`.
2. Inside this file add these lines. 
`# .env
DISCORD_TOKEN={Your_Token_No_Brackets}`


# Directory Structure

The main app is stored in the 'app' directory. 

```
.
.
└── probius/
    ├── app/
    │   ├── data
    │   ├── functions
    │   ├── models
    │   └── application.py
    ├── builds
    ├── emojis
    ├── heroConfig
    └── maps
```    

## Install

On linux 

> sudo apt-get install python3-venv 
> sudo apt-get install python3-pip
> sudo apt-get install unixodbc unixodbc-dev 

