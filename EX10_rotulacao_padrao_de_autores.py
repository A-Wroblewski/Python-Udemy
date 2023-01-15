def standard_label(*args):
    author_last_surname = author_full_name[-1]
    publish_date_last_two_digits = publish_date[-2] + publish_date[-1]

    bibliographic_reference_title_uppers_only = ''

    for letter in bibliographical_reference_title:
        if letter.isupper():
            bibliographic_reference_title_uppers_only += letter

    bibliographic_reference_title_first_three_capital_letters = bibliographic_reference_title_uppers_only[:3]

    return author_last_surname + publish_date_last_two_digits + bibliographic_reference_title_first_three_capital_letters

author_full_name = input('Author\'s full name: ').split()
publish_date = input('Date of publishment: ')
bibliographical_reference_title = input('Bibliographical reference title: ')

print(standard_label(author_full_name, publish_date, bibliographical_reference_title))
