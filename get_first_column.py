def get_first_column(data):
    """
    Get the first column from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First column.
    """
    data=data.split("\n")
    a=[]
    for k in data:
        a.append(k.split(",")[0])
    return a[:-1] 
f =open("data.csv")
data=f.read()
print(get_first_column(data))
# Read the csv file