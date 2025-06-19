class City:
    def __init__(self, name, country, population, landmarks, nickname, founded, mayor):
        self.name = name
        self.country = country
        self.population = population  # integer, rounded to the nearest 1,000
        self.landmarks = landmarks    # list of strings
        self.nickname = nickname
        self.founded = founded
        self.mayor = mayor

# Your hometown
monrovia = City(
    name="Monrovia",
    country="United States",
    population=37000,
    landmarks=["Old Town", "Monrovia Canyon Park", "Library Park"],
    nickname="Gem City of the Foothills",
    founded=1887,
    mayor="Becky A. Shevlin"
)

# A city you’ve always wanted to visit
tokyo = City(
    name="Tokyo",
    country="Japan",
    population=13960000,
    landmarks=["Tokyo Tower", "Shibuya Crossing", "Senso-ji Temple"],
    nickname="The Eastern Capital",
    founded=1603,
    mayor="Yuriko Koike"
)

# Print out both objects
print(vars(monrovia))
print(vars(tokyo))
