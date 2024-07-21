from smartphone import Smartphone

catalog = []

catalog.append(Smartphone("Samsung", "Galaxy Note", "+7902235485"))
catalog.append(Smartphone("Samsung", "A40", "+7905685485"))
catalog.append(Smartphone("Samsung", "A60", "+7902235479"))
catalog.append(Smartphone("Samsung", "Galaxy S10+", "+7902235123"))
catalog.append(Smartphone("Samsung", "Galaxy Fold", "+7902238526"))


for phones in catalog:
  print(f"{phones.brand} - {phones.model}. {phones.number}")