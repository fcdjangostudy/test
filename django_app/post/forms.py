from django import forms


class PostForm(forms.Form):
    photo = forms.ImageField(
        label='image',
        widget=forms.FileInput(),
    )
    comment = forms.CharField(
        label='comment',
        widget=forms.TextInput(),
    )