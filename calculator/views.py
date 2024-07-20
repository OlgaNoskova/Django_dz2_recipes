from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def ingredient_calculation(recipe, servings):
    if recipe in DATA.keys():
        ingredients = DATA.get(recipe)
        return {ingredient: format(amount * int(servings), '.2f') for ingredient, amount in ingredients.items()}
    return None


def recipe_view(request, recipe_name):
    servings = request.GET.get('servings', 1)

    res_ingredients = ingredient_calculation(recipe_name, servings)
    context = {
        'recipe_name': recipe_name,
        'recipe': res_ingredients,
        }
    return render(request, 'calculator/index.html', context)

