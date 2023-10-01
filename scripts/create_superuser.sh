#!/bin/sh

echo 'Creating superuser using create_superuser.sh'

# Attempt to create the superuser using environment variables
create_user_output=$(echo "from django.contrib.auth.models import User
try:
    User.objects.create_superuser('$ADMIN_USERNAME', '$ADMIN_EMAIL', '$ADMIN_PASSWORD')
    result = 'Superuser created successfully'
except Exception as e:
    result = f'Superuser could not be created: {e}'
print(result)
" | python manage.py shell 2>&1)

# Print the result of user creation
# echo "$create_user_output"
