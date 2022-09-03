# Stats based Text Generator

# Install the needed libraries 

```
import os
from ebooklib import epub
import ebooklib
import random
```
os and random are Python libraries that should already be on your system. We will also use ebooklib which you can use pip to install and see the documentation for it at these links:

https://pypi.org/project/EbookLib/
https://docs.sourcefabric.org/projects/ebooklib/en/latest/

# Collect the books that we are going to read through
Navigate to this website and download all of the books there in epub format and place them in a 'books' directory within your coding directory. Some of the links will direct you to another page to select which format you would like. 

https://concretecomputing.com/thoughts/list-of-public-domain-free-books-for-kids-by-grade-level/

# Parse the books and just extract the text
The first thing we need to do is read through the epub books and extract the text within. epub format uses html style formatting so we can look for certain things that will anchor the text we are searching for. 

To filter out some of the content, create an ignore list of classes to not read in. 
```
ignore_list = ["<class 'ebooklib.epub.EpubImage'>","<class 'ebooklib.epub.EpubItem'>"]
```
Now, iterate through each book in your 'books' directory. There are other methods for decoding the books that might work better for you, but I used the epublib doc class to grab the content and decode it. 

```
doc_content = doc.content.decode()
```
Use the nextline '\n' symbol as a delimiter to break down the doc_conent. We can now read each line of the list and look for the paragraph '<p>' symbol to capture the sentences we want. A little bit of cleaning is needed at this point as well. Replace all of the punctuation makes with periods. In this case, it won't matter/we are not looking at that for relevance. Additionally, due to some of these books being of a different time, they appear to have been fans of using ';' to string together multiple sentences. I ended up splitting them into different sentences for this use case. 
Another thing to clean is hyperlinks, bold, and italic by removing them. 
  
# Building the corpus
Just like you would do for machine learning, we will build out a corpus that assigns an integer value to each word while reserving the value of 0 for a blank word. We also need to remove all punctuation from the sentences so that is doesn't duplicate words with those contained. 
I ended up creating two dictionaries here, one for the corpus and one for a reverse corpus. The corpus keys are the integers with the values as words and the reverse is true for the latter. 
  
# Convert text to corpus values
Take all of the sentences that we collected from the books eariler and convert those to the integer values. This will create an array of values that represent the words. 
We will then read through each array and determine the longest sentence that was read. Once the max length of the sentences is obtained, iterate back through and pad each array/sentence so that they are all the same length. 
  
  
# Create position dictionaries
We are now going to find each word in each position, the count of that word in that position, and the fraction of the time that word appears in that position across all of the sentences we read in (these are added to one another to total 1 so that we can use them statistically later on). 
 
There are multiple position dictionaries (1,2,3,4) with each becoming better at generating senences as they increase in value. The first only takes into account the current position, where as the others increasingly look back one position in the sentence to determine the current word. 

# Sentence Generation 
There are a couple of parameters at the start here
```
full_sent = ''
full_sent_len = 0
random_base = 0
```
These work within the while look to make sure that a sentence is actually generated in each run (as there is a possibility that no sentence will be made). Therefore, set the while loop to look for a sentence length of greater than 0. 
  
Since we calculated the max length before, we will use that to iterate through the positions for filling in the words. You can modify this section to only use certain dictionaries, but be aware that if you use 2+ that you need to make sure that you either generate the positions they are looking back towards or use one of the smaller dictionaries to fill that position. 
  
We will also use a random number generator between a minimum and 1 (again, due to the fact that it could potentially not generate a sentence). 
  
The script will now use that random value in combination with the current position in the sentence to assign the word based on its fractional representation. For example, if the position had 5 'the', 3 'and', and 2 'from' their fractions would be (0.5,0.8,1) respectively. If the random number generated was 0.834, the word would be assigned to 'from' since it is between 0.8 and 1. For the higher number dictionaries, it will use values that are stored in previous positions to determine the current position word. 
  
We then append the values to the current sentence array as well as the sentence string. Additionally, if the sentence didn't produce any values then the random base is incremented so that it approaches 1. 
  
# Display Sentences
Now, read through the array and create the sentence. 
  
# Note
The script does seem to favor the sentence below. To generate another sentence, simply continue to run the make_sent() function. 
  
```
folklore legends myths and fairy tales have followed childhood through the ages for every healthy youngster has a wholesome and instinctive love for stories fantastic marvelous and manifestly unreal 
```
