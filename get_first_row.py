def get_first_row(data):   
   """
   Get the first row from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First row.
   """
   data=data.split("\n")
   a=[]
   a.append(data[1])
   return a
f=open("data.csv")
data=f.read()
print(get_first_row(data))

# Read the csv file