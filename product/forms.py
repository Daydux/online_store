from django import forms


class ProductCreateForm(forms.Form):
    image = forms.FileField(required=False)
    name = forms.CharField(max_length=255)
    description = forms.CharField(widget=forms.Textarea())
    price = forms.IntegerField(required=False)


class ReviewCreateForm(forms.Form):
    text = forms.CharField(max_length=255, min_length=6)