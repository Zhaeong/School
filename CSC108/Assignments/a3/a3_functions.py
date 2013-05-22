'''A friend recommendation system.

In a "person to friends" dictionary, each key is a person (str) and each value is that person's friends (list of strs).

In a "person to networks" dictionary, each key is a person (str) and each value is the networks that person belongs to (list of strs).

In a "network to people" dictionary, each key is a network (str) and each value is the people belonging to that network (list of strs).'''

def reverse_name(l_f):
    '''
    (str)-> str.
    Returns the paramater string <l_f>, but in reverse and without a comma.
    ('Parker, Charlie') -> 'Charlie Parker'
    '''
    
    (last, first) = l_f.split(', ')
    return first + ' ' + last
    
def read_file(r):
    '''
    (r)-> list of strs
    Returns a list of strings without '\n' character.
    '''
    
    lines = r.readlines()
    clean_lines = []
    for line in lines:
        clean_lines.append(line.rstrip('\n'))
    return clean_lines
    

def person_records(l_lines):
    '''
    (list of strings)-> list of lists
    <l_lines> is a list of strings as produced by read_file().
    Returns a list of lists, in which each list is a record.
    '''
    
    records = []
    start_of_next_record = 0
    while '' in l_lines[start_of_next_record:]: #" '' shows where record ends"
        index_of_empty = l_lines.index('', start_of_next_record)
        records.append(l_lines[start_of_next_record:index_of_empty])
        start_of_next_record = index_of_empty + 1
    if records != []:
        records.append(l_lines[start_of_next_record:])  
    return records 

def split_record(record):
    '''
    (list)-> list
    Splits the person <record> into a list of three elements:
    - First, the person's name (str)
    - Second, the person's networks (list of strings) 
    - Third, a person's friends.(list of strings)
    '''
    name = record[0]
    networks = [] 
    friends = []
    
    for line in record[1:]:
        if ',' in line:
            friends.append(line)
        else: 
            networks.append(line)
    return [name, networks, friends]
            
    

def load_profiles(profiles_file, person_to_friends, person_to_networks):
    '''
    (file, dict of {str : list of strs}, 
    dict of {str : list of strs}) -> NoneType
    <profiles_file> is a reader with specific formatting. <person to friends> 
    is a dictionary with a person as the key and a list of friends the value. 
    Likewise with <person_to_networks>, but with a list of a
    person's networks as the value. 
    Updates the two dictionaries to include the data from the open file. 
    '''
    
    
    lines = read_file(profiles_file)
    records = person_records(lines)
    for record in records:
        (person, networks, friends) = split_record(record)
        reverse_friends = []
        reverse_person = reverse_name(person)
        for friend in friends:
                    reverse_friends.append(reverse_name(friend))        
        
        if reverse_person in person_to_friends.keys():
            person_to_friends[reverse_person] += reverse_friends
        else:
            if reverse_friends != []  :  # "if he does have friends"
                person_to_friends[reverse_person] = reverse_friends
        if reverse_person in person_to_networks.keys():
            person_to_networks[reverse_person] += networks
            
        else:
            if networks != []: # "if person does belong to a network"
                person_to_networks[reverse_person] = networks
        
        
            
        
    
     
        
def invert_networks_dict(person_to_networks):
    '''
    (dict of {str : list of strs}) -> dict of {str : list of strs}.
    Returns a "network to people" dictionary based on
    the <person_to_networks> dictionary.
    '''
    
    
    n_people = {}
    for person, networks in person_to_networks.items():
        for network in networks:
            if network in n_people.keys(): 
                n_people[network].append(person)
            else: n_people[network] = [person]
            
    return n_people
    
		
		
def make_recommendations(person, person_to_friends, person_to_networks):
    '''(str, dict of {str : list of strs}, dict of {str : list of strs}) -> list of (str, int) tuples
    Return the friend recommendations for the given person in a list of tuples where the first element of each tuple is a potential friend's name (in the same format as the dictionary keys) and the second element is that potential friend's score. Only potential friends with non-zero scores is included in the list.'''
    
    
    #Arguement checks
    
    if person == '':
        return []
    
    if person_to_friends == {} and person_to_networks == {}:
        return []
    
    #all person must be in the person_to_friends dictionary, no new person
    #can be introduced in person_to_networks dictionary    
    if not person_to_friends.has_key(person):
        return []
    
    if person_to_friends[person] == [] and person_to_networks[person] == []:
        return []
    
    
    
    recommend = [] 
  
    personList = person_to_friends[person]
    
    #tests for empty networks dictionary
    if person_to_networks != {} and person_to_networks.has_key(person):
        networkList = person_to_networks[person]
    
    #append all [person,0] to recommend list except for person
    for other_person in person_to_friends:
        if person != other_person and other_person not in personList:
            recommend.append([other_person,0])
    
    #add +1 to the friend score based on mutual friends in recommend list    
    for other_person in recommend:
        otherPersonList = person_to_friends[other_person[0]]
        for i in otherPersonList:
            if i in personList:
                other_person[1] += 1
                
    #add +1 to friend score based on mutual networks in recommend list    
    if person_to_networks != {} and person_to_networks.has_key(person):
        for person_networks in person_to_networks:
            if person != person_networks:
                for network in networkList:
                    if network in person_to_networks[person_networks]:
                        for name in recommend:
                            if name[0] == person_networks:
                                name[1] += 1
                
    #remove all persons with friend score at 0 from recommend list
    for names in recommend:
        for names in recommend:
            if names[1] == 0:
                recommend.remove(names)
            
    #add +1 for all same last name in the recommend list           
    for names in recommend:
        last_name = person[person.find(' ')+1:]
        name_friend = names[0]
        last_name_friend = name_friend[(names[0]).find(' ')+1:]
        if last_name == last_name_friend:
            names[1]+=1
            
        
    #turn all lists into tuple pairs
    for names in range(len(recommend)):
        recommend[names] = tuple(recommend[names])
        
    #remove all zero score friends
    
    final_recommend = []
    for people in recommend:
        if people[1] != 0:
            final_recommend.append(people)
                
    return final_recommend

            
                
    

 
def sort_recommendations(recommendations):
    '''(list of (str, int) tuples) -> list of strs
    Takes the str of the tuple pair in recommendations and sorts them based on the int first, in non-decsending order, then by non-ascending alphabetical order'''
    
    
    recommendations.sort()
    for i in range(len(recommendations)):
        for j in range(0, len(recommendations) - 1 - i):
            if recommendations[j][1] < recommendations[j + 1][1]:
                recommendations[j], recommendations[j + 1] = recommendations[j + 1], recommendations[j]    
                    
    finallist = []
             
    for friend in recommendations:
        finallist.append(friend[0])  
      

    return finallist

	
if __name__ == "__main__":
    d_pp = {'Gloria Pritchett':['Jay Pritchett','Cameron Tucker','Manny Delgado'],'Dylan D-Money':['Haley Gwendolyn Dunphy'],'Haley Gwendolyn Dunphy':['Dylan D-Money']}
    d_pn = {}
    print make_recommendations('Claire Dunphy', d_pp,d_pn)
    
    testlist = [('george d',3),('george d',3),('abra',3),('confusion',3),('steain',3),('steain',3)]
    print sort_recommendations(testlist) 