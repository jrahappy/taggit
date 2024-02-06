from django import forms
from .models import Page

class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ["title", "content", "tags"]
        labels = {
            "title": "Title",
            "content": "Content",
            "tags": "Tags",
        }
        help_texts = {
            "title": "Enter the title of the page",
            "content": "Enter the content of the page",
            "tags": "Enter tags for the page",
        }
        error_messages = {
            "title": {
                "max_length": "This title is too long.",
            },
        }
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "content": forms.Textarea(attrs={"class": "form-control"}),
            "tags": forms.TextInput(attrs={"class": "form-control"}),
        }