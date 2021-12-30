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

This is an environmental file that hold the discord token, and other configs.
For security reasons, this is not added to the repository. You will need to create your own. 

1. In the parent directory, create a file called `.env`.
2. Inside this file add these lines. 
```
# .env
DISCORD_TOKEN={Your_Token_No_Brackets}
HEROES_PROFILE_TOKEN=={Your_Token_No_Brackets}
API_URL=https://api.heroesprofile.com/api
OPEN_API_URL=https://api.heroesprofile.com/openApi
```


# Directory Structure

1. The main app is stored in the `app` directory.
3. `builds` currently contains the .txt files for the different hero build urls.
4. `dockerfiles` contains the different docker files I used.
   1. Planning for an rdbms in order to help make storing the data easier, hence `_sql` file 
   2. `dockerfiles/dockerfile` will create a "base" image to use for python 3.7. 
      1. This is a massive PITA, so thats why the base exists. 
   3. `./dockerfile` is the main file you will build off once the base image exists.
      1. Includes SQL Server tools you can comment this out if you wish.
         1. Nothing uses it and the files were intended to be a template for my other project. 
      2. This pulls the base image, and then runs the app. 
5. 

```

.
└── probius/
    ├── app/
    │   ├── data
    │   ├── functions
    │   ├── models
    │   └── application.py
    ├── builds
    ├── dockerfiles
    ├── emojis
    └── maps
```
