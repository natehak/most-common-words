#!/usr/bin/env python3.3 -O

# The most common words bot. By drkabob.
# Finds the top most common words in a reddit comment thread
# Copyright 2013 Nathan Hakkakzadeh. All rights reserved.
import praw, sys

# Before we do anything, we need to grab a list of the most common words to ignore
with open("commonwords.txt", "r") as words:¬
	commonwords = [word.lower().rstrip() for word in words]

r = praw.Reddit(user_agent="PRAW Most Common Word Bot. By /u/drkabob")
# Login would go here if it is necessary.

# Get the submission...
submission = r.get_submission(sys.argv[1])

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

# Print the top 5 words
for i in range(5):
	print(winners[i] + " - " + str(wordcount[winners[i]]))
