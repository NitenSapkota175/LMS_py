from books import books
from lms import LMS
from user import User
def main():
    lib = LMS()

    user1 = User(1,"Niten","7908039176")
    lib.issue_book(user1,"1")


if __name__ == "__main__":
    main()