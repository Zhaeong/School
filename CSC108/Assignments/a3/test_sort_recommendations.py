import nose
import a3_functions

def test_sort_recommendations_empty():
    testlist = []
    assert a3_functions.sort_recommendations(testlist) == [], \
           "Empty List"
    
    
def test_sort_recommendations_one_tuple():
    testlist = [('george',3)]
    assert a3_functions.sort_recommendations(testlist) == ['george'], \
           "One tuple"
    
def test_sort_recommendations_multiple_tuples():
    testlist = [('george',3),('abra',3),('confusion',8),('steain',1)]
    assert a3_functions.sort_recommendations(testlist) == ['confusion','abra','george', 'steain'], \
           "Multiple tuples"

def test_sort_recommendations_multiple_tuples_duplicate_names():
    testlist = [('george',3),('abra',3),('confusion',8),('steain',1),('steain',5)]
    assert a3_functions.sort_recommendations(testlist) == ['confusion','steain','abra','george','steain'], \
           "Multiple tuples, duplicate names"
    
def test_sort_recommendations_multiple_tuples_duplicate_tuples():
    testlist = [('george d',3),('george d',3),('abra',3),('confusion',8),('steain',1),('steain',3)]
    assert a3_functions.sort_recommendations(testlist) == ['confusion','abra','george d','george d','steain','steain'], \
           "Multiple duplicate tuples"
    
def test_sort_recommendations_all_duplicate_tuples():
    testlist = [('george d',3),('george d',3),('george d',3),('george d',4),('george d',1),('george d',3)]
    assert a3_functions.sort_recommendations(testlist) == ['george d','george d','george d','george d','george d', 'george d'], \
           "All duplicate tuples"
    
def test_sort_recommendations_all_same_score():
    testlist = [('george d',3),('george d',3),('abra',3),('confusion',3),('steain',3),('steain',3)]
    assert a3_functions.sort_recommendations(testlist) == ['abra','confusion','george d','george d','steain', 'steain'], \
           "All same score"
    
    
if __name__ == '__main__':
    nose.runmodule()