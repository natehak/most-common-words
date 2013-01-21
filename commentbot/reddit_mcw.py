#!/usr/bin/env python3.3 -O

# The most common words bot. By /u/drkabob
# Finds the top most common words in a reddit comment thread
# Copyright 2013 Nathan Hakkakzadeh. All rights reserved.
import praw, sys, collections

from bottle import get, request, run

# Before we do anything, we need to grab a list of the most common words to ignore
with open("commonwords.txt", "r") as words:
	commonwords = [word.lower().rstrip() for word in words]

r = praw.Reddit(user_agent="PRAW Most Common Word Bot. By /u/drkabob")
# Login would go here if it is necessary.


# Function that actually does the dirty work
# Returns an ordered dictionary with the words in order of how popular
# link: Comment thread we want to parse
# top: How many of the top words do we want to get (Default: 5)
# WARNING: This function is SLOOOOOOW and will block the entire script.
# You should REALLY run this in a thread.
def get_top_words(link, top=5):
	# Get the submission...
	submission = r.get_submission(link)
	
	# We need to go deeper...
	submission.replace_more_comments()
	comments = praw.helpers.flatten_tree(submission.comments)
	
	wordcount = {}
	
	# Loop through the comments, split it up into words and count them up
	for comment in comments:
		
		words = comment.body.split()
		
		for word in words:
			word = word.lower()
			word = ''.join(e for e in word if e.isalnum())
			if not word in commonwords:
				if word in wordcount:
					wordcount[word] += 1
				else:
					wordcount[word] = 1
	
	# Sort the list...
	winners = sorted(wordcount, key=wordcount.get, reverse=True)
	
	# Build the dictionary we want to return...
	toreturn = collections.OrderedDict()
	for i in range(top):
		toreturn[winners[i]] = wordcount[winners[i]]
		
	return toreturn

@get("/mcw")
def mcw():
	link = request.query.link
	
	if link == "":
		return """<title>Most Common Words for Reddit comment threads</title>
				<h3>Most Common Words for Reddit comment threads</h3>
				<form name="input" action="mcw" method="get">
					Comment Thread Link: <input type="text" size="50" name="link">
					<br />
					Top <select name="top">
							<option value="1">1</option>
							<option value="2">2</option>
							<option value="3">3</option>
							<option value="4">4</option>
							<option value="5" selected>5</option>
							<option value="6">6</option>
							<option value="7">7</option>
							<option value="8">8</option>
							<option value="9">9</option>
							<option value="10">10</option>
						</select> words.
						<br /> <br />
						<input type="submit" value="Calculate">
				</form>
				
				Warning, will take a long time to load. Do NOT try to refresh page.
				A tool by <a href="http://www.reddit.com/user/drkabob">Nathan.</a>
				Are good with HTML and CSS? Can you make websites pretty? <a href="mailto:nathan@welcometonathan.com">Contact me</a> if you're interested in making this less ugly. <br />
				Find the code on GitHub <a href="https://github.com/drkabob/most-common-words"> here!</a>"""
	else:
		results = get_top_words(link, top=int(request.query.top))
		
		toreturn = """<title>Most Common Words for Reddit comment threads</title>
					<h3>Most common words for comment thread given</h3>
					"""
		i = 1
		for result in results:
			toreturn = toreturn + str(i) + ") " + result + " - " + str(results[result])+ "<br />"
			i += 1
			
		toreturn = toreturn + """<br /><br /><FORM METHOD="LINK" ACTION="mcw"> <INPUT TYPE="submit" VALUE="Back"> </FORM>"""
		return toreturn
		
# Run the web server!
run(server="cherrypy", port=80)
