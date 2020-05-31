''' 
The email slicer is a handy program to get the username 
and domain name from an email address. You can customize and 
send a message to the user with this information.
'''
email = input("Enter your email address : ").strip()
user_name = email[:email.index('@')]
domain_name = email[email.index('@')+1:]
result = print('Your username is "{}" and your domain name is {}'.format(user_name,domain_name))
print(result)