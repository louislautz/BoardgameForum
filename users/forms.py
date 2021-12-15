from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField

User = get_user_model()

class RegisterForm(forms.ModelForm):
    """"""
    username = forms.CharField()
    biography = forms.CharField(widget=forms.Textarea(attrs={'cols': 50}))
    password = forms.CharField(widget=forms.PasswordInput)
    password_2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username']

    def clean_username(self):
        """Checks whether username is already taken"""
        username = self.cleaned_data.get('username')
        database_selector = User.objects.filter(username=username)
        if database_selector.exists():
            raise forms.ValidationError("Username is already taken")
        return username

    def clean(self):
        """Checks if both passwords match"""
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_2 = cleaned_data.get("password_2")
        if password is not None and password != password_2:
            self.add_error("password_2", "Your passwords must match")
        return cleaned_data
    
class UserAdminCreationForm(forms.ModelForm):
    """A form for creating new users in the admin section"""
    password = forms.CharField(widget=forms.PasswordInput)
    password_2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username']

    def clean(self):
        """Checks if both passwords match"""
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_2 = cleaned_data.get("password_2")
        if password is not None and password != password_2:
            self.add_error("password_2", "Your passwords must match")
        return cleaned_data

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"]) #set_password function saves the passwords as hashes to the database
        if commit:
            user.save()
        return user

class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users."""
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ['username', 'password', 'is_admin', 'is_staff']

    def clean_password(self):
        # Returns the value the user typed
        return self.initial["password"]