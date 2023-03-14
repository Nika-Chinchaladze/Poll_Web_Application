from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import Personal, UserImage


class RegisterModelForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=150, widget=forms.TextInput(attrs={"class": "form-control"}))
    last_name = forms.CharField(
        max_length=150, widget=forms.TextInput(attrs={"class": "form-control"}))
    email = forms.EmailField(max_length=150, widget=forms.EmailInput(
        attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name",
                  "email", "password1", "password2",)

    def __init__(self, *args, **kwargs):
        super(RegisterModelForm, self).__init__(*args, **kwargs)

        self.fields["username"].widget.attrs["class"] = "form-control"
        self.fields["password1"].widget.attrs["class"] = "form-control"
        self.fields["password2"].widget.attrs["class"] = "form-control"


class LoginModelForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ("username", "password",)

    def __init__(self, *args, **kwargs):
        super(LoginModelForm, self).__init__(*args, **kwargs)

        self.fields["username"].widget.attrs["class"] = "form-control"
        self.fields["password"].widget.attrs["class"] = "form-control"


class PersonalInfoForm(forms.ModelForm):
    class Meta:
        model = Personal
        fields = "__all__"
        labels = {
            "work": "",
            "university": "",
            "city": "",
            "country": "",
            "love": "",
            "phone": "",
            "user": ""
        }
        error_messages = {
            "work": {
                "required": "All field must be filled",
                "max_length": "Please try shorter string"
            },
            "university": {
                "required": "All field must be filled",
                "max_length": "Please try shorter string"
            },
            "city": {
                "required": "All field must be filled",
                "max_length": "Please try shorter string"
            },
            "country": {
                "required": "All field must be filled",
                "max_length": "Please try shorter string"
            },
            "love": {
                "required": "All field must be filled",
                "max_length": "Please try shorter string"
            },
            "phone": {
                "required": "All field must be filled",
                "max_length": "Please try shorter string"
            },
            "user": {
                "required": "All field must be filled",
                "max_length": "Please try shorter string"
            }
        }

    def __init__(self, *args, **kwargs):
        super(PersonalInfoForm, self).__init__(*args, **kwargs)

        self.fields["work"].widget.attrs["class"] = "form-control personalForm"
        self.fields["university"].widget.attrs["class"] = "form-control personalForm"
        self.fields["city"].widget.attrs["class"] = "form-control personalForm"
        self.fields["country"].widget.attrs["class"] = "form-control personalForm"
        self.fields["love"].widget.attrs["class"] = "form-control personalForm"
        self.fields["phone"].widget.attrs["class"] = "form-control personalForm"
        self.fields["user"].widget.attrs["class"] = "form-control personalForm"

        self.fields["work"].widget.attrs["placeholder"] = "Work place"
        self.fields["university"].widget.attrs["placeholder"] = "University"
        self.fields["city"].widget.attrs["placeholder"] = "City"
        self.fields["country"].widget.attrs["placeholder"] = "Country"
        self.fields["love"].widget.attrs["placeholder"] = "Relationship status"
        self.fields["phone"].widget.attrs["placeholder"] = "Phone Number"


class UserImageForm(forms.ModelForm):
    class Meta:
        model = UserImage
        fields = "__all__"
        labels = {
            "image": "",
            "user": ""
        }

    def __init__(self, *args, **kwargs):
        super(UserImageForm, self).__init__(*args, **kwargs)

        self.fields["image"].widget.attrs["class"] = "form-control imageForm"
        self.fields["user"].widget.attrs["class"] = "form-control imageForm"


class EditInformationForm(forms.Form):
    item = forms.CharField(label="", max_length=500, widget=forms.TextInput(
        attrs={"placeholder": "Enter New Value!"}))


MY_CHOICES = (
    ("pie", "Pie"),
    ("bar", "Bar"),
    ("line", "Line"),
)


class ChartForm(forms.Form):
    charts = forms.ChoiceField(label="", choices=MY_CHOICES)
