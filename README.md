# Probius

This is a forked version of the Nexus School House HotS Discord bot. It is being re-worked to be server agnostic, containerized ,and easily configurable.

Call in Discord with [hero/modifier], where modifier is hotkey or talent tier. Data is pulled from HotS wiki. 

Written in Python 3.5.3

# Installation and Setup

The discord bot should be run in a Virtual Environment ( venv ) to prevent collisions on a local machine or server. 

1. Setup the Viirtual Environment
    > python -m venv venv
1. Install the required modules 
    > python -m pip install -r requirements.txt 
1. Run the main bot function. 
    > python ./src/application.py



# File description

probius: The main file that calls all the other files

aliases: Spellcheck and alternate names for heroes

trimBrackets: Trims < from text

printFunctions: The functions that output the things to print

heroPage: The function that imports the hero pages

emojis: Emojis

miscFunctions: Edge cases and help message

getDiscordToken: The token is in an untracked file because this is a public Github repo

elitesparkleGuide: Hero guides

downloadHero: Downloads a hero page. Not called by main loop, must be run after each patch.

Example usage:
![bilde](https://user-images.githubusercontent.com/49531523/109698466-b7da2a00-7b8f-11eb-8b5a-d20a3daf22a3.png)
