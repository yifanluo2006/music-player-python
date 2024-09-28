# Music Player

Our Music Player project will be coded using Python with the Tkinter library to create a graphical user interface (GUI). We will be coding together during classes with the VS Code Live Share which allows people to collaborate in real time with one project. After we are done with each class, we will commit our changes to GitHub. As the project develops, we might split into different branches and work on separate features. We will complete our planning, track our progress, and save and commit code on GitHub. GitHub will be the centre of our project, with a repository to store code and track commits, and a Project to plan and schedule.

# Daily Log

### Sept 24

Yifan

1. Developed a plan to complete the project
2. Completed weekly planner with: Goals, description, and specific checklist
3. Completed project description and overview
4. Created daily log spreadsheet and format of each log
5. Created and imported list of 200 songs

Jaden

1. Started User class and Song class
2. Started learning Python

### Sept 25

Yifan

1. Redesigned the class system
2. Created new gui.py, playlist.py, song.py, user.py, and main.py files
3. Created GUI, Playlist, Song, User class, and the main method

### Sept 26

**College Presentation Whole Period**

Yifan

1. Researched and added a way to read and import .txt documents

### Sept 27

Yifan

1. Created music_player_system.py file and MusicPlayerSystem class
2. Created constructors, variables, and functions in the newly created classes, including:
  - Constructor, set_next in Song class
  - Constructor, add_song in Playlist class
  - Constructor, update, populate_complete_list in MusicPlayerSystem class
  - updated main function to create instances of GUI class and MusicPlayerSystem class
3. Imported modules to link the OOP structure together, since the classes are on seperate files
4. Successfully Displayed Tkinter window and resized
5. Completed the linked-list data structure with the following:
  - playlist acts as the list and each song is a link
  - keep track of first song and last song added in playlist class
  - in the add_song method, checks if it is first song with if else statement and adds accordingly
  - next attribute for song class to keep track of next song

### Sept 28

Yifan
1. Successfully imported all songs from the .txt document to a new playlist
  - Generated a new list of songs since the original does not fit the format
  - Split the text document into a list of attributes of each song with '\n\ as the seperator
  - Then split each element in this list into another list, with each element being the attribute of a single song
  - Each element in this new list is the parameter of new song instance
  - All the songs are added into a linked list structure
2. Tested and verified that the linked-list data structure works by printing attribute of each link and going through list
3. Added commends to all code for readability