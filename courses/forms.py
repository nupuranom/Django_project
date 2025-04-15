# from django import forms
# from .models import Course, Lesson, Student

# class CourseForm(forms.ModelForm):
#     class Meta:
#         model = Course
#         fields = ['title', 'description', 'duration', 'thumbnail']
#         widgets = {
#             'title': forms.TextInput(attrs={'class': 'form-control'}),
#             'description': forms.Textarea(attrs={'class': 'form-control'}),
#             'duration': forms.NumberInput(attrs={'class': 'form-control'}),
#         }

# class LessonForm(forms.ModelForm):
#     class Meta:
#         model = Lesson
#         fields = ['course', 'title', 'content']
#         widgets = {
#             'course': forms.Select(attrs={'class': 'form-control'}),
#             'title': forms.TextInput(attrs={'class': 'form-control'}),
#             'content': forms.Textarea(attrs={'class': 'form-control'}),
#         }

# class CourseEnrollmentForm(forms.Form):
#     student_name = forms.CharField(
#         label="Full Name",
#         max_length=100,
#         widget=forms.TextInput(attrs={'class': 'form-control'})
#     )
#     student_email = forms.EmailField(
#         label="Student Email", 
#         widget=forms.EmailInput(attrs={'class': 'form-control'})
#     )
#     course = forms.ModelChoiceField(
#         queryset=Course.objects.all(), 
#         label="Select Course", 
#         widget=forms.Select(attrs={'class': 'form-control'})
#     )
#------------lab 6--------
from django import forms
from django.contrib.auth.models import User
from .models import Course, Lesson, Student

# User Profile Update Form
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

# Course Form
class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'duration', 'thumbnail']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'duration': forms.NumberInput(attrs={'class': 'form-control'}),
        }

# Lesson Form
class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['course', 'title', 'content']
        widgets = {
            'course': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }

# Course Enrollment Form
class CourseEnrollmentForm(forms.Form):
    student_name = forms.CharField(
        label="Full Name",
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    student_email = forms.EmailField(
        label="Student Email", 
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    course = forms.ModelChoiceField(
        queryset=Course.objects.all(), 
        label="Select Course", 
        widget=forms.Select(attrs={'class': 'form-control'})
    )
