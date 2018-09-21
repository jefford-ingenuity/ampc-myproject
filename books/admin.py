from django.contrib import admin

from books.models import Author, Book, Publisher


class AuthorAdmin(admin.ModelAdmin):
    fields = ['email', 'first_name', 'last_name']
    list_display = ['first_name', 'last_name', 'email']
    search_fields = ['first_name', 'last_name', 'email']

class BookAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Basic Information", {'fields': ['title', 'authors', 'publisher']}),
        ('Date information', {
            'fields': ['publication_date'],
            'classes': ['collapse'],
        }),
    ]
    list_display = ['title', 'publisher']
    list_filter = ['publication_date']
    search_fields = ['title']
    filter_vertical = ['authors']

class BookInline(admin.TabularInline):
    model = Book
    extra = 0

class PublisherAdmin(admin.ModelAdmin):
    inlines = [BookInline]



admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Publisher, PublisherAdmin)
