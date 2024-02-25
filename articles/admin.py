from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        main_tag = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main'):
                main_tag += 1
        if main_tag < 1:
            raise ValidationError('Укажите основной раздел!')
        if main_tag > 1:
            raise ValidationError('Основной может быть только один раздел!')
        return super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset
    extra = 2


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]