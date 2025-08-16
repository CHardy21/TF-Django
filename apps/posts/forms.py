# apps/posts/form.py
from django import forms
from .models import Post
from django_summernote.widgets import SummernoteWidget
from .widgets import SimpleSummernoteWidget
from apps.core.widgets import ImagePreviewWidget  # Widget con data-initial


class PostAdminForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
        widgets = {
            "resumen": SimpleSummernoteWidget(),
            "contenido": SummernoteWidget(),
        }


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["titulo", "resumen", "contenido", "categoria", "imagen"]
        widgets = {
            "resumen": SimpleSummernoteWidget(),
            "contenido": SummernoteWidget(),
            "imagen": ImagePreviewWidget(attrs={"class": "form-control"}),
        }
