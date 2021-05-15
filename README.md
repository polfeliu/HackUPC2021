
# Models:
https://docs.djangoproject.com/en/3.2/intro/tutorial02/

##Migrate models to database
```shell script
python manage.py makemigrations vue_app
python manage.py sqlmigrate vue_app 0001
python manage.py migrate
```

##Shell
```shell script
python manage.py shell
```

```python
from vue_app.models import Idea
Idea.objects.all()
```

# URL patterns and views
https://docs.djangoproject.com/en/3.2/intro/tutorial03/