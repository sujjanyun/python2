ramit = {
    'name': 'Ramit',
    'email': 'ramit@gmial.com',
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

def count_friends(olddir):
    olddir["friends_count"] = len(olddir['friends'])
    print(olddir)

count_friends(ramit)