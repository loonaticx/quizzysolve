# Quizzysolve - An updated Quizzy's Word Challenge solver!

This is a fork of a quizzy solver that was made by Chidambaram Annamalai (quantumelixir). You can find the original Quizzy script (here)[https://gist.github.com/quantumelixir/780823]


## Features
!(GUI Interface!! Wowza!)[img/interface.png]
- Both a command line interface *and* a GUI interface.

## Requirements
- The GUI requires the panda3d library.

### Installation
- Install the requirements if needed.
- Next, run ``download_dictionary.bat``. This will download a 6.50 MB JSON file of just words. Awesome.

### Usage
- For CLI, edit ``ringfile.txt`` with the given letters. Add all of the letters in the outer most ring first, then add a new line for each ring. Run ``python RunQuizzySolver.py`` to get words that fit your input letters.
- For GUI, run ``python QuizzyGUI.py``.
	- Note: Some entries don't automatically update. You need to press ENTER after entering the letter.

## Todo
- Yeah, it would've been much better if i used an actual GUI library. Maybe I'll rewrite it in PySide someday!
