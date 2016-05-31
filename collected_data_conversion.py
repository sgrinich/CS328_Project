import csv
import object_loader


# gets a num between 1 and 0 to see how similar two objects are. 
# num_responses is total number of responses in this compariosn 
# Tesponse lst is a list of size 5, where each index maps to how many rated that index in our experiment. 
# Because we rated on a scale 1-5, and lists start with index 0, let scale 1 -> list[0], scale 2 -> list[1] etc.
def find_average_val(response_lst):
	
	total = 1 * response_lst[0] + 2 * response_lst[1] + 3 * response_lst[2] + 4 * response_lst[3] + 5 * response_lst[4]
	
	num_responses = sum(response_lst)

	average = total/float(num_responses)
	return average


def get_names_and_responses(filename):
	pair_lists = [[] for x in range(0,30)]
	similar_data = object_loader.load_google_form_csv("data/" + filename)
	names = similar_data[0].split(",")


	for i in range(len(similar_data)):
		if i != 0:
			lst = (similar_data[i].split(",")[1:])
			int_lst = []
			for str_num in lst:
				if str_num == '""':
					str_num = '"3"'
				int_num = int(''.join(filter(lambda x: x.isdigit(), str_num)))
				int_lst.append(int_num)


			for j in range(len(int_lst)):
				pair_lists[j].append(int_lst[j])


	return(names[1:], pair_lists)



def get_tuples_from_names(names):
	tup_lst = []
	for i in range(len(names)):
		# print(names[i])
		lst = names[i].split("and")
		tup = (lst[0][1:-1], lst[1][1:-1])
		tup_lst.append(tup)
	return tup_lst

def get_similarity_dict(name_tuples, responses):
	sim_dict = {}
	for i in range(len(name_tuples)):
		sim_dict[name_tuples[i]] = responses[i]
	return sim_dict


# Gets a single dictionary. Each key in this dictionary is a pair of characters in our experiment.
# The value for each key is a list of all rankings between 1 and 5 that people recorded in our experiment
def get_all_similarity_dict():

	tup = get_names_and_responses("Similarity_Data1.txt")
	names = tup[0]
	responses = tup[1]
	name_tuples = get_tuples_from_names(names)


	sim_dict_1 = get_similarity_dict(name_tuples, responses)

	tup = get_names_and_responses("Similarity_Data2.txt")
	names = tup[0]
	responses = tup[1]
	name_tuples = get_tuples_from_names(names)

	sim_dict_2 = get_similarity_dict(name_tuples, responses)


	tup = get_names_and_responses("Similarity_Data3.txt")
	names = tup[0]
	responses = tup[1]
	name_tuples = get_tuples_from_names(names)


	sim_dict_3 = get_similarity_dict(name_tuples, responses)

	tup = get_names_and_responses("Similarity_Data4.txt")
	names = tup[0]
	responses = tup[1]
	name_tuples = get_tuples_from_names(names)

	sim_dict_4 = get_similarity_dict(name_tuples, responses)

	
	all_dicts = [sim_dict_1, sim_dict_2, sim_dict_3, sim_dict_4]

	super_dict = {}

	for d in all_dicts:
	    for k, v in d.iteritems():
	        super_dict[k] = v

	return super_dict






get_all_similarity_dict()

