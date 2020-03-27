# Email-Secret-Santa
A python script that randomly assigns secret santas and sends out emails letting everyone know who they should get a present for!

## Setup

0. Choose a gmail account to send email from. Do NOT use your personal gmail account for security reasons.
1. Log in to the gmail account, go to https://myaccount.google.com/lesssecureapps and allow less secure apps.
2. Choose how you want to supply your gmail password to the script:
  - If using a dotenv file instead of getpass, create a file called .env in the same directory as the secret santa script with one line with the format:
`PASSWORD=your_password_for_the_gmail_you're_sending_from_here`
  - If using getpass, you don't need to do 2a because you'll type the password in dynamically when running the script
3. Run the python script from terminal: `python send_email.py`
