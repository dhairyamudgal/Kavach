from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Replace with your API credentials
creds = Credentials.from_authorized_user_file('credentials.json', ['https://www.googleapis.com/auth/gmail.readonly'])

# Create a Gmail API client
service = build('gmail', 'v1', credentials=creds)

# Fetch the list of messages in the inbox
messages = service.users().messages().list(userId='me', q='is:inbox').execute()

# Iterate through the messages and print the subject and sender of each message
for message in messages['messages']:
    msg = service.users().messages().get(userId='me', id=message['id']).execute()
    print(f"Subject: {msg['payload']['headers'][15]['value']}")
    print(f"From: {msg['payload']['headers'][16]['value']}")
