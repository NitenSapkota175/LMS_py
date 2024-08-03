import csv
from user import User
from books import Book
# Book.list_of_all_books()               

class LMS:
    
    def __init__(self):
        
        self.book_list = Book.list_of_all_books()
        self.user = []
    
    def issue_book(self,user,book_id):
        
        for book in self.book_list:
            
            if book.book_id == book_id and (book.availability.lower()) == "available" :

                if user.fine == 0 and user.view_borrowing_history():
                        user.browwer_book(book_id)              
                    
                else:
                    print("You cannot borrow book right now")
            
           


lib = LMS()

user1 = User(1,"Niten","7908039176")
lib.issue_book(user1,"1")
        