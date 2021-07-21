import pandas as pd
import numpy as np

#read csv into pandas Dataframe

num_data = pd.read_csv(r'workspace.txt',header=None)
list_data = pd.read_csv(r'data.txt',header=None, sep="\t")

motion_arr = ["1.Stand", "2.Walk", "3.Run", "4.SitDown", "5.LieDown", "6.Ride", "7.Dress", "8.PickUp", "9.ClimbOver", "10.Suicide", "11.Photo"]

def take_inputs():
    range_from = input("from? : ")
    range_to = input("to? : ")
    object_id = input("object id? : ")
    motion = input('motion? \n "1.Stand", "2.Walk", "3.Run", "4.SitDown", "5.LieDown", \n "6.Ride", "7.Dress", "8.PickUp", "9.ClimbOver", "10.Suicide", "11.Photo"')
    return range_from, range_to, object_id, motion

def take_inputs_txt():
    range_from = list_data[0]
    range_to = list_data[1]
    object_id = list_data[2]
    motion = list_data[3]
    return range_from, range_to, object_id, motion

def validation(a,b,c,d):
    d = int(d)
    if d in range (1,12):
        motion = motion_arr[d-1]
        print("selected motion : {}".format(motion))
    else:
        print("NO SUCH MOTION")
        return False

    return motion

def save():
    answer = input("save now ? : [y/n]")
    if (answer == 'y' or 'n'):
        return answer
    else:
        return False

def main():
    while(True):
        #a,b,c,d = take_inputs()
        a2,b2,c2,d2 = take_inputs_txt()

        for k in range(len(a2)):
        
            a = int(a2[k])
            b = int(b2[k])
            c = int(c2[k])
            d = int(d2[k])

            a_index = num_data.loc[(num_data[0] == a) & (num_data[2] == c)].index
            b_index = num_data.loc[(num_data[0] == b) & (num_data[2] == c)].index

            a_index = int(a_index[0]) + 1
            b_index = int(b_index[0]) + 1

            motion = validation(a,b,c,d)
            
            for i in range(a_index,b_index-1):
                if num_data.loc[i][2] == c :
                    num_data.at[i,1] = motion
                    
            print("range from {} to {} replacing motion with {}".format(a,b,motion))
        
        savenow = save()
        
        if (savenow):
            num_data.to_csv('workspace.txt',sep=",",index=False, header=False)
        
        
if __name__ == "__main__":
    main()
