import csv
from user import User
from books import Book
from db_connector import mycursor,mydb
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
                         
                        if User.check_borrowings_history(user_id,book_id) and Book.get_book_by_Id(book_id):
                                    
                                    LMS.borrow_books(user_id , book_id)

                        else:
                                print("you cannot borrow")
                        
                else:
                        print("User not present")


    @classmethod
    def borrow_books(cls , user_id , book_id):
            
            issue_date = datetime.date.today()
            return_date = issue_date + datetime.timedelta(days=14)
            
            stm = "INSERT INTO borrowings VALUES(%s,%s , %s,%s)"
            mycursor.execute(stm, (book_id,user_id,issue_date,return_date))
            mydb.commit()



            for book in cls.list_of_books:
                    if book.book_id == book_id : 
                            stm = "UPDATE books SET quantity = %s WHERE book_id = %s"
                            mycursor.execute(stm , ((book.quantity - 1) , book_id))
                            book.quantity = book.quantity - 1
                            mydb.commit()
                            break


    @classmethod
    def return_books(cls,user_id,book_id):
            


            stm = "SELECT issue_date , return_date FROM borrowings WHERE user_id=%s and book_id=%s"
            mycursor.execute(stm , (user_id,book_id))
            borrow_dates = mycursor.fetchone()
            if borrow_dates: 
                issue_date , return_date = borrow_dates
                if return_date <= datetime.date.today() and  (issue_date < return_date and return_date > datetime.date.today()) :
                        LMS.delete_borrowing_records(user_id,book_id)
                        print("thankyou for return the book on time")
                
                #     if return_date > issue_date + datetime.timedelta(14):
                else:
                            print("You have return late and charged with fine") 
                            LMS.pay_fine()
            else:
                    print("Record not found")


    @classmethod
    def delete_borrowing_records(cls, user_id ,book_id):
               
               
                    stm = "DELETE FROM borrowings WHERE user_id=%s and book_id=%s"
                    mycursor.execute(stm , (user_id,book_id))
                    mydb.commit()

                    for book in cls.list_of_books:
                            
                            if book.book_id == book_id : 
                                    stm = "UPDATE books SET quantity = %s WHERE book_id = %s"
                                    mycursor.execute(stm , ((book.quantity +1) , book_id))
                                    book.quantity = book.quantity + 1
                                    mydb.commit()
                                    break
                            

    @classmethod 
    def pay_fine(cls):
                pass