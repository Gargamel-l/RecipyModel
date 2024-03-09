import pandas as pd

# Список простых рецептов для обучения
data = [
    {"ingredients": "томаты, огурцы, оливковое масло, соль", "recipe": "Салат из томатов и огурцов"},
    {"ingredients": "куриная грудка, соевый соус, мед, чеснок", "recipe": "Маринованная курица"},
    {"ingredients": "макароны, соль, вода, сыр пармезан, черный перец", "recipe": "Макароны с сыром"},
    {"ingredients": "лосось, соль, лимон, оливковое масло", "recipe": "Запеченный лосось"},
    {"ingredients": "авокадо, лимонный сок, соль, перец", "recipe": "Гуакамоле"},
    {"ingredients": "яйца, соль, молоко, сливочное масло", "recipe": "Омлет"},
    {"ingredients": "бананы, молоко, мед, лед", "recipe": "Банановый смузи"},
    {"ingredients": "гречка, вода, соль", "recipe": "Вареная гречка"},
    {"ingredients": "шпинат, чеснок, оливковое масло, соль", "recipe": "Жареный шпинат"},
    {"ingredients": "курица, карри, кокосовое молоко, лук", "recipe": "Курица карри"},
    {"ingredients": "хлеб, майонез", "recipe": "бедный бутерброд"},
    {"ingredients": "хлеб, калбоса, сыр", "recipe": "обыкновенный бутерброд"}
]

# Создание DataFrame
recipes_df = pd.DataFrame(data)

# Сохранение в CSV-файл
recipes_df.to_csv('D:/programming/VisualStudion/workZone/RecipyModel/recipes.csv', index=False)

# Возвращаем путь к файлу
'D:/programming/VisualStudion/workZone/RecipyModel/recipes.csv'

