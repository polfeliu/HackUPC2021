from pip._vendor.pyparsing import unicode_set

from vue_app.models import Post, User, Boarding
from django.utils import timezone

p = Post(
    title="example",
    pub_date=timezone.now(),
    description="description",
)

p.save()

u = User.objects.last()

b = Boarding(
    user=u,
    post=p
)

b.save()