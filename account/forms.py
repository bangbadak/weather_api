from django import forms

class ID(forms.Form):
    title = forms.IntegerField()
    email = forms.CharField(max_length=30)
    password = forms.CharField(max_length=16)

    def __str__(self):
        return f'ID_{self.pk}'
