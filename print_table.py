# import pandas library
import pandas as pd

def sum(x,y):
    return x+y


def is_even(x):
	if type(x) != int:
		raise TypeError("Katinha, it should be a number")
	if x%2==0:
		return True
	return False


def return_katinha():
    return "linda"
    

# dictionary with list object in values
details = {
	'Name' : ['Ankit', 'Aishwarya', 'Shaurya', 'Shivangi'],
	'Age' : [23, 21, 22, 21],
	'University' : ['BHU', 'JNU', 'DU', 'TEST3'],
}

# creating a Dataframe object 
df = pd.DataFrame(details)

print(df)


# is_even("katinha")



