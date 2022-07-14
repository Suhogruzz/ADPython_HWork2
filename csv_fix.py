import re
import csv


def form_new_contacts(find, fix):
    new_contacts = []
    with open("phonebook_raw.csv",  encoding='utf-8') as f:
        rows = csv.reader(f, delimiter=',')
        contacts_list = list(rows)
    for contact in contacts_list:
        new_contact = []
        fullname = ','.join(contact[:3])
        foundnames = re.findall(r'(\w+)', fullname)
        while len(foundnames) != 3:
            foundnames.append(' ')
        new_contact += foundnames
        new_contact.extend([contact[3], contact[4]])
        phone_compile = re.compile(find)
        phone_change = phone_compile.sub(fix, contact[5])
        new_contact.extend([phone_change, contact[6]])
        new_contacts.append(new_contact)
    return new_contacts


def delete_dupes_and_rewrite(new_contacts):
    new_contacts_dict = {}
    for contact in new_contacts:
        if contact[0] in new_contacts_dict:
            dict_value = new_contacts_dict[contact[0]]
            for i in range(len(dict_value)):
                if contact[i]:
                    dict_value[i] = contact[i]
        else:
            new_contacts_dict[contact[0]] = contact
    with open('phonebook.csv','w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(list(new_contacts_dict.values()))


if __name__ == '__main__':
    phone_find = '(8|\+7)?\s*(\(*)(\d{3})(\)*)(\s*|-)(\d{3})(\s*|-)(\d{2})(\s*|-)(\d{2})\s*(\(*)(\w\w\w\.)*\s*(\d{4})*(\))*'
    phone_fix = r'+7(\3)\6-\8-10 \12\13'
    delete_dupes_and_rewrite(form_new_contacts(phone_find, phone_fix))



