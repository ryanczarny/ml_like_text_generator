# filename = open('pg2591.epub')

# import ebooklib
# from ebooklib import epub
# book = epub.read_epub('pg2591.epub')
# items = list(book.get_items_of_type(ebooklib.ITEM_DOCUMENT))

# all_items = book.get_items()

# print(all_items)

from ebooklib import epub
import os
import ebooklib
import os
import nltk

ignore_list = ["<class 'ebooklib.epub.EpubImage'>","<class 'ebooklib.epub.EpubItem'>"]

book_corpus = []
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
                all_books.append(line)

