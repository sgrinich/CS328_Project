import math

def get_tversky_similarity(a, b, alpha=.5, beta=.5):
	a = get_index_for_binary_val(a)
	b = get_index_for_binary_val(b)

	intersection = intersect(a,b)

	numerator = tversky_func(intersection)
	denomonator = tversky_func(intersection) + (alpha * tversky_func(difference(a,b))) + (beta * tversky_func(difference(b,a)))

	return numerator/denomonator

def tversky_func(lst):
	count = 0
	for i in range(len(lst)):
		count += 1
	return count	

def intersect(x, y):
     return list(set(x) & set(y))

def difference(x, y):
	return list(set(x).difference(set(y)))
def sym_difference(x,y):
	return list(set(x) ^ set(y))

def get_index_for_binary_val(lst):
	index_list = []
	for i in range(len(lst)):
		if lst[i] == 1:
			index_list.append(i)

	return index_list

def get_shepard_similarity(a,b):
	return math.exp(shepard_distance_function(a,b))
	

def shepard_distance_function(a,b):
	a = get_index_for_binary_val(a)
	b = get_index_for_binary_val(b)
	d = sym_difference(a,b)
	count = 0
	for i in range(len(d)):
		count += 1
	return (count * -1)

def get_medin_similarity(a, b, theta=0.1):
	if a == b:
		return 1
	else:
		return theta

def getIndicesForCategory(category_name, exemplar_categories):
	lst = []
	for i in range(len(exemplar_categories)):
		if exemplar_categories[i] == category_name:
			lst.append(i)

	return lst

def context_model(test_stimuli, exemplars, exemplar_categories, similarity_fn):
	probability_A_x_list = []

	category_A_indices = getIndicesForCategory("A", exemplar_categories)
	category_B_indices = getIndicesForCategory("B", exemplar_categories)



	for x in test_stimuli:


		func_sum_a=0
		func_sum_b = 0
		for i in range(len(exemplar_categories)):
			if i in category_A_indices:
				fn_res = similarity_fn(x, exemplars[i])
				func_sum_a += fn_res
			else:
				fn_res = similarity_fn(x, exemplars[i])
				func_sum_b += fn_res

		model_val = func_sum_a/(func_sum_a + func_sum_b)
		
		probability_A_x_list.append(model_val)
	return probability_A_x_list



def prototype(exemplars):
	prototype_list = [0 for x in range(len(exemplars[0]))]
	num_exemplars = len(exemplars)

	
	for exemplar in exemplars:
		for i in range(len(exemplar)):
			prototype_list[i] += exemplar[i]

	for i in range(len(prototype_list)):
		if prototype_list[i] >= num_exemplars/2:
			prototype_list[i] = 1
		else:
			prototype_list[i] = 0

	return prototype_list

def prototype_model(test_stimuli, exemplars, exemplar_categories, similarity_fn):
	probability_A_x_list = []

	category_A_indices = getIndicesForCategory("A", exemplar_categories)
	category_B_indices = getIndicesForCategory("B", exemplar_categories)



	for x in test_stimuli:



		category_A_exemplars = []
		category_B_exemplars = []


		for i in range(len(exemplar_categories)):
			if i in category_A_indices:
				category_A_exemplars.append(exemplars[i])
			else:
				category_B_exemplars.append(exemplars[i])

		func_a_res = similarity_fn(x, prototype(category_A_exemplars))
		func_b_res = similarity_fn(x, prototype(category_B_exemplars))

		model_val = func_a_res/(func_a_res + func_b_res)
		
		probability_A_x_list.append(model_val)
	return probability_A_x_list






