# forms.py
from django import forms
from .models import BlogPost
from django_ckeditor_5.widgets import CKEditor5Widget

class BlogForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields["text"].required = False
    class Meta:
        model = BlogPost
    
        fields = ['title', 'content']
        widgets = {
            'content': CKEditor5Widget(  # Correct the widget key to match the model field
                attrs={"class": "django_ckeditor_5"}, config_name="extends"
            ),
        }
    
    def __init__(self, *args, **kwargs):
        super(BlogForm, self).__init__(*args, **kwargs)
        self.fields['content'].required = False


class Update_BlogForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields["text"].required = False
    class Meta:
        model = BlogPost
    
        fields = ['title', 'content']
        widgets = {
            'content': CKEditor5Widget(  # Correct the widget key to match the model field
                attrs={"class": "django_ckeditor_5"}, config_name="extends"
            ),
        }
    
    def __init__(self, *args, **kwargs):
        super(BlogForm, self).__init__(*args, **kwargs)
        self.fields['content'].required = False