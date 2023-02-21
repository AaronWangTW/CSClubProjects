import yagmail

# try:
#     yag = yagmail.SMTP(user="honglin2023@gmail.com",oauth2_file="credentials.json")
#     yag.send(to=["91xw04@ms.mingdao.edu.tw","honglinwang@gmail.com"],subject="testing yagmail",content="hi, this email have been sent to you using yagmail")
#     print("email sent successfully")
# except:
#     print("email failed to deliver")

with open('example.html', 'r', encoding='utf-8') as f:
    contentHTML = f.read()
try:
    yag = yagmail.SMTP(user='honglin2023@gmail.com', oauth2_file="credentials.json")
    yag.send(to='91xw04@ms.mingdao.edu.tw', subject='Fancy Email!', contents=contentHTML)
    print("email sent successfully")
except Exception as e:
    print("error sending email",e)