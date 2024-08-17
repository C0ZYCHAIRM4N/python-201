# Add the necessary import statement in order to make this script
# produce output. Don't change any of the existing code.
# All the necessary variables and functions are
# already defined in the `codingnomads/` folder.
from codingnomads.recipes.soup import make_soup
from codingnomads import ingredients

print(ingredients.carrot)

soup = make_soup(ingredients.carrot)
print(soup)
