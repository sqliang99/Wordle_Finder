#word finding function

import word_list
import collections
import random

def find_wordle(avoid,*args,**kwargs):
    '''
    a function to find words from the wordle list 
    can pass down letters that are present in the word
    and letters that are in the word with set position
    '''
    new_kwargs = {}
    for key in kwargs.keys():
        if key == 'first':
            new_kwargs[0] = kwargs[key]
        if key == 'second':
            new_kwargs[1] = kwargs[key]
        if key == 'third':
            new_kwargs[2] = kwargs[key]
        if key == 'fourth':
            new_kwargs[3] = kwargs[key]
        if key == 'fifth':
            new_kwargs[4] = kwargs[key]
    
    
    
    o = [word for word in word_list.word_list if all(letter in word for letter in args) and all(value == word[key] for key,value in new_kwargs.items())]
    output = [word for word in o if all(letter not in word for letter in avoid)]
    if len(output) > 0:
         return output
    else:
        print("Seems like there's no word for this")

def max_info(args2,*args,**kwargs):
    words = find_wordle(args2,*args,**kwargs)
    cnt = collections.Counter()
    scores = collections.Counter()
    for word in list(words):
        for letter in set(word):
            cnt[letter]+=1
    
    ignore = list(args)+list(kwargs.values())
    ignore = set(ignore)
    for i in ignore:
        del cnt[i]
    print(cnt)
    
    for w in words:
        for l in cnt.keys():
            if l in w:
                scores[w]+=cnt[l]
    
    lucky = [k for k, v in scores.items() if v == max(scores.values())]
    
    return random.choice(lucky)
