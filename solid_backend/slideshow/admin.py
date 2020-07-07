from django.contrib import admin

from solid_backend.utility.forms import HasImgForm

from .models import Slideshow, SlideshowImage, SlideshowPage


class SlideshowPageInline(admin.TabularInline):
    model = SlideshowPage


class SlideshowImageInline(admin.TabularInline):
    model = SlideshowImage


class SlideshowAdmin(admin.ModelAdmin):
    form = HasImgForm
    list_display = ["id", "title", "img"]
    inlines = [SlideshowPageInline]


admin.site.register(Slideshow, SlideshowAdmin)


class SlideshowPageAdmin(admin.ModelAdmin):
    list_display = ["id", "show", "position", "title"]
    inlines = [SlideshowImageInline]


admin.site.register(SlideshowPage, SlideshowPageAdmin)


class SlideshowImageAdmin(admin.ModelAdmin):
    list_display = ["id", "page", "position", "title", "img"]


admin.site.register(SlideshowImage, SlideshowImageAdmin)
