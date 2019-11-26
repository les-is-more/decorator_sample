import smtplib, ssl

# SMTP/E-mail Server Address and Port
smtp_server_address = 'smtp.gmail.com'
smtp_server_port_TLS = 587

# SMTP Account Login and Password
user_id = 'gamma.alpha.upsilon.90@gmail.com'
user_pwd = 'priest.1'

# Message Body 
message_FROM_address = 'gamma.alpha.upsilon.90@gmail.com'
message_TO_address = ['jez1209@gmail.com']
message_CC_address = ['lester.cajegas@gmail.com']
message_subject = 'Test mail (Lester to lol)'
message_body = "Hi, \n This is a test e-mail, using Python script. \n\nYours Trulili, \nLester"

message = "From: {} \r\n".format(message_FROM_address) + \
    "To: {} \r\n".format(",".join(message_TO_address)) + \
    "CC: {} \r\n".format(",".join(message_CC_address)) + \
    "Subject : {} \r\n".format(message_subject) + message_body

# Main Function
with smtplib.SMTP(smtp_server_address,smtp_server_port_TLS) as server:
    server.starttls(context = ssl.create_default_context())
    server.login(user_id, user_pwd)
    server.sendmail(message_FROM_address, message_TO_address, message)

