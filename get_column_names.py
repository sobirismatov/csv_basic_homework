#Define function,Get coloumn names from a csv file
def get_column_names(data):
    """ 
    Get column names from a csv file
    Parameters:
        data(str): csv file
    Returns:
        column_names: list of column names
    """
    data=data.split("\n")
    data=data[0].split(",")
    return data
f=open("data.csv")
data=f.read()
print(get_column_names(data))
    
# Read the csv file