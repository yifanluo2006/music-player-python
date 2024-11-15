# User Documentation

## Introduction

Our Music Player project will be coded using Python with the Tkinter library to create a graphical user interface (GUI). We will be coding together during classes with the VS Code Live Share which allows people to collaborate in real time with one project. After we are done with each class, we will commit our changes to GitHub. As the project develops, we might split into different branches and work on separate features. We will complete our planning, track our progress, and save and commit code on GitHub. GitHub will be the centre of our project, with a repository to store code and track commits, and a Project to plan and schedule.

## Daily Log

https://docs.google.com/spreadsheets/d/1bNXFvRExQ5VKGVNFsL_oDoNSH_yp29qRXxQ70lwLvQs/edit?usp=sharing

## Installation

### Environment

The Python version we used is Python 3.12.4
The following dependencies are required:

- tkinter
- sklearn
- numpy

### Install

Run the following code in your console to install the required dependencies:
python -m pip install --upgrade pip
pip install numpy scikit-learn tkinter

## Running

Run the project in main, specifically the main.py file
Stop the run by closing the tkinter window or deleting the console
Note that multi threading is involved for random event generation. Therefore, the program won't stop immediately once the window is cloded

## Use

### Login

The login screen consists of a text box to username and a textbox to input the password. Once a correct username and password is imported, press confirm to login.
If you wish to create a new user, simply press the new user button and a window will appear below prompting you to create a new profile. Put in the desired username and password and a new user is created, which can be logged in right after with the original login screen.

### User Interface

On the left side, there is a bar that displays the searching, section tabs, playlists, and various other functions. On the right side, the individual songs are displayed

On top of the left side is the use name. Below is the search bar, simply type in a query and we will find the best match through fuzzy logic. Your query can be matched with title, artist, genre, or meta data. There is also a search history available with search

The For You tab is a recommendation based on your specific taste for music.

The browse tab displays the most popular and trending songs as well as all the songs in this music player system.

The library displays the song that you own, including all songs in your playlists.

Under playlsts, are all your playlists. You can add a new playlist by pressing the Add Playlist button which will prompt you to add a new playlist.

On the right side, you can add a song to a library/playlist, by selecting the library/playlist on the drop down menu and clicking ADD TO:

### Admin Interface

By inputting admin as the username, and adminpassword as the password, you are able to login as an administrator.

As an administrator, you are able to check system, manual, and random event logs, with advanced filtering tools to filter the desired types of logs. The filtering tool is similar to a search function, that can find the required type of log.

The administrator can also add a new song to the system or remove a song from the system. To do this, simply press these buttons and follow the prompts and instructions.

## Credits

This project is a collaboration between Yifan and Jaden, with Yifan working on backend functionality and Jaden working on GUI

## Tests

The tests are stored in the tests directory, and automated testing is integrated each time the code is pushed to Github.
