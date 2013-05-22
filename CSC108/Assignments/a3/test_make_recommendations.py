import nose
import a3_functions

def test_make_recommendations_empty_string_and_dict():
    d_pp = {}
    d_pn = {}
    
    assert a3_functions.make_recommendations('', d_pp,d_pn) == [], \
           'Empty String and both empty dictionaries'
    
def test_make_recommendations_empty_string():
    d_pp = {'s m':[],'A g':['F p','A d','T-32'],'F p':['A g','A d'],'Z b':['T=32','A D']}
    d_pn = {'s m':[],'A g':['milliways restaurant','planet freepress','hitchhikers guild'], 'A D':['planet freepress','hitchhikers guild']}
    
    assert a3_functions.make_recommendations('', d_pp,d_pn) == [], \
           'Empty String '
    
def test_make_recommendations_empty_dictionaries():
    d_pp = {}
    d_pn = {}
    
    assert a3_functions.make_recommendations('Marvin So-Sad', d_pp,d_pn) == [], \
           'Empty dictionaries'
    
def test_make_recommendations_one_empty_dictionary():
    d_pp = {}
    d_pn = {'a':['fefd']}
    
    assert a3_functions.make_recommendations('Marvin So-Sad', d_pp,d_pn) == [], \
           'one empty dictionary'

def test_make_recommendations_no_mutual_friend_or_networks():
    d_pp = {'s m':[],'A g':['F p','A d','T-32'],'F p':['A g','A d'],'Z b':['T=32','A D']}
    d_pn = {'s m':[],'A g':['milliways restaurant','planet freepress','hitchhikers guild'], 'A D':['planet freepress','hitchhikers guild']}
    
    assert a3_functions.make_recommendations('s m', d_pp,d_pn) == [], \
           'No mutual friends or networks'
    
def test_make_recommendations_one_mutual_friend_no_mutual_networks():
    d_pp = {'s m':['F p'],'A g':['F p','A d','T-32'],'F p':['A g','A d'],'Z b':['T=32','A D']}
    d_pn = {'s m':[],'A g':['milliways restaurant','planet freepress','hitchhikers guild'], 'A D':['planet freepress','hitchhikers guild']}
    
    assert a3_functions.make_recommendations('s m', d_pp,d_pn) == [('A g',1)], \
           'one mutual friend and no mutual network'


def test_make_recommendations_one_mutual_friend_one_mutual_networks():
    d_pp = {'s m':['F p'],'A g':['F p','A d','T-32'],'F p':['A g','A d'],'Z b':['T=32','A D']}
    d_pn = {'s m':['milliways restaurant'],'A g':['milliways restaurant','planet freepress','hitchhikers guild'], 'A D':['planet freepress','hitchhikers guild']}
    
    assert a3_functions.make_recommendations('s m', d_pp,d_pn) == [('A g',2)], \
           'one mutual friend and one mutual network'

def test_make_recommendations_one_mutual_friend_same_last_name():
    d_pp = {'Arthur Dent':['Ford Prefect'], 'Trillian Dent':['Ford Prefect']}
    d_pn = {}
    assert a3_functions.make_recommendations('Arthur Dent', d_pp,d_pn) == [('Trillian Dent',2)], \
           'one mutual friend and same last name and empty networks dictionary'
    
def test_make_recommendations_one_mutual_friend_and_network_same_last_name():
    d_pp = {'Arthur Dent':['Ford Prefect'], 'Trillian Dent':['Ford Prefect']}
    d_pn = {'Arthur Dent':['milliways'],'Trillian Dent':['milliways']}
    assert a3_functions.make_recommendations('Arthur Dent', d_pp,d_pn) == [('Trillian Dent',3)], \
           'one mutual friend and network, and same last name'
    
def test_make_recommendations_one_mutual_network_same_last_name():
    d_pp = {'Arthur Dent':['Ford Prefect'], 'Trillian Dent':['Ford']}
    d_pn = {'Arthur Dent':['milliways'],'Trillian Dent':['milliways']}
    assert a3_functions.make_recommendations('Arthur Dent', d_pp,d_pn) == [('Trillian Dent',2)], \
           'one mutual network and same last name, no mutual friends'
    
def test_make_recommendations_multiple_friends_empty_networks():
    d_pp = {'a':['b','c','d'],'q':['b','c'],'d':['a','q'],'h':['c','d']}
    d_pn = {}
    
    assert a3_functions.make_recommendations('a', d_pp,d_pn) == [('q',2),('h',2)], \
           'multiple mutual friends and empty no mutual networks'
    
def test_make_recommendations_multiple_networks():
    d_pp = {'a':[],'q':[],'d':[],'h':[]}
    d_pn = {'a':['b','c','d'],'q':['b','c'],'d':['a','q'],'h':['c','d']}
    
    assert a3_functions.make_recommendations('a', d_pp,d_pn) == [('q',2),('h',2)], \
           'multiple mutual networks and no mutual friends'
    
def test_make_recommendations_multiple_networks_and_friends():
    d_pp = {'a':['b','c','d'],'q':['b','c'],'d':['a','q'],'h':['c','d']}
    d_pn = {'a':['b','c','d'],'q':['b','c'],'d':['a','q'],'h':['c','d']}
    
    assert a3_functions.make_recommendations('a', d_pp,d_pn) == [('q',4),('h',4)], \
           'multiple mutual networks and multiple friends'
    
def test_make_recommendations_multiple_networks_and_friends_samelnames():
    d_pp = {'a B-3-df joe':['b','c','d'],'q B-3-df joe':['b','c'],'d':['a','q'],'h':['c','d']}
    d_pn = {'a B-3-df joe':['b','c','d'],'q B-3-df joe':['b','c'],'d':['a','q'],'h':['c','d']}
    
    assert a3_functions.make_recommendations('a B-3-df joe', d_pp,d_pn) == [('q B-3-df joe',5),('h',4)], \
           'multiple mutual networks and multiple friends and last names'
    
def test_make_recommendations_multiple_networks_and_friends():
    d_pp = {'Claire Dunphy':['a','b','c'],'a b Dunphy':['yo-o'],'yo-o':['a b Dunphy']}
    d_pn = {}
    
    assert a3_functions.make_recommendations('Claire Dunphy', d_pp,d_pn) == [], \
           'multiple mutual networks and multiple friends and last names'
    
    
def test_make_recommendations_multiple_networks_and_friends():    
    d_pp = {'Gloria Pritchett':['Jay Pritchett','Cameron Tucker','Manny Delgado'],'Dylan D-Money':['Haley Gwendolyn Dunphy'],'Haley Gwendolyn Dunphy':['Dylan D-Money']}
    d_pn = {}
    assert a3_functions.make_recommendations('Gloria Pritchett', d_pp,d_pn)== [], \
           'Common names'
    
if __name__ == '__main__':
    nose.runmodule()