Most Common Words for Reddit
=================

A website that finds the most common words on a reddit comment thread.

A tool by [Nathan Hakkakzadeh](http://www.welcometonathan.com/) or [drkabob](http://www.reddit.com/u/drkabob).

This repo consists of two python scripts. The `bot.py` file is a script that takes one argument and will output the
top 5 words.

The `reddit_mcw.py` file is a [bottle](http://bottlepy.org/) web application. An example implementation can be found
on my website [here](http://mcw.welcometonathan.com/). The web app needs to be run with a web server that supports threading
as finding the most common words takes a long time due to the limit placed on reddit API calls. I personally use [CherryPy](http://www.cherrypy.org/),
but you can change the server used by editing the `reddit_mcw.py` file manually.

Also the `commonwords.txt` file is used by both `bot.py` and `reddit_mcw.py` to ignore common words that would make the results
a lot less interesting. It is required that this file be in the directory where either `bot.py` or `reddit_mcw.py` is run.

Prerequisites
-----------------
Both `bot.py` and `reddit_mcw.py` are designed to work with `Python 3.x`. They will work with Python 2.x, but you will encounter
Unicode errors.

For both `bot.py` and `reddit_mcw.py`, you will need...
* A Python interpreter, preferably `Python 3.x`
* The latest version of [praw](https://github.com/praw-dev/praw)

And for `reddit_mcw.py`, you will need...
* [bottle](http://bottlepy.org/)
* [CherryPy](http://www.cherrypy.org/)

UI Overhaul
-----------------
The UI Overhaul was done by [Samuel Thacker](http://www.samuelthacker.me) or [h4xg33k](http://www.github.com/h4xg33k/).

Designed in Bootstrap, coding integrated into Python.
