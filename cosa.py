users = [
    {
        'email': 'jona@gmail.com',
        'first_name': 'jojo',
        'last_name':'jeje',
        'password': '123456'
    },
    {
        'email': 'jona@gmail.com',
        'first_name': 'jojo',
        'last_name':'jeje',
        'password': '123456',
        'birthdate': date(1990, 12, 19)
    },
    {
        'email': 'jona@gmail.com',
        'first_name': 'jojo',
        'last_name':'jeje',
        'password': '123456',
        'birthdate': date(1990, 12, 19),
        'bio': 'Muchas cosas woooo',
        'is_admin': True
    },
]

from posts.models import User

for user in users:
    person = User(**user)
    obj.save()
    # person = User.objects.create(**user)
    print(obj.pk)