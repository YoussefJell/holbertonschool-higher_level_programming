#!/usr/bin/python3
def multiple_returns(sentence):
    my_Tuple = ()
    if not sentence:
        my_Tuple = (len(sentence), None)
        return my_Tuple
    else:
        my_Tuple += (len(sentence), sentence[0])
        return my_Tuple
