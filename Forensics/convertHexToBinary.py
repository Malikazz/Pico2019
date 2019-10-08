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
    return list_to_return

lineList = [open("whitePagesHexOnly.txt")]

convert_to_binary(lineList)
