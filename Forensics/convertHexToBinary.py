import os

def convert_to_binary(toConvertList):
    list_to_return = [];
    for  index in toConvertList:
        print(index)
        for item in index:
            print(item)
            list2 = item.split(' ')
            print(list2)
            if(cell == 'E2'):
                list_to_return.append(1)
            else:
                list_to_return.append(0)

# This program is a little misnamed it does not convert from hex to binary
# it takes a space value of 1 and converts that to 1 and everything eles is 0
# was looking to see if that was a possible way to hide the values in white pages. 
# turns out no. 

def convert_to_binary(toConvertList):
    binary_list = []
    list_to_return = []
    for  index in toConvertList:
        for item in index:
            list2 = item.split(' ')
            for cell in list2:
                if(cell == 'E2'):
                    binary_list.append(1)
                else:
                    binary_list.append(0)
    
    list_to_return = binary_list.split(8)
    return list_to_return

lineList = [open("whitePagesHexOnly.txt")]


print(convert_to_binary(lineList))

