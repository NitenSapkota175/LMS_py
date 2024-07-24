import datetime
import os
class LMS:
    "this class will act as source code for 4 modules displaybooks,addbooks,returnbooks and isssue books"
    
    def __init__(self,list_of_books,library_name):
        self.list_of_books = list_of_books
        self.library_name = library_name
        self.bookId = 101
        self.book_dict= {}
        content = None
        with open(self.list_of_books) as bk:
            content = bk.readlines()
        for books in content:
            self.book_dict.update({str(self.bookId) : { "Book_title" : books.replace("\n","") , "lender_name" :"" , "Issue_date" : ""  , "status" : "Available" } })
            self.bookId +=1

    def Display_books(self):
        print("-------------------List of Books-------------------- ")
        print("\t\t Book title \t\t\t\t\t\t status")
        for key , value in self.book_dict.items():
                print(key," \t ",value.get("Book_title") ,"\t\t\t",value.get("status"))

obj1 = LMS("list_of_books.txt","Niten")
obj1.Display_books()
        
    