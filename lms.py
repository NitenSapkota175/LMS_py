import csv
from user import User
from books import Book
# Book.list_of_all_books()               

class LMS:
    
    def __init__(self):
        
        self.book_list = Book.list_of_all_books()
        self.user = []
    
    def issue_book(self,user,book_id):
                pass        