"""
Theory of Computation- Metacompiler Project 
"I never metacompiler I didn't like."	- Will Rogers
Author- Zhenlin Jin
"""
import string

alphabets = list(input("Enter your choice of language alphabets: \n"))
dim = input("Enter your dimensions of transition matrix (in the format of rows followed by columns separated with space): \n")
dim_list = [int(x) for x in dim.split()]
rows = int(dim_list[0])
cols = int(dim_list[1])

"""we want the user to input the transition table like
[[1,10001],[1,2]]
with rows and cols in mind, we make the transition matrix"""
def your_table(rows, cols):
	print("Now let's make this table!")
	i = j = 0
	table = []
	#table = [[0 for x in range(cols)] for x in range(rows)]
	#repeat filling the rows of the table for cols times	
	for i in range(0,rows):
		row_vals = input("Fill the row, separate each integer by space \n")
		rv_list = [int(x) for x in row_vals.split()]
		#make sure columns count is correct! 
		if(len(rv_list) != cols):
			assert len(rv_list) == cols, "Your row input isn't right!"
				
		table.append(rv_list)
	return table

"""this function look up the values given the input current state
it returns the value, i.e., the state it ends up"""
def table_output(input_char, state, table, sorted_alphabets):
	#since we are reading a string of characters, we need to 
	#convert input alphabet into index
	#alpha2index = dict(zip(string.ascii_lowercase, range(0,26))) 
	

	input_column = sorted_alphabets.index(input_char)
	state = table[state][input_column]
	return state


"""take the string and the state that tbe table outputs
	a list of string"""
def parse(s, state, alphabets):
	if state > 10000:
		#we assumed state > 10000 has to do with error state! 
		#this will directly end the parsing and show the error message
		return state
	elif len(s) > 0:
		char = s.pop(0)
		#examine if char is in alphabet
		if char not in alphabets:
			state = 10000 #generic illegal char would end up in state 10000
			return state
			
		return parse(s, table_output(char, state, table,sorted_alphabets), alphabets)
	else:	#empty string, therefore return final state
		return state


def error_messages():
	nofMessages = int(input("Time to Make Error/Acceptance messages! Enter number of messages in total: "))
	
	i = 0
	total_i = []
	total_m = []
	while(i < nofMessages):
		m_i = int(input("Enter the state for the message: "))
		total_i.append(m_i)
		m = input("Enter the corresponding message: ") 
		total_m.append(m)
		i += 1

	dict_messages = dict(zip(total_i, total_m))
	return dict_messages



"""we need to do something about our alphabets to make sure it corresponds to 
the column it belongs to, note that here we don't accept uppercase letter"""
sorted_alphabets = sorted(alphabets)



table = your_table(rows, cols)

dict_messages = error_messages()
dict_messages[10000] = 'Illegal character!'


while True:
	#here we input the string as s
	s = list(input("Please enter an string of characters! \n"))
	resulting_state = parse(s, 0, alphabets)

	resulting_messages = dict_messages[resulting_state]
	print(resulting_messages)