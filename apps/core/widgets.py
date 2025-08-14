from django.forms.widgets import ClearableFileInput


class ImagePreviewWidget(ClearableFileInput):
    # template_name = "widgets/image_preview_widget.html"

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        if value and hasattr(value, "url"):
            context["widget"]["attrs"]["data-initial"] = value.url
        return context


class AdminAvatarWidget(ClearableFileInput):
    template_name = "widgets/admin_avatar_widget.html"
    
    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['widget'].update({
            'value': value,
        })
        return context