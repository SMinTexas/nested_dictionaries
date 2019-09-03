# ramit = { 
#  'name': 'Ramit', 
#  'email': 'ramit@gmail.com', 
#  'interests': ['movies', 'tennis'], 
#  'friends': [ 
#     { 
#       'name': 'Jasmine', 
#       'email': 'jasmine@yahoo.com', 
#       'interests': ['photography', 'tennis']
#     }, 
#     { 
#        'name': 'Jan', 
#        'email': 'jan@hotmail.com', 
#        'interests': ['movies', 'tv'] 
#     } 
#   ] 
#}
#
# 1. Write a python expression that gets the email address of Ramit.
# 2. Write a python expression that gets the first of Ramit's interests.
# 3. Write a python expression that gets the email address of Jasmine.
# 4. Write a python expression that gets the second of Jan's two interests.

ramit = { 
  'name': 'Ramit', 
  'email': 'ramit@gmail.com', 
  'interests': ['movies', 'tennis'], 
  'friends': [ 
     { 
       'name': 'Jasmine', 
       'email': 'jasmine@yahoo.com', 
       'interests': ['photography', 'tennis']
     }, 
     { 
        'name': 'Jan', 
        'email': 'jan@hotmail.com', 
        'interests': ['movies', 'tv'] 
     } 
    ] 
}

# Get ramit's email address
email = ramit.get("email")
print(f"Ramit\'s E-Mail Address: {email}")

# Get ramit's first interest
interests = ramit.get("interests")
first_interest = interests[0]
print(f"Ramit\'s First Interest: {first_interest}")

# Get jasmine's email address
friends = ramit.get("friends")
for friend in friends:
    if friend["name"] == "Jasmine":
        friend_email = friend["email"]
        print(f"Ramit\'s First Friend\'s E-Mail Address: {friend_email}")

        # Get jasmine's second interest
        friend_interests = friend["interests"]
        friend_second_interest = friend_interests[1]
        print(f"Ramit\'s First Friend\'s Second Interest: {friend_second_interest}")