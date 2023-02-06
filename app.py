from peewee import *
from playhouse.shortcuts import model_to_dict, dict_to_model

db = PostgresqlDatabase('contact_list', user='vasilis', password='12345', host='localhost', port=5432)

db.connect()

class BaseModel(Model):
  class Meta:
    database = db

class Contacts(BaseModel):
  name = CharField()
  phone_number = CharField()
  email = CharField()


ace = Contacts(name = 'Ace', phone_number = '7657657655', email = 'ace@gmail.com')
ace.save()
vasilis = Contacts(name = 'Vasilis', phone_number = '1234567890', email = 'vasilis@gmail.com')
vasilis.save()
rob = Contacts(name = 'Rob', phone_number = '0987654321', email = 'rob@gmail.com')
rob.save()
jim = Contacts(name = 'Jim', phone_number = '1231231234', email = 'Jim@gmail.com')
jim.save()

# contact_name = contact.name

def contacts_list1():
  print('What would you like to do with your contacts?')
  banana = input('List(L), Add New(N): ')
  if banana == 'L':
    con = input('Name of contact you are looking for?: ')
    contact = Contacts.get(Contacts.name == con)
    print(contact.name, contact.phone_number, contact.email)
  elif banana == 'N':
    name = input('Contact Name?: ')
    number = input('Contact Number?: ')
    email = input('Contact Email?: ')
    contact_list = Contacts(name=name, phone_number=number, email=email)
    contact_list.save()
    print(f'Contact {name} is now in your address book! Congrats... Your first friend!')




contacts_list1()