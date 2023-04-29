# Kavach Round 1
# Basic Implementation with code and screenshots

# Aim:
The part of the project aims to develop a system that can detect fileless malware in emails. To accomplish this, we obtain a dataset of known malicious scripts from GitHub. We preprocess this dataset by converting the scripts into a structured format that can be easily compared to the email text.

When a new email arrives, the system extracts its details such as the subject, sender, and body of the email. It then compares the email text with the malicious script dataset to check for possible matches. If a match is found, the system alerts the user that the email may contain malware.
The system provides a simple yet effective method for detecting fileless malware in emails. It leverages a dataset of known malicious scripts to compare against incoming emails and alert the user when a match is found.

Aims to develop a system that can detect fileless malware in emails.


# Dataset used:
https://github.com/das-lab/mpsd
We used 'malicious_pure' samples from the above link

# Explaination of code in 'main.py':

This code uses the imaplib library in Python to establish a connection with a Gmail account via the Internet Message Access Protocol (IMAP). The yaml library is used to load login credentials (i.e., email address and password) from a YAML file. Once authenticated, the code selects the Inbox folder and searches for emails using a specific criterion (e.g., emails received since a particular date).

After finding emails that match the search criteria, the code extracts their details (e.g., subject, sender, and body) and prints them to the console. The email library is used to parse the message data received from the email server. Finally, the check function is called to check if the email body contains any malicious script by comparing it with a dataset of malicious scripts.

The code works by using the fetch() method to retrieve the data of each email from the server. Then, the message_from_bytes() method is used to convert the raw email data into an email.message.Message object, which can be used to extract email details such as the subject, sender, and body. The code uses the walk() method to iterate through the parts of the message and checks if there is any plain text content in the email body. If plain text content is found, the check() function is called to check if the email body contains any malicious script.


# Using Google API 
Basic implementation code in 'api.py'
We can also possibly use the Google API to extract emails from a Gmail account. The Gmail API provides programmatic access to a user's Gmail mailbox, and allows you to read, send, and delete messages, as well as manage labels and filters.

To use the Gmail API, you need to enable the API in the Google Cloud Console and obtain an API key or OAuth2 credentials. You can then use the Gmail API client library for Python to interact with the API and fetch emails.

Modules include os, pickle, and google-auth, which are needed to authenticate and authorize access to the Gmail API, and googleapiclient, which is the module that provides access to the Gmail API.
The program reads the user's credentials (stored in a token.pickle file) to authorize access to the user's Gmail account. If no credentials are found, the program prompts the user to log in and authorize access.
Once authorized, the program creates a gmail_service object, which is used to access the user's Gmail account through the API.
The program defines a function get_emails() that retrieves all the emails in the user's inbox using the messages().list() method of the gmail_service object. It then iterates over the list of messages returned and retrieves the full message for each one using the messages().get() method

# Implementation Screenshots:

1. Showing how the extracted mail is shown in console

<img width="984" alt="Screenshot 2023-04-29 at 9 42 19 PM" src="https://user-images.githubusercontent.com/88214026/235312507-ff26c19e-1115-4595-b350-9decdbe6d873.png">
Actual mail screenshot:<img width="1120" alt="Screenshot 2023-04-29 at 9 43 53 PM" src="https://user-images.githubusercontent.com/88214026/235312585-10947d21-bce4-49b1-8671-fd67aa0aefd6.png">

2. Now sending a malicious script via email

Console output:

<img width="1097" alt="Screenshot 2023-04-29 at 9 47 44 PM" src="https://user-images.githubusercontent.com/88214026/235312789-2fa4df21-0375-435e-9111-f5ad021de520.png">

Gmail Screenshot:
<img width="1098" alt="Screenshot 2023-04-29 at 9 48 41 PM" src="https://user-images.githubusercontent.com/88214026/235312833-302742f7-ce10-40dc-b0f5-6b2645f3a904.png">

3. Scanning this content for possible malicious scripts:

<img width="1071" alt="Screenshot 2023-04-29 at 9 52 04 PM" src="https://user-images.githubusercontent.com/88214026/235312969-1bbab061-b5b2-485e-8008-9549e29c6836.png">
In the output we can see that we detected that the content that was sent via email matches with the malicious scripts present in the dataset.

# This could be one of the possible ways of detecting file less malware sent via gmail and its basic implementation

