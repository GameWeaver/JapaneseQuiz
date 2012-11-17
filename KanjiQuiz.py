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

introText = """Welcome To the Super Japanese Quiz!

Do your best!

The game is multiple choice, when you know the answer
to a question enter, 1,2,3 or 4 and hit return.
"""

questionKeys = [
    {
    "type": "kanji",
    "question": u"What is the かんじ for %s(%s)",
    "score": 0,
    "outof": 0
    },
    {
    "type": "kunyomi",
    "question": u"What is the くんよみ for %s(%s)",
    "score": 0,
    "outof": 0
    },
    {
    "type": "onyomi",
    "question": u"What is the おんよみ for %s(%s)",
    "score": 0,
    "outof": 0
    },
    {
    "type": "meanings",
    "question": u"What is the meaning of %s(%s)",
    "score": 0,
    "outof": 0
    }
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
	for item in questionKeys:
		print "Type: %s,\t score: %s out of %s" % (item['type'], item['score'], item['outof'])
	print ""

#Pick a random item from the list,
#Pick a key to be answer.
def CreateQuestion():

	#Pick an item
	index = random.randrange(0,len(kanjis))
	targetItem = kanjis[index]

	#pick the target question item
	items = list(xrange(len(questionKeys)))
	randomKeyIndex = random.choice(items)

	guessTarget = targetItem[questionKeys[randomKeyIndex]['type']]

	#Now select one of the other questions to ask
	#except this one.
	items.remove(randomKeyIndex)
	questionToAskIndex = random.choice(items)

	print questionKeys[questionToAskIndex]['question'] % (guessTarget,questionKeys[randomKeyIndex]['type'])

	#here we can get a list of possible answers
	lsoptions = list(xrange(len(kanjis)))
	lsoptions.remove(index)

	#Select 3 random from list.
	#I imagine a bug here in future, where
	#two hiraganas may clash.
	indexes = random.sample(lsoptions, 3)
	indexes.append(index)

	random.shuffle(indexes)

	correctAnswer = indexes.index(index)
	humanAnswer = correctAnswer+1

	print ""
	#print "Maybe it's...(hint, its: %s)" % humanAnswer
	print "Pick an answer..."

	ptr = 1
	for possibleAnswers in indexes:
		print "%s: %s" % (ptr,kanjis[possibleAnswers][questionKeys[questionToAskIndex]['type']])
		ptr = ptr + 1

	print ""
	enteredAnswer = raw_input("What's your answer?...")

	if not enteredAnswer:
		enteredAnswer = -1

	try:
		enteredAnswer = int(enteredAnswer)
	except ValueError:
		enteredAnswer = -1

	if enteredAnswer == humanAnswer:
		print "Correct"
		questionKeys[questionToAskIndex]['score'] = questionKeys[questionToAskIndex]['score'] + 1
	else:
		print "Incorrect, the correct answer was: %s" % humanAnswer

	questionKeys[questionToAskIndex]['outof'] = questionKeys[questionToAskIndex]['outof'] + 1

	nextQ = raw_input("Press return key for next question...")


def Start():
	clearScreen()
	print introText
	while True:
		CreateQuestion()
		clearScreen()
		PrintScores()
		
Start()