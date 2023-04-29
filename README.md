# Kavach Round 1
 Aims to develop a system that can detect fileless malware in emails.
 
# Explaination of code in 'main.py':

This code uses the imaplib library in Python to establish a connection with a Gmail account via the Internet Message Access Protocol (IMAP). The yaml library is used to load login credentials (i.e., email address and password) from a YAML file. Once authenticated, the code selects the Inbox folder and searches for emails using a specific criterion (e.g., emails received since a particular date).

After finding emails that match the search criteria, the code extracts their details (e.g., subject, sender, and body) and prints them to the console. The email library is used to parse the message data received from the email server. Finally, the check function is called to check if the email body contains any malicious script by comparing it with a dataset of malicious scripts.

The code works by using the fetch() method to retrieve the data of each email from the server. Then, the message_from_bytes() method is used to convert the raw email data into an email.message.Message object, which can be used to extract email details such as the subject, sender, and body. The code uses the walk() method to iterate through the parts of the message and checks if there is any plain text content in the email body. If plain text content is found, the check() function is called to check if the email body contains any malicious script.


#Using Google API 
Basic implementation code in 'api.py'
We can also possibly use the Google API to extract emails from a Gmail account. The Gmail API provides programmatic access to a user's Gmail mailbox, and allows you to read, send, and delete messages, as well as manage labels and filters.

To use the Gmail API, you need to enable the API in the Google Cloud Console and obtain an API key or OAuth2 credentials. You can then use the Gmail API client library for Python to interact with the API and fetch emails.

Modules include os, pickle, and google-auth, which are needed to authenticate and authorize access to the Gmail API, and googleapiclient, which is the module that provides access to the Gmail API.
The program reads the user's credentials (stored in a token.pickle file) to authorize access to the user's Gmail account. If no credentials are found, the program prompts the user to log in and authorize access.
Once authorized, the program creates a gmail_service object, which is used to access the user's Gmail account through the API.
The program defines a function get_emails() that retrieves all the emails in the user's inbox using the messages().list() method of the gmail_service object. It then iterates over the list of messages returned and retrieves the full message for each one using the messages().get() method
