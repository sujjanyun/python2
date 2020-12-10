phonebook = {
    'Alice': '703-493-1834',
    'Bob': '857-384-1234',
    'Elizabeth': '484-584-2923'
}

print(phonebook['Elizabeth'])

phonebook['Kareem'] = '038-489-1234'

if 'Alice' in phonebook:
    del phonebook['Alice']

phonebook['Bob'] = '968-345-2345'

print(phonebook)