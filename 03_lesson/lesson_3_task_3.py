from address import Address
from mailing import Mailing

to_address = Address("123456", "Алматы", "Абая", "10", "5")
from_address = Address("654321", "Астана", "Байтурсынова", "20", "15")

mailing = Mailing(
    to_address=to_address,
    from_address=from_address,
    cost=500,
    track="RT123456789KZ"
)

print(
    f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, "
    f"{mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment} "
    f"в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, "
    f"{mailing.to_address.house} - {mailing.to_address.apartment}. Стоимость {mailing.cost} рублей."
)
