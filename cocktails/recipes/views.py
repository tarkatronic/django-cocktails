from django.core.urlresolvers import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView

from .models import Component, Drink, Ingredient


class DrinkDetailView(DetailView):
    model = Drink

    def get_context_data(self, **kwargs):
        context = super(DrinkDetailView, self).get_context_data(**kwargs)
        context.update({'components': Component.objects.filter(drink=self.get_object())})
        return context


class DrinkListView(ListView):
    model = Drink


class IngredientListView(ListView):
    model = Ingredient


class IngredientCreateView(CreateView):
    model = Ingredient
    fields = ['name', 'measurement']
    success_url = reverse_lazy('ingredient_list')
