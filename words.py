"""Retrieve and print words from a URL.
    
    Usage:
       python3 words.py <URL>
 """


import sys
from urllib.request import urlopen #access urlopen by importing function from request module w/in standard library urllib package

def fetch_words(url):
    """Fetch a list of words from a URL.

        Args:
            url: the URL of a UTF-8 text document.
            
        Returns:
            A list of strings containing the words from the document.
    
    """
    # url = urlopen('http://sixty-north.com/c/t.txt')
    # story = urlopen('http://sixty-north.com/c/t.txt') #calling urlopen w/a url to our story
    story = urlopen(url)
    story_words = [] #created an empty list that will hold all words from the text
    for line in story:
        line_words = line.decode('utf8').split() #must decode by uses bytes.decode() to get list of strings instead of list of bytes objects
        # print(line_words)  # Debug statement #prints story each word in separate quotes
        for word in line_words: #nested for loop within a for loop to iterate over list of words
            story_words.append(word) #appending each word to story words list      
    story.close()
    return story_words

def print_items(items):
    """Print items one per line. 
        Args: 
            an iterable series of printable items.
    """
    for item in items:
        print(item) #prints one word on each line

 
def main(url):
    """Print each word from a text document from at a URL.

    Args:
        url: The URL of a UTF-8 text document.
    """
    # url = sys.argv[1] #argv is a list of strings in the sys module. must import sys to access. [1] gets second argument with index of 1 from list.
    words = fetch_words(url)
    print_items(words)  
    # print('http://sixty-north.com/c/t.txt') #actually in the terminal you type python words.py http://sixty-north.com/c/t.txt
    
    

# if __name__ == '__main__':  #if dunder name is equal to dunder main we execute our function, but if it's not the module knows it's being imported into another module,  not executed, so it will only define fetch_words func without executing it.
#     fetch_words()

#pass into main function so that we can test 
if __name__ == '__main__':
    main(sys.argv[1]) #The 0th arg is the module filename, that's why we are using 1 instead of 0.