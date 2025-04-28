from faker import Faker
import pytest

fake = Faker('pl_PL')
fake.seed_instance(6669)

# print(fake.name())
# print(fake.address())
# print(fake.email())

@pytest.mark.parametrize(
    "name,email",
    [(fake.name(), fake.email()) for _ in range(5)],
    ids=lambda x: f"User-{str(x)[:30]}"
)
def test_registered_user(name,email):
    assert "@" in email
    assert isinstance(name, str)
