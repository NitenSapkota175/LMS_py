from db_connector import mycursor

class User:
    
    def __init__(self,user_id , first_name, last_name , phone_number , fines):
        
            self.user_id = user_id
            self.first_name = first_name
            self.last_name = last_name
            self.phone_number = phone_number
            self.borrowing_history = []
            self.fines = fines
        
    @classmethod
    def get_all_users(cls):

            mycursor.execute("SELECT * FROM users")
            users = mycursor.fetchall()
            
            all_users = []
            for user in users:
                all_users.append(User(*user))

            return all_users

    @classmethod 
    def get_user_by_Id(cls,user_id):
        
         stmt = "SELECT * FROM users WHERE user_id=%s"
         mycursor.execute(stmt, (user_id,))

         user = mycursor.fetchone()
         if user ==  None:
                return False
         
         return True
         





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
    