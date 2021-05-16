from django import forms
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Post, User, Boarding

class NewPost(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField(max_length=10000)
    users_to_fly = forms.IntegerField(min_value=1, max_value=100)

    def create_post(self):
        post = Post(
            title=self.cleaned_data['title'],
            pub_date=timezone.now(),
            description=self.cleaned_data['description'],
            users_to_fly=self.cleaned_data['users_to_fly']
        )

        post.save()

        return post.id

class NewBoarding(forms.Form):

    def create_boarding(self, user, post):
        b = Boarding(
            user=user,
            post=post
        )
        b.save()

class NewUserForm(UserCreationForm):
    email = forms.EmailField()

    gender = forms.ChoiceField(choices =
        (
            (1, "female"),
            (2, "male"),
            (3, "others"),
            (4, "prefer not to say")
        )
    )
    #studies # TODO

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user