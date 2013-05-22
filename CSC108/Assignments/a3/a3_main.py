import a3_functions
       
if __name__ == '__main__':
    
    # During testing, we may change the values of these variables.
    friendships = {}
    networks = {}
    profiles_file = open('profiles.txt')

    # Add your code here.  
    person = 0
    while person != '':
        a3_functions.load_profiles(profiles_file, friendships, networks)
        person = raw_input("Please enter a person(or press return to exit):")
        recommendations = a3_functions.make_recommendations(person, friendships,networks)
        if recommendations == [] and person != '':
            print "There are no recommendations for this person."
            
        else:
            recomlist = a3_functions.sort_recommendations(recommendations)
            for names in recomlist:
                print names
            
            
 
        
    print "Thank you for using the recommendation system!"
    