import pandas as pd

# Загрузка данных
data = pd.read_csv('recipes.csv')

# Функция для поиска рецептов
def find_recipes(ingredients):
    ingredients_set = set(ingredients.split(', '))
    possible_recipes = []
    
    for index, row in data.iterrows():
        recipe_ingredients = set(row['ingredients'].split(', '))
        # Если все введенные ингредиенты содержатся в рецепте, добавляем его в список
        if ingredients_set.issuperset(recipe_ingredients):
            possible_recipes.append(row['recipe'])
            
    return possible_recipes

# Интерактивный ввод пользователя
print("Введите ингредиенты, разделяя их запятой (например, 'томаты, огурцы, сыр'): ")
user_ingredients = input()

# Поиск и вывод рецептов
possible_recipes = find_recipes(user_ingredients)
if possible_recipes:
    print("Из этих ингредиентов можно приготовить следующие блюда:")
    for recipe in possible_recipes:
        print(f"- {recipe}")
else:
    print("Из данных ингредиентов нельзя приготовить ни одного из известных рецептов.")
