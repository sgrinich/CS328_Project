# Written by Stephen Grinich for CS328 at Carleton College

import numpy as np
import matplotlib.pyplot as plt # import the plotting tools
import collected_data_conversion

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

person = raw_input("Please enter a name from the following list. Make sure to spell it the same way.\n" +  str(object_lst))
print
while person not in object_lst:
	person = raw_input("Please enter a name from the following list. Make sure to spell it the same way.\n" +  str(object_lst))
	print




object_lst_sans_person = []
for character in object_lst:
	if character != person:
		object_lst_sans_person.append(character)
sims = collected_data_conversion.get_similarities_for_person(person)
experiment_results = sims[0]
model_results = sims[1]
tversky_results = model_results[0]
shepard_results = model_results[1]
medin_results = model_results[2]

experiment_map_dict = {}
ranking = len(experiment_results)
for i in experiment_results:
	experiment_map_dict[i] = ranking
	ranking -= 1

tversky_map_dict = {}
ranking = len(tversky_results)
for i in tversky_results:
	tversky_map_dict[i] = ranking
	ranking -= 1

shepard_map_dict = {}
ranking = len(shepard_results)
for i in shepard_results:
	shepard_map_dict[i] = ranking
	ranking -= 1


plt.ylabel('Ranking of Similarity to ' + person)
plt.xlabel("People compared to " + person)
plt.xticks(range(len(object_lst_sans_person)), object_lst_sans_person, size='small')
experiment, = plt.plot([x for x in range(15)], [experiment_map_dict[i] for i in object_lst_sans_person], label = "Experimental Results")
tversky, = plt.plot([x for x in range(15)], [tversky_map_dict[i] for i in object_lst_sans_person], label = "Tversky Model Results")
shepard, = plt.plot([x for x in range(15)], [shepard_map_dict[i] for i in object_lst_sans_person], label = "Shepard Model Results")
plt.legend([experiment, tversky, shepard], ['Experimental Results', 'Tversky Model Results', "Shepard Model Results"])

plt.title('Similarity to ' + person)
plt.show()
