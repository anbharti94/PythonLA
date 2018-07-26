user = { 'admin': True, 'active': False, 'name': 'Kevin' }
if user['admin'] and user['active']:
    prefix = 'ACTIVE - ADMIN '
elif user['admin']:
    prefix = 'ADMIN '
elif user['active']:
    prefix = 'ACTIVE '
else:
    prefix = ''

print(prefix + user['name'])
