

from modeltranslation.translator import translator, TranslationOptions
from core.models import *

class BlogTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)


class CategoryTranslationOptions(TranslationOptions):
    fields = ('title',)


class AboutTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


translator.register(Blog, BlogTranslationOptions)

translator.register(Category, CategoryTranslationOptions)

translator.register(About, AboutTranslationOptions)





# class testTranslationOptions(TranslationOptions):
#     fields = ('title',)

# translator.register(test, testTranslationOptions)


