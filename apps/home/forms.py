from django import forms

from apps.scraper.royalroad import RoyalRoadError, canonical_fiction


class NovelImportForm(forms.Form):
    fiction_url = forms.URLField(
        label="Royal Road fiction URL",
        assume_scheme="https",
        max_length=500,
        widget=forms.URLInput(attrs={"placeholder": "https://www.royalroad.com/fiction/…"}),
    )

    def clean_fiction_url(self):
        url = self.cleaned_data["fiction_url"]
        try:
            _, canonical_url = canonical_fiction(url)
        except RoyalRoadError as exc:
            raise forms.ValidationError("Enter a Royal Road fiction URL.") from exc
        return canonical_url
