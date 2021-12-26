import scipy.io
import numpy as np
import os
import re

# Python 3 code to find sum of elements in given array
def _sum(arr):
    # initialize a variable to store the sum while iterating through the array later
    sum=0
    # iterate through the array and add each element to the sum variable one at a time
    for i in arr:
        sum = sum + i
    return(sum)

path = '/media/manoj/0C0CF5C50CF5A9BA/Users/manojg/Documents/NI_DAQ_Scripts/'

folder = 'Data_Backup_10112021 [CAM2N3 8FPS OVERLAP43 5K Frames] [Scale-3] REPEAT SET/Voltage_data'

csvfile_name = '[CAM2N3 8FPS OVERLAP43 5K Frames] [Scale-3] REPEAT SET_Voltage_data'

# file_id = 'Data_20211028T155029'

file_index = 0
# data_stack = np.empty((0,999), float)
data_stack = np. array([])
entries_stack = np. array([])
Comb_Stack = np. array([])

entries = os.listdir(path+folder+'/')
entries.sort() #good initial sort but doesnt sort numerically very well
# print (entries[0:4])

print (len(entries))

while file_index<len(entries):

    print(file_index)

    # print(entries.split("Data_"))
    # print ([i.split('_', 1)[0] for i in entries])

    entries_label = re.split('_|.mat', entries[file_index])[1]
    # print (entries_label)

    # mat_data = scipy.io.loadmat(path+folder+file_id+'.mat')
    mat_data = scipy.io.loadmat(path+folder+'/'+entries[file_index])

    # extract header of the python dictionary
    # print (mat_data.keys())

    # # print first element of the dict array
    # print (mat_data["data_acq"][0])
    #
    # print ( len(mat_data["data_acq"]))

    # Calculate sum of data vector
    ans = _sum(mat_data["data_acq"])
    # Normalize data Dvector
    ans_norm = ans/1000
    # print (ans)
    data_stack = np.append(data_stack, ans_norm)
    # print(data_stack)
    entries_stack = np.append(entries_stack, entries_label)
    # print(entries_stack)

    Comb_Stack =  np.column_stack((entries_stack, data_stack))

    file_index = file_index+1

    # print (Comb_Stack)

np.savetxt((csvfile_name+'_Data_Vrms.csv'), Comb_Stack, delimiter=',', fmt="%s")
