import phonenumbers
from phonenumbers import carrier

mobileno = input("Enter Mobile Number With Country Code : ")
service_provider = phonenumbers.parse(mobileno)

print(carrier.name_for_number(service_provider,"en"))