from books import Book
from lms import LMS
from user import User
def main():

    LMS.all_book_list()
    # LMS.issue_book(1,4)
    LMS.return_books(2,2)
    # Book.get_all_books()  
    # User.get_all_users()



    # user1 = User(1,"Niten","7908039176")
    # lib.issue_book(user1,"1")


if __name__ == "__main__":
    main()