# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 15:28:37 2022

@author: Gabriel
"""
def get_data(url):
    from urllib.request import urlopen
    response = urlopen(url)
    return response.read().decode('utf-8').split("\n")


raw_data = get_data("https://raw.githubusercontent.com/devw/spen/main/docs/scripts/words.txt")  # The Url is a str not a variable.
print(raw_data)


def get_words(data):
    words = []
    for word in data:
        words.append(word.rstrip("\n"))
    return words

words =get_words(raw_data)
words.pop()
print(words)



def get_tree(words,tree=[],j=1,k=2):
        if len(words) >= 3 :
            tree.append((words[0],[j,k]))
            words.pop(0)
            get_tree(words,tree,j+2,k+2)
        else :
            if len(words) >= 2:
                tree.append((words[0],[j,None]))
                words.pop(0)
                get_tree(words,tree,j+2,k+2)
            else :
                tree.append((words[0],[None,None]))
        
        return tree


def main():
    fName = "https://raw.githubusercontent.com/devw/spen/main/docs/scripts/words.txt"  # The Url is a str not a variable.
    raw_data = get_data(fName)
    words = get_words(raw_data)
    words.pop()
    tree = get_tree(words)
    print(tree)

main()