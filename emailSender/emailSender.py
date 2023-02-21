import yagmail

# Sending simple email
try:
    #initializing the server connection
    yag = yagmail.SMTP(user='honglin2023@gmail.com', oauth2_file="credentials.json")
    #sending the email
    yag.send(to='91xw04@ms.mingdao.edu.tw', subject='Testing Yagmail', contents='Hurray, it worked!')
    print("Email sent successfully")
except:
    print("Error, email was not sent")

# Sending with attachment
try:
    #initializing the server connection
    yag = yagmail.SMTP(user='honglin2023@gmail.com', oauth2_file="credentials.json")
    #sending the email
    yag.send(to='91xw04@ms.mingdao.edu.tw', subject='Sending Attachment', contents='Please find the image attached', attachments='goose.jpg')
    print("Email sent successfully")
except:
    print("Error, email was not sent")

# Send to multiple ppl
try:
    yag = yagmail.SMTP(user='honglin2023@gmail.com', oauth2_file="credentials.json")
    yag.send(to=['91xw04@ms.mingdao.edu.tw', 'wanghonglin2023@gmail.com'], subject='Greetings...', contents='How are you?')
    print("email sent successfully")
except:
    print("error sending email")

# Send HTML email
with open('index.html', 'r', encoding='utf-8') as f:
    contentHTML = f.read()
try:
    yag = yagmail.SMTP(user='honglin2023@gmail.com', oauth2_file="credentials.json")
    yag.send(to='91xw04@ms.mingdao.edu.tw', subject='Fancy Email!', contents=contentHTML)
    print("email sent successfully")
except:
    print("error sending email")
