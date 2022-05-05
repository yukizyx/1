# My First Roguelike

*A python project of an old-fashion roguelike game, including source code and game descriptions.*

- Category: Python

- Keyword: 
  - Python objected-oriented programming
  - Visualization
  - Game design
  - File manipulation
- Date: January, 2022

## Table of Contents

- [My First Roguelike](#my-first-roguelike)
  * [Table of Contents](#table-of-contents)
  * [Description](#description)
  * [Usage](#usage)
  * [Operations](#operations)
    + [Character info](#character-info)
    + [Movements](#movements)
    + [In-game message log](#in-game-message-log)
    + [Items and inventory](#items-and-inventory)
    + [Next level](#next-level)
  * [Reference](#reference)

## Description

This project is an implementation of a traditional roguelike game with elements such as generated levels of dungeon, turn-based gameplay, randomly placed items and permanent death of the player.
It also allows auto save when exiting a unfinished game, but only one game load is allowed.

The appearance of the game is not traditional, color schemes are used instead of the characters to make the entire game look nicer.

The current design and implementation is simple, but allows further modifications and additional features.

## Usage

- You may need `python 3` and `python-tcod` install in your environment.

- To install `python-tcod`, run the following from a Windows command line:
```
> pip install tcod
```

## Operations

### Character info

- To check the character information: press `C`

### Movements

- To play with 4 directions: press direction keys to move
- To play with 8 directions: use the numpad, press `2`, `4`, `6`, `8` to move along the axis, press `1`, `3`, `7`, `9` to move along the diagonals.

### In-game message log

- To see a log of all past messages: press `V`

### Items and inventory

- To pick up items: press `G`
- To drop items: press `H`
- To open inventory: press `I`
- To select and index inventory: press `A-Z` (press `B` to select the second item in the inventory)

### Next level

- To go to the next floor: press `>` on the `>` tile in the map


## Reference

[Roguelike Tutorials](http://rogueliketutorials.com/tutorials/tcod/v2/)

