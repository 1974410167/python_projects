
from pygments.styles import get_all_styles
from pygments.lexers import get_all_lexers

print(type(get_all_styles()))
print(get_all_styles())

for i in get_all_lexers():
    print(i)

# for i in get_all_styles():
#     print(i)