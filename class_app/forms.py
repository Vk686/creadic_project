from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Student
from .models import Teacher


class AddStudentForm(ModelForm):
	class Meta:
		model = Student
		fields = '__all__'

class AddTeacherForm(ModelForm):
	class Meta:
		model = Teacher
		fields = '__all__'	

			
class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']