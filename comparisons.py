# Written by Stephen Grinich for CS 328, Spring 2016 Carleton College. Randomly determines experiment stimlui to remove selection bias.

import itertools
import random 


def get_four_chunks(lst):

	# all of our possible pairs over our 16 characters
	choosed = list(itertools.combinations(lst, 2))

	# randomizes our list of possible pairs
	random.shuffle(choosed)

	# split into 4 chunks for 4 different surveys
	four_chunks = chunks(choosed, len(choosed)/4)

	return four_chunks


def chunks(l, n):
    n = max(1, n)
    return [l[i:i + n] for i in range(0, len(l), n)]


def get_objects_for_features(lst):
	return chunks(lst,len(lst)/4)

def main():

	object_lst = ['William Shakespeare', 'Darth Vader',
	'Madonna',
	'Usain Bolt',
	'Hercules',
	'Pope Francis',
	'Rosa Parks',
	'Christopher Colombus',
	'Stevie P.',
	'Harry Potter',
	'Matt Damon',
	'Mother Teresa',
	'Barack Obama',
	'Marie Curie',
	'Jane Austen',
	'Serena Williams']

	feature_lst = ['Male',
	'Female',
	'Deceased',
	'Performer',
	'Athlete',
	'Award-winning',
	'Conqueror',
	'Evil',
	'Fictional',
	'Royal',
	'Adventurous',
	'Controversial',
	'Young',
	'Old',
	'Knowledgeable'
	'Modern',
	'Progressive',
	'Conservative',
	'Died abruptly',
	'Successful',
	'Writer'
	'Musician']


	chunks = get_four_chunks(object_lst)

	for i in range(len(chunks)):
		print("SURVEY " + str(i))
		print 
		for j in range(len(chunks[i])):
			pair =  chunks[i][j]
			print pair[0] + " and " + pair[1]
			print 
		print
		print

main()
