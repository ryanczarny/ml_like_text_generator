from ebooklib import epub
import os
import random
import ebooklib

ignore_list = ["<class 'ebooklib.epub.EpubImage'>","<class 'ebooklib.epub.EpubItem'>"]

all_books = []
for filename in os.listdir('books/'):
    if filename.endswith('.epub'):
        book = epub.read_epub('books/' + filename)
        book_text = ''
        for doc in book.get_items():
            if not str(type(doc)) in ignore_list:
                doc_content = doc.content.decode()
                book_text += doc_content
        book_text = book_text.split('\n')
        for line in book_text:
            if line.startswith('<p>'):
                line = line.replace('<p>','').replace('</p>','')
                line=line.replace(';','.').replace('!','.').replace('?','.')
                line = line.split(".")
                for sent in line:
                    if sent.startswith(" "):
                        sent = sent[1:]
                    if sent.endswith(" "):
                        sent = sent[:-1]
                    html = 0
                    while html == 0:
                        try:
                            sent_start = sent.split('<a')[0]
                            sent_end = sent.split('</a>')[1]
                            sent = sent_start + sent_end
                        except:
                            html = 1
                    
                    sent = sent.replace('<i>','').replace('</i>','').replace('<b>','').replace('</b>','')
                    if len(sent) > 1 and sent != '<br/>':
                        all_books.append(sent.lower())

# corpus = {}
# reverse_corpus = {0:''}
# counter=1
# punct = ['!','"','#','$','%','&',"'",'(',')','*','+',',','-','.','/',':',';','<','=','>','?','@','[','\\',']','^','_','`','{','¦','}','~']
# for sent in all_books:
#     for punc in punct:
#         sent=sent.replace(punc,' ')
#     sent=sent.split(' ')
#     for word in sent:
#         if not word in corpus and word != ' ' and len(word) > 0:
#             corpus[word]=counter
#             reverse_corpus[counter]=word
#             counter+=1

# all_books_indexed = []
# for sent in all_books:
#     temp_list = []
#     for punc in punct:
#         sent=sent.replace(punc,' ')
#     sent=sent.split(' ')
#     for word in sent:
#         try:
#             temp_list.append(corpus[word])
#         except:
#             continue
#     all_books_indexed.append(temp_list)

# max_length = 0
# for i in all_books_indexed:
#     if len(i) > max_length:
#         max_length = len(i)

# max_length = 0
# for i in range(len(all_books_indexed)):
#     if len(all_books_indexed[i]) > max_length:
#         max_length = len(all_books_indexed[i])

# for i in range(len(all_books_indexed)):
#     while len(all_books_indexed[i]) < max_length:
#         all_books_indexed[i].insert(0,0)

# position_dict = {}
# for sent in all_books_indexed:
#     for i in range(max_length):
#         if not i in position_dict:
#             position_dict[i] = [{}]
#         if not sent[i] in position_dict[i][0]:
#             position_dict[i][0][sent[i]]=1
#         else:
#             position_dict[i][0][sent[i]]+=1

# for position in position_dict:
#     total = 0
#     temp_list = []
#     temp_word_list = []
#     for word in position_dict[position][0]:
#         count = position_dict[position][0][word]
#         temp_list.append(count)
#         temp_word_list.append(word)
#         total += count
#     for i in range(len(temp_list)):
#         temp_list[i] = temp_list[i]/total
#         if i >= 1:
#             temp_list[i] += temp_list[i-1]
#     position_dict[position].append(temp_list)
#     position_dict[position].append(temp_word_list)
# total_sents = total

# full_sentence = []
# for i in range(max_length):
#     rand_num = random.random()
#     print(rand_num)
#     position_weights = position_dict[i][1]
#     print(position_weights)
#     indexer = 0
#     for x in range(len(position_weights)):
#         if rand_num > position_weights[x]:
#             indexer = x
#     print(indexer)
#     full_sentence.append(reverse_corpus[position_dict[i][2][indexer]])

# print(full_sentence)