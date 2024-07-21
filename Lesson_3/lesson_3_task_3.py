from address import Address
from mailing import Mailing

to_address = Address(123456, "Vilnius", "Gedimmino", 63, 45)
from_address = Address(456321, "Kaliningrad", "Sovetskaja", 75, 89)

mail = Mailing(to_address, from_address, 125, "QWERTY")
print(f"""Отправление {mail.track} из {mail.from_address.index}, {mail.from_address.city}, {mail.from_address.street}, {mail.from_address.house} - {mail.from_address.flat}
в {mail.to_address.index}, {mail.to_address.city}, {mail.to_address.street}, {mail.to_address.house} - {mail.to_address.flat}. Стоимость {mail.cost} рублей.""")