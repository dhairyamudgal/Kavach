
# Importing libraries
import imaplib
import email
import os
import yaml  # To load saved login credentials from a yaml file


def check(a):
    # folder containing text files
    folder_path = "malicious_pure"
    input_string = a
    input_string = input_string.replace('3D', '')
    input_string = input_string.replace(',=', ',')

    print(input_string)

    # iterate over all files in folder
    for filename in os.listdir(folder_path):
        # read file contents
        with open(os.path.join(folder_path, filename), "r") as f:
            file_contents = f.read()
            # check if input string is present in file contents
            if input_string in file_contents:
                print(f"Match found in file: {filename}")



with open("credentials.yml") as f:
    content = f.read()

# from credentials.yml import user name and password
my_credentials = yaml.load(content, Loader=yaml.FullLoader)

# Load the user name and passwd from yaml file
user, password = my_credentials["user"], my_credentials["password"]

# URL for IMAP connection
imap_url = 'imap.gmail.com'

# Connection with GMAIL using SSL
my_mail = imaplib.IMAP4_SSL(imap_url)

# Log in using your credentials
my_mail.login(user, password)

# Select the Inbox to fetch messages
my_mail.select('Inbox')
key = 'SINCE "29-Apr-2023"'


_, data = my_mail.search(None, key)  # Search for emails with specific key and value

mail_id_list = data[0].split()  # IDs of all emails that we want to fetch

msgs = []  # empty list to capture all messages
# Iterate through messages and extract data into the msgs list
for num in mail_id_list:
    typ, data = my_mail.fetch(num, '(RFC822)')  # RFC822 returns whole message (BODY fetches just body)
    msgs.append(data)



for msg in msgs[::-1]:
    for response_part in msg:

        if type(response_part) is tuple:
            my_msg = email.message_from_bytes((response_part[1]))
            print("_________________________________________")
            print("subj:", my_msg['subject'])
            print("from:", my_msg['from'])
            print("body:")
            for part in my_msg.walk():
                if part.get_content_type() == 'text/plain':
                    check(part.get_payload())












