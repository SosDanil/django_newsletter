from django import forms

from text_messages.models import TextMessage


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class TextMessageForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = TextMessage
        fields = '__all__'
