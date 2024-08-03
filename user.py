class User:
    
    def __int__(self,user_id , name , contact_information):
        
            self.user_id = user_id
            self.name = name
            self.contact_information = contact_information
            self.borrowing_history = []
            self.fines = 0
        
        
    def browwer_book(self,book_id):
        self.borrowing_history.append(book_id)
    
    def return_book(self):
        pass
    
    def view_borrowing_history(self):
        
        if len(self.borrowing_history) > 2:
            return False
        else:
            return True
    
    def pay_fine(self):
        pass
    