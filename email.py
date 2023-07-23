class Email:
    has_been_read = False

    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content

    def mark_as_read(self):
        self.has_been_read = True


Inbox = []


def populate_inbox():
    # Create sample email objects and add them to the Inbox list
    email1 = Email("sender1@example.com", "Welcome to HyperionDev!", "Thank you for joining us!")
    email2 = Email("sender2@example.com", "Great work on the bootcamp!", "We are impressed with your progress.")
    email3 = Email("sender3@example.com", "Your excellent marks!", "Congratulations on your outstanding performance!")
    Inbox.extend([email1, email2, email3])


def list_emails():
    print("Inbox:")
    # Loop through the Inbox list and print the subject line of each email along with its index
    for i, email in enumerate(Inbox):
        print(f"{i} {email.subject_line}")


def read_email(index):
    if index < len(Inbox):
        # Retrieve the email object at the specified index from the Inbox list
        email = Inbox[index]
        print(f"\nFrom: {email.email_address}")
        print(f"Subject: {email.subject_line}")
        print(f"Content: {email.email_content}")
        email.mark_as_read()
        print(f"Email from {email.email_address} marked as read.\n")
    else:
        print("Invalid email index.")


# Populating the initial Inbox
populate_inbox()

# Main program loop
while True:
    print("\nMenu:")
    print("1. Read an email")
    print("2. View unread emails")
    print("3. Quit application")

    choice = input("Enter your choice: ")

    if choice == "1":
        # Option to read an email
        list_emails()
        index = int(input("Enter the index of the email you want to read: "))
        read_email(index)
    elif choice == "2":
        # Option to view unread emails
        unread_emails = [email.subject_line for email in Inbox if not email.has_been_read]
        print("Unread emails:")
        for email in unread_emails:
            print(email)
    elif choice == "3":
        # Option to quit the application
        print("Quitting application...")
        break
    else:
        print("Invalid choice. Please try again.")
