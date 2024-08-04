import csv
class Book:
    
    ___CSV_FILE = "list_of_books.csv"
    __list_of_books = []
    def __init__(self, book_id,title,author,publisher,publication_year,genre,availability,quantity ):
        
        self.book_id  = book_id
        self.title = title
        self.author = author 
        self.publisher = publisher
        self.publication_year = publication_year
        self.genre = genre
        self.availability= availability 
        self.quantity  = quantity 
        
    
    @classmethod
    def initialize_books(cls):
        
        try:
            with open(Book.___CSV_FILE,'r') as csv_file:
                csv_read_books =  csv.DictReader(csv_file)

                for book in csv_read_books:
                        book_temp = Book(book["book_id"],book["title"],book["author"],book["publisher"],book["publication_year"],book["genre"],book["availability"],book["quantity"])
                        
                        Book.__list_of_books.append(book_temp)
                        
            
   
               
        except FileNotFoundError:
            print("File doesnot exists")
        
        
    @classmethod
    def list_of_all_books(cls):
            
            for book in Book.__list_of_books:
                print(f"Book Id : {book.book_id} , Book Title : {book.title[0:6]} , Publication_year : {book.publication_year} , Genre : {book.genre[0:5]},\t Availability : { book.availability } , Quantity  : {book.quantity}" )

    @classmethod
    def list_of_all_books(cls):
        return cls.__list_of_books


Book.initialize_books()     