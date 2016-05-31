# Written by Stephen Grinich for CS328 at Carleton College

import numpy as np
import matplotlib.pyplot as plt # import the plotting tools
import collected_data_conversion


person = "Rosa Parks"

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





plt.ylabel('Ranking of Similarity to ' + person)
plt.xlabel("People compared to " + person)
plt.xticks(range(len(object_lst_sans_person)), object_lst_sans_person, size='small')
plt.plot([x for x in range(16)], [x for x in range(0,16)])

plt.title('Similarity to ' + person)
plt.show()
