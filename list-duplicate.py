#################################################Using the For loop######################################################################



data = [1,2,3,4,5,55,55,6,6,2,1,3,4,1000,1000]

def remove_duplicates(duplist):
    NoDuplicateList = []
    for element in duplist:
        if element not in NoDuplicateList:
            NoDuplicateList.append(element)

    return NoDuplicateList

print(remove_duplicates(data))



#########################################################using sets######################################################################





# removing duplicates from the list using set()

# initializing list

duplicate_list = [11, 15, 13, 16, 13, 15, 16, 11]

print ("The list is: " + str(duplicate_list))

# to remove duplicates from list

duplicate_list = list(set(duplicate_list))

# printing list after removal

# ordering distorted

print ("The list after removing duplicates: " + str(duplicate_list))