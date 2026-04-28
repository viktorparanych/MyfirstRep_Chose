from faker import Faker

fake = Faker("uk_UA")

def get_fake_user():
    return {
        "name": fake.name(),
        "phone_number": fake.phone_number(),
        "email":fake.email(),
        "password": fake.password()
    }

print (get_fake_user()) 





#from mock import get_mocked_user
#import json
#import mock
#filename = input("Enter filename >>> ")
amount = int(input("How many fake want >>> "))


with open(filename, "w") as file:
    mocked_users = list()
    for i  in range(amount):
        mocked_users.append(mock.get_mocked_user())

    json.dump(mocked_users, file)    