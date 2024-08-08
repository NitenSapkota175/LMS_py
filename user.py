from db_connector import mycursor

class User:
    
    def __init__(self,user_id , first_name, last_name , phone_number , fines):
        
            self.user_id = user_id
            self.first_name = first_name
            self.last_name = last_name
            self.phone_number = phone_number
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
         


    @classmethod
    def check_borrowings_history(cls,user_id,book_id):
         
         stm = "SELECT * FROM borrowings WHERE user_id = %s"
         mycursor.execute(stm , (user_id,))

         borrowed_history = mycursor.fetchall()
         
         if len(borrowed_history) < 4:
            
            for borrow in borrowed_history:
                if borrow[0] == book_id :

                        return False
            
            return True
                
         else : 
              return False               

         


    def browwer_book(self,book_id):
        self.borrowing_history.append(book_id)
    
   
    
    def view_borrowing_history(self):
        
        if len(self.borrowing_history) > 2:
            return False
        else:
            return True
    
