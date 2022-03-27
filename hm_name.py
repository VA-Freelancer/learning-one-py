
"""
3. Дан список имен. Выберите в новый список только те имена, которые состоят из 4-х букв.
names = ["Ryan", "Kieran", "Mark", "John", "David", "Paul"] # ["Ryan", "Mark", "John", "Paul"]
"""

names = ["Ryan", "Kieran", "Mark", "John", "David", "Paul"] # ["Ryan", "Mark", "John", "Paul"]
def get_names(names):
    return [i for i in names if len(i) == 4]

print(get_names(names))