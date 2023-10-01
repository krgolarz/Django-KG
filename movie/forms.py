from django import forms


class MovieForm(forms.Form):
    tmdb_id = forms.CharField(max_length=15, required=False, label='TMDB ID')
    title = forms.CharField(max_length=255, label='Tytul')
    cast = forms.CharField(max_length=255, label='Obsada')
    homepage = forms.URLField(label='Strona WWW')
    director = forms.CharField(max_length=255, label='Rezyser')
    keywords = forms.CharField(max_length=255, label='Slowa kluczowe')
    overview = forms.CharField(max_length=1000, widget=forms.Textarea(attrs={'rows': 3}), label='Opis')
    runtime_minutes = forms.IntegerField(label='Czas trwania (minuty)')
    genres = forms.CharField(max_length=255, label='Gatunki ,rozdzielone |')
    production_companies = forms.CharField(max_length=255, label='Producenci, rodzielone |')
    release_date = forms.DateField(label='Data Produkcji', widget=forms.DateInput(attrs={"type": "date"}))
