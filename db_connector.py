from dotenv import load_dotenv
import os
import mysql.connector

# Load environment variables from .env file
load_dotenv()

# Connect to the database using environment variables
mydb = mysql.connector.connect(
    host=os.getenv('DB_HOST'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD'),
    database=os.getenv('DB_NAME')
)

mycursor = mydb.cursor()
