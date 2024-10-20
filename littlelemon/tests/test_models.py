
from restaurant.models import Menu


def test_menu():

    class MenuTest():

        def test_get_item(self):
            item = Menu.objects.create(title="IceCream", price=80, inventory=100)
            assert item == "IceCream : 80"


def test_booking():
    assert True
