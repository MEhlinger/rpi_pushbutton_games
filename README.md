## RPi-Pygame Interactive Display

### What
This project aims to create a set of small games meant to be displayed
with a Raspberry Pi in a public location, and controlled using a few
pushbuttons attached to the GPIO pins. Ideally, the project will give
birth to a portable, self-contained (but externally powered) cabinet
with the display, controls, and other hardware. The software will
feature a main navigational menu, allowing users to step up and 
jump quickly into a number of different small games, and then
exit back to the menu. 

The intended home of the display is Elliot Hall @ Mansfield University,
home of the University's Computer Science department (as well as other
disciplines), in a high-traffic public location. 

### Ethos
The project should embody the following principles:

* Ease-of-Use: the games should be fast and easy to understand, for non-gamers.
* Community Participation: both in the sense that this is an open-source
	project intended to involve the CS department, as well as a public
	attraction intended to involve everyone passing by in a collective
	experience. Contributing to the project and playing with the product
	should be equally accessible, friendly experiences.
* Clean Code: since this is a small academic open-source project,
	we'll strive to keep to stylistic best practices. This project may-
	or may not- pass through many hands. There is always time for refactoring.

### Dependencies
* Python 2.7
* Pygame
* RPi.GPIO (Note: lowercase 'i' in 'RPi')


### Becoming Involved
There are four major categories in which you can help:

1. New Game: create a new game! It should rely on very simple assets,
	require almost no explanation to learn, and provide a quick and
	memorable experience. Use the pushbutton module for controls. *For now,
	this also includes the yet-unborn central menu interface*

	**NOTE: The final pin numbers for the pushbutton wiring are undecided.**

	**Contact project maintainer before submitting a pull request for pin #s**
2. Refactoring: clean up any part of the code according to general stylistic
	best practices: functions should do one thing, clear and concise naming,
	etc. "Best Practice" is fairly poorly defined here as: if you can't 
	understand a code block quickly and unambiguously from only reading it
	over, then it might be a candidate for refactoring.
3. Graphic Assets: this is a cs department project, and thus there's probably
	going to be some pretty rugged 'programmer art.' If you're at all
	artistically inclined, contact the project maintainer to talk about 
	making some sprites.
4. Hardware / Re-Form-Factoring: while the project works, and has been tested,
	as a hodgepodge of wires and exposed breadboarding components, we would
	ideally like to place everything in a sealed, sturdy housing that is both
	portable and not ugly. Think tabletop bar-game cabinet. Talk to the project
	maintainer if you have skills or resources to donate.

**Project Maintainer:** 
Marshall Ehlinger

ehlingermd15@mounties...

### Not An MU Student?
This project is intended to be a platform for education for Mansfield University
CS students, particularly the Fall 2015 Business Programming Concepts class. 
If you are interested in the project, but are not an MU student, feel
free to fork and do what you will, but know that there is a chance that any subsequent
pull requests may be declined in order to keep this version of the project inside
the department until the end of the semester.