from faker import Faker


class Users:
    faker = Faker()

    firstname = faker.first_name()
    lastname = faker.last_name()
    email = faker.email()
    password = "StrongPass123!"
