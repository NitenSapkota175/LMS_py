import csv
from user import User
from books import Book
from db_connector import mycursor
import datetime
# Book.list_of_all_books()               

class LMS:
    
    list_of_books = Book.get_all_books()
    list_of_user = User.get_all_users()

    @classmethod
    def all_book_list(cls):
            
            print("\t\tName")
            for books in cls.list_of_books:
            
                    print(f"\t\t {books.title} \t\t \t\t{books.author}")
            
    @classmethod
    def issue_book(cls,user_id,book_id):

                if User.get_user_by_Id(user_id) :
                         LMS.borrow_books(user_id , book_id)
                        
                else:
                        print("User not present")


    @classmethod
    def borrow_books(cls , user_id , book_id):
            
            issue_date = datetime.date.today()
            return_date = issue_date + datetime.timedelta(days=14)
            
            stm = "INSERT INTO borrowings VALUES(%s,%s , %s,%s)"
            mycursor.execute(stm, (book_id,user_id,issue_date,return_date))
            



    
    def return_books(self):
            pass