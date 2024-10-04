import subprocess

def send_imessage(recipient, message):
    apple_script = f'''
    tell application "Messages"
        set targetService to 1st service whose service type = iMessage
        set targetBuddy to buddy "{recipient}" of targetService
        send "{message}" to targetBuddy
    end tell
    '''
    subprocess.run(['osascript', '-e', apple_script])

# Example usage
# recipient = "+14708478039"  # Replace with the recipient's phone number or email
# message = "I Love uuuu"
# send_imessage(recipient, message)