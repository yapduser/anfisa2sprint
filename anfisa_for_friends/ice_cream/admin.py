from django.contrib import admin
from .models import Category, Topping, Wrapper, IceCream

admin.site.empty_value_display = 'Не задано'


class CustomAdmin(admin.ModelAdmin):
    """Родительский класс для админки."""

    list_display = ('title',)


class IceCreamInline(admin.TabularInline):
    """
    Интерфейс отображения дял связанных классов.

    Передаем его в CategoryAdmin, для вывода в разделе категории,
    при редактировании категорий.
    """

    model = IceCream
    extra = 0


class CategoryAdmin(CustomAdmin):
    """Интерфейс админки для модели Category."""

    inlines = (IceCreamInline,)


class ToppingAdmin(CustomAdmin):
    """Интерфейс админки для модели Topping."""
    ...


class WrapperAdmin(CustomAdmin):
    """Интерфейс админки для модели Wrapper."""
    ...


class IceCreamAdmin(CustomAdmin):
    """Интерфейс админки для модели IceCream."""

    list_display = (
        'title',
        'description',
        'price',
        'is_published',
        'is_on_main',
        'category',
        'wrapper',
        'output_order',
    )
    list_editable = (
        'is_published',
        'is_on_main',
        'category',
    )
    search_fields = ('title',)
    list_filter = ('is_published',)
    list_display_links = ('title',)
    filter_horizontal = ('toppings',)


admin.site.register(IceCream, IceCreamAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Topping, ToppingAdmin)
admin.site.register(Wrapper, WrapperAdmin)
