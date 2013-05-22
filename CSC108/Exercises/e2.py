def get_upper_list(list):
    '''(list of strs) -> list of strs'''
    index = 0
    new_list = []
    while index < len(list):    
        string = str(list[index]).upper()
        new_list.append(string)
        index += 1
    return new_list

def convert_to_upper(list):
    '''(list of strs) -> NoneType'''
    index = 0
    while index < len(list):
        list[index] = list[index].upper()
        index += 1
    
   

def get_str_list(list):
    '''(list of lists of strs) -> list of strs'''
    index = 0
    new_list = []
    while index < len(list):
        string = ''
        for x in list[index]:
            string += x
        new_list.append(string)
        index +=1
    return new_list


 

if __name__ == "__main__":
    list  = ['haha','lalal', 'fe', 'sas1']
    list2 = [['haha','bobo'],['nono','gogo'],['soso','lolo']]
