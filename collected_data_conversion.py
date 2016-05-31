import csv


# gets a num between 1 and 0 to see how similar two objects are. 
# num_responses is total number of responses in this compariosn 
# Tesponse lst is a list of size 5, where each index maps to how many rated that index in our experiment. 
# Because we rated on a scale 1-5, and lists start with index 0, let scale 1 -> list[0], scale 2 -> list[1] etc.
def find_average_val(response_lst):
	
	total = 1 * response_lst[0] + 2 * response_lst[1] + 3 * response_lst[2] + 4 * response_lst[3] + 5 * response_lst[4]
	
	num_responses = sum(response_lst)

	average = total/float(num_responses)
	return average


print(find_average_val([1, 4, 3, 4, 0]))


with open('data/Similarity_Data1.csv', 'rb') as csvfile:
	reader = csv.reader(csvfile, delimiter=',')

	lst = [None for x in range(0,30)]

	for i in range(len(reader)):
		print(reader[i])
		# for col in row:
		# 	print col
