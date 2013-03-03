#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- encoding: utf-8 -*-

#  Licensed under the Apache License, Version 2.0 (the "License"); you may not
#  use this file except in compliance with the License. You may obtain a copy of
#  the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#  License for the specific language governing permissions and limitations under
#  the License.
#
#  KanjiQuiz.py
#  Japanese Quiz
#
#  Created by Chris Davis on 17/06/2011.
#  Copyright (c) 2012 GameWeaver LTD. All rights reserved.
#

#Notes:
#kunyomi = japanese reading
#onyomi = chinese reading

import os
import random
import json
from KanjiData import kanjis
from collections import namedtuple

Question = namedtuple('question', ['type', 'question'], verbose=False)
questions = [
	Question('kanji', u"What is the かんじ for %s(%s)"),
	Question('meaning', u"What is the meaning of %s(%s)"),
	Question('kunyomi', u"What is the くんよみ for %s(%s)"),
	Question('onyomi', u"What is the おんよみ for %s(%s)")
]

scores = [
	{'type': 'kanji', 'score': 0, 'outof': 0},
	{'type': 'meaning', 'score': 0, 'outof': 0},
	{'type': 'kunyomi', 'score': 0, 'outof': 0},
	{'type': 'onyomi', 'score': 0, 'outof': 0}
]

#Try and clear the screen
#just makes for a nicer user experience
#for mac & pc
def clearScreen():
	try:
		os.system('cls')
	except:
		pass
	try:
		os.system('clear')
	except:
		pass

#print scores
def PrintScores():
	print "Current score:"
	for item in scores:
		print "Type: %s,\t score: %s out of %s" % (item['type'], item['score'], item['outof'])
	print ""

def CreateQuestion():

	#Pick a dataitem at random
	index = random.randrange(0,len(kanjis)-1)
	targetItem = kanjis[index]

	#Pick a question at random
	qindex = random.randrange(0,len(questions)-1)
	q = questions[qindex]
	
	#Get a list of answer types, that are not the question type
	fields = list(targetItem._fields)
	fields.remove(q.type)
	rndom = random.randrange(0,len(fields))
	val = getattr(targetItem, fields[rndom])

	#find other possible answers to mix in the result
	possibleAnswers = kanjis
	del possibleAnswers[index]
	values = random.sample(possibleAnswers, 3)
	values.append(targetItem)
	random.shuffle(values)
	
	#Find the correct answer after the shuffle
	correctAnswer = values.index(targetItem)
	humanAnswer = correctAnswer+1

	#Show the question
	print q.question % (val, fields[rndom])
	
	for i, answer in list(enumerate(values, start=1)):
		print "%s) - %s" % (i, getattr(answer, q.type))

	enteredAnswer = raw_input("What's your answer?...")
	
	#entered answer cleanup
	if not enteredAnswer:
		enteredAnswer = -1

	try:
		enteredAnswer = int(enteredAnswer)
	except ValueError:
		enteredAnswer = -1

	#check answer
	if enteredAnswer == humanAnswer:
		print "Correct"
		scores[qindex]['score'] += 1
	else:
		print "Incorrect, the correct answer was: %s" % humanAnswer

	scores[qindex]['outof'] += 1

	nextQ = raw_input("Press return key for next question...")


def Start():
	clearScreen()
	print """Welcome To the Super Japanese Quiz!

	Do your best!

	The game is multiple choice, when you know the answer
	to a question enter, 1,2,3 or 4 and hit return.
	"""
	while True:
		CreateQuestion()
		clearScreen()
		PrintScores()
		
Start()