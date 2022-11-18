def find_number_of_columns(data):
    """
    Find the number of columns in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of columns.
    """
    a=0
    for row in data:
        a=row.split(',')
    return len(a)

    
f= open('data.csv')
data=f.read()
print(find_number_of_columns(data))


# Read the csv file