from pip._vendor.pyparsing import unicode_set

from vue_app.models import Post, User, Boarding
from django.utils import timezone

p = Post.objects.last()

print(p.is_ready_to_fly)