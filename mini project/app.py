print("database mini project")
import sqlite3 as sq
import pandas as pd

connection=sq.connect("myappdatabase.db")
my_cursor=connection.cursor()
# users_table
my_cursor.execute('CREATE TABLE IF NOT EXISTS users (user_name TEXT, user_id INTEGER PRIMARY KEY)')

user1= ("Ali Khan",1)
user2= ("Sara Ahmed",2)
user3= ("Ahmed Raza",3)
user4= ("Ayesha Malik",4)
user5=  ("Usman tariq",5)
users_list=[user1,user2,user3,user4,user5]
my_cursor.executemany('INSERT OR IGNORE INTO users VALUES (?,?)',users_list)
connection.commit()

my_cursor.execute('SELECT * FROM users')
usrs_result=my_cursor.fetchall()
users_df=pd.DataFrame(usrs_result)
print(users_df)

# conversation table 
my_cursor.execute("CREATE TABLE IF NOT EXISTS conversations (convo_title TEXT ,convo_id INTEGER PRIMARY KEY,user_id INTEGER, FOREIGN KEY(user_id) REFERENCES users(user_id))")
#each user can have multiple conversations
convo1=("Python Learning",1,1)
convo2=("AI Chatbot Project",2,1)
convo3=("Job Search",3,2)
convo4=("React Basics",4,2)
convo5=("Database Design",5,3)
convo6=("Interview Preparation",6,3)
convo7=("Resume Improvement",7,4)
convo8=("Web Development",8,4)
convo9=("SQL Practice",9,5)
convo10=("Career Guidance",10,5)
convo_list=[convo1,convo2,convo3,convo4,convo5,convo6,convo7,convo8,convo9,convo10]
my_cursor.executemany('INSERT OR IGNORE INTO conversations VALUES (?,?,?)',convo_list)
my_cursor.execute('SELECT * FROM conversations')
convo_res=my_cursor.fetchall()
convo_df=pd.DataFrame(convo_res)
print(convo_df)

#msgs_table
my_cursor.execute("CREATE TABLE IF NOT EXISTS messages (each_msg TEXT ,eachmsg_id  INTEGER PRIMARY KEY,convo_id INTEGER, FOREIGN KEY(convo_id) REFERENCES conversations(convo_id))")
msg1 = ("How do I learn Python?", 1, 1)
msg2 = ("Start with Python basics.", 2, 1)

msg3 = ("How can I build an AI chatbot?", 3, 2)
msg4 = ("You can use Python and an LLM API.", 4, 2)

msg5 = ("How should I search for jobs?", 5, 3)
msg6 = ("Start by identifying your target roles.", 6, 3)

msg7 = ("What are React components?", 7, 4)
msg8 = ("Components are reusable UI building blocks.", 8, 4)

msg9 = ("What is database design?", 9, 5)
msg10 = ("It is the process of organizing data into tables.", 10, 5)

msg11 = ("How should I prepare for interviews?", 11, 6)
msg12 = ("Practise technical and behavioral questions.", 12, 6)

msg13 = ("How can I improve my resume?", 13, 7)
msg14 = ("Highlight your projects and technical skills.", 14, 7)

msg15 = ("What is web development?", 15, 8)
msg16 = ("It involves building websites and web applications.", 16, 8)

msg17 = ("Explain SQL JOIN.", 17, 9)
msg18 = ("JOIN combines related records from multiple tables.", 18, 9)

msg19 = ("How can I improve my career?", 19, 10)
msg20 = ("Focus on building skills and gaining experience.", 20, 10)

msgs_list = [
    msg1, msg2, msg3, msg4, msg5,
    msg6, msg7, msg8, msg9, msg10,
    msg11, msg12, msg13, msg14, msg15,
    msg16, msg17, msg18, msg19, msg20
]
my_cursor.executemany('INSERT OR IGNORE INTO messages VALUES (?,?,?)',msgs_list)

my_cursor.execute('SELECT * FROM messages')
msgs_result=my_cursor.fetchall()
msgs_df=pd.DataFrame(msgs_result)
print(msgs_df)


# document meta data table 
my_cursor.execute('CREATE TABLE IF NOT EXISTS documents (document_id INTEGER PRIMARY KEY, user_id INTEGER, filename TEXT, file_type TEXT, upload_date INTEGER, FOREIGN KEY (user_id) REFERENCES users (user_id))')
doc_data1=(1, 1, "python_notes.pdf", "pdf", "2026-10-25")
doc_data2=(2, 1, "ai_chatbot.docx", "docx", "2026-10-26")
doc_data3= (3, 2, "react_basics.pdf", "pdf", "2026-10-26")
doc_data4=(4, 2, "resume.pdf", "pdf", "2026-10-27")
doc_data5=(5, 3, "sql_guide.txt", "txt", "2026-10-28")

doc_data_list=[doc_data1,doc_data2,doc_data3,doc_data4,doc_data5]
my_cursor.executemany('INSERT OR IGNORE INTO documents VALUES (?,?,?,?,?)',doc_data_list)
my_cursor.execute('SELECT * FROM documents')
doc_data_result=my_cursor.fetchall()
doc_data_df=pd.DataFrame(doc_data_result)
print(doc_data_df)