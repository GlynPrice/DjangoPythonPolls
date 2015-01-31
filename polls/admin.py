# Register your models here.

from django.contrib import admin
from polls.models import Question, Choice

# Register your models here.

class ChoiceInline(admin.TabularInline):   #TabularInline or StackedInline
    model = Choice
    extra = 3

#Change the order of the fields
#class QuestionAdmin(admin.ModelAdmin):
#    fields = ['pub_date', 'question_text']

#Split the form up into fieldsets and order the fields
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]    #choices  - forms for each question

    #fields for questions in columns, rather than in rows (and table-based)
    list_display = ('id', 'question_text', 'pub_date', 'was_published_recently', 'choicesPub')
    list_filter = ['question_text','pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)


