
#entropy of entire data set first
def totalEntropy(data):
	entropy_node = 0 #initialize entropy node
	values = data.play.unique() # get list of unique inputs in the column to iterate through
	for value in values:
		fraction = data.play.value_counts()[value]/len(data.play) # divide count of each answer by total number of answers
		entropy_node += -fraction*np.log2(fraction) # add set to compute entropy


#entropy of a feature column
def entropy(data, column):
	target_variables = data.play.unique()
	variables = data[column].unique() # get list of unique inputs in the column to iterate through

	entropy_column = 0 #initialize
	for variable in variables: #iterate
		numerator = len(data[column][data[attribute]==variable][data.play == target_variable])
		denominator = len(data[column][data[column]==variable])
		fraction = numerator/(denominator+eps) #proportion(i)
		entropy_column += -fraction*log(fraction+eps) # totals up entropy of single column
	fraction2 = denominator/len(data)
	entropy_column += -fraction2*entropy_column # sum of all entropy
	return(abs(entropy_attribute))

#entropy of each column gets stored in dictionary
entropyDict = {k:ent(data,k) for k in data.keys() [:-1]}
entropyDict

# information gain for a feature column

def infoGain(data, column):
	return(data-column)

infoGainDict = {k:infoGain(entropy_node,a_entropy[k]) for k in a_entropy)