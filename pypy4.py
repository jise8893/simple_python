import imaplib
imap=imaplib.IMAP4_SSL('imap.gmail.com')
imap.login('silanon65@gmail.com','passwd')
imap.select('inbox')
result,data=imap.uid('search',None,'ALL')
print(result,data)

latest_email_uid=data[0].split()[-1]
result,data=imap.uid('fetch',latest_email_uid,'(RFC822)')
raw_email=data[0][1]
print(raw_email)
