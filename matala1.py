# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 15:06:48 2023

@author: buki2
"""

####### q1
def my_func(x1,x2,x3):
    try:
          up = (x1+x2+x3)*(x2+x3)*x3
          down = x1+x2+x3
          if down == 0:
              return print('Not a number – denominator equals zero')
          if (type(x1) is int or type(x2) is int or type(x3) is int):
              return print('Error: parameters should be float')
          else: 
              func =  up/down
              return func
    except TypeError: 
        return print(None)
        
     
        
x1 = 's'
x2 = 0
x3 = 0
my_func(x1, x2, x3)

###############q2

def revword(word):
    word=''.join(reversed(word))
    word = word.lower()
    return word
    
def countword():
    counter = 1
    fh = open('text.txt')
    for line in fh:
        lineWords = line.split()
        my_word = lineWords[0]
        break
    for line in fh:
        lineWords = line.split()
        if len(lineWords) == 1:
            continue
        for word in lineWords:
            word = revword(word)
            if word == my_word:
                counter +=1
    return counter
    
        
        
dan = "hWord"  
print(revword(dan))    
print(countword())