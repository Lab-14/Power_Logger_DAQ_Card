import scipy.io
import numpy as np


# Python 3 code to find sum of elements in given array
def _sum(arr):
    # initialize a variable to store the sum while iterating through the array later
    sum=0
    # iterate through the array and add each element to the sum variable one at a time
    for i in arr:
        sum = sum + i
    return(sum)

path = '/media/manoj/0C0CF5C50CF5A9BA/Users/manojg/Documents/NI_DAQ_Scripts/'

folder = 'Data_Backup_28102021/'

file_id = 'Data_20211028T155029'

file_index = 0
# data_stack = np.empty((0,999), float)
data_stack = np. array([])

mat_data = scipy.io.loadmat(path+folder+file_id+'.mat')

# extract header of the python dictionary
# print (mat_data.keys())

# print first element of the dict array
print (mat_data["data_acq"][0])

print ( len(mat_data["data_acq"]))


# Calculate sum of data vector
ans = _sum(mat_data["data_acq"])
# print (ans)
data_stack = np.append(data_stack, ans)
print(data_stack)

file_index = file_index+1
