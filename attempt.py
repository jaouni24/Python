import pandas as pd 

#import the data to dataframe
df = pd.read_csv('prog_book.csv')

#put all the data in the dataframe that has rating >= 4.0
good_books = df[(df['Rating'] >= 4.0)]

#print the number of good books with rating >= 4.0
print('number of good books with rating >= 4.0: '+str(len(good_books))+'\n')

#print number of books in good_books
print('number of books in good_books: '+str(len(good_books['Book_title'].unique()))+'\n')

#print mean value of the number of pages of good_books
print('mean value of the number of pages of good_books: '+str(round((good_books['Number_Of_Pages'].mean()),2))+'\n')

#print Print the first 5 book titles in the good_books data frame
print('the first 5 book titles in the good_books data frame: \n'+str(good_books.head()))