import pandas as pd
import numpy as np

#read csv into pandas Dataframe

num_data = pd.read_csv(r'workspace.txt',header=None)
#arr_del = []

def take_inputs():

    object_id = input("object id? : ")
    return object_id

def save():
    answer = input("save now ? : [y/n]")
    if (answer == 'y'):
        return answer
    else:
        return False

def main():
    while(True):
        
        c = take_inputs()

        c = int(c)

        arr_del = []
            
        for i in range(len(num_data)-1):
            if num_data.loc[i][2] == c :
                arr_del.append(i)
                print("deleting index {} with id {}".format(i,c))

        print("delete array: {}".format(arr_del))

        del_arr = num_data.drop(num_data.index[arr_del])
        
        savenow = save()
        
        if (savenow):
            del_arr.to_csv('workspace.txt',sep=",",index=False, header=False)

        
if __name__ == "__main__":
    main()
