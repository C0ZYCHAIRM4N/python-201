# Add the necessary import statement in order to make this script
# produce output. Don't change any of the existing code.
# All the necessary variables and functions are
# already defined in the `codingnomads/` folder.


from codingnomads.recipes import soup as s
from codingnomads import ingredients as i


digestible = i.prepare(i.potato)
mix = i.carrot + i.potato + i.salt
soup = s.make_soup(mix)
print(soup)
