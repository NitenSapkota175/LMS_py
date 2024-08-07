import csv
from db_connector import mycursor
class Book:
    
  
    def __init__(self, book_id,title,author,publication_year,genre,availability,quantity):
        
        self.book_id  = book_id
        self.title = title
        self.author = author 
        self.publication_year = publication_year
        self.genre = genre
        self.availability= availability 
        self.quantity  = quantity 
        
    
    @classmethod
    def get_all_books(cls):
            
            
            mycursor.execute("SELECT * FROM books")
            books = mycursor.fetchall()

            book_objects = []
            for book in books:
                book_objects.append(Book(*book))      

            return book_objects


    @classmethod
    def get_book_by_Id(cls,book_id):
         
         books = Book.get_all_books()

         for book in books:
              if book.book_id == book_id and book.quantity > 0:
                   return True
         else:
            return False

        
        
 


