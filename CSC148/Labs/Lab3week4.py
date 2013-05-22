def is_palindrome (input_string):
    if (len(input_string) == 1 or len(input_string) == 0):
        return True

    if input_string[0] == input_string[-1]:
        return is_palindrome(input_string[1:-1])
    else:
        return False

def binary_rep(input_int):
    output_string =''
    output_string = output_string +str(input_int % 2)
    input_int = input_int // 2
    if (input_int == 0):
        #output_string = "0" + output_string
        return output_string
    if(input_int == 1):
        output_string = "1" + output_string
        return output_string
    else:
        return binary_rep(input_int) + output_string
    
def anagrams (input_string):
    res = []
    if (len(input_string) == 1):
        res.append(input_string)
    else:
        for element in input_string:
            res2 = anagrams(input_string[1:])
            for e2 in res2:
                res.append(element + e2)
            
    return res

if __name__ == '__main__':
    print (is_palindrome("mom"))
    print (is_palindrome("racecar"))
    print (is_palindrome("kinnikinnik"))
    print (is_palindrome("kinn"))
    print (is_palindrome("kiafenk"))
    print (is_palindrome("kiafiak"))
    print (is_palindrome("kaifiak"))
    
    print (binary_rep(0))
    print (binary_rep(1))
    print (binary_rep(2))
    print (binary_rep(3))
    print (binary_rep(4))
    print (binary_rep(5))
    print (binary_rep(6))
    print (binary_rep(7))
    print (binary_rep(254))
    
    anagrams("horse")
    print("------smart------")
    anagrams("smart")
    print ("-----cat-----")
    anagrams("cat")
    print (len(anagrams("cat")))