from django import forms


class userBioForm(forms.Form):
    username = forms.CharField(
        label="", widget=forms.TextInput(attrs={"placeholder": "Username"})
    )

    class Meta:
        fields = ["username"]
