#! python3
PASSWORDS = {'email':'KSHITij#*#99',
             'blog':'Shivam#*#99',
             'test':'12345'}
import sys, pyperclip
if len(sys.argv)<2:
    print('Usage: py pw.py [account] - copy account password')
    sys.exit()
account = sys.argv[1]
if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for '+account+' is copied to clipboard.')
else:
    print('There is no account named '+account)
    
