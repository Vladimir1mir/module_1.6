mu_dict = {'Vladimir': 1994, 'Dmitry': 2001, 'Denis': 1998}
print(mu_dict)
print(mu_dict['Vladimir'])
print(mu_dict.get('Viktor'), ': Not existing value')
mu_dict.update({'Nikita': 2000,
                'Emelyan': 1998})
print(mu_dict)
Modified_dictionary = mu_dict.pop('Vladimir')
print(Modified_dictionary)

mu_set = {1,2,3, (1,2,3), 'String', 2,5,4, 1.5}
print(mu_set)
mu_set.add((10,12))
print(mu_set)
mu_set.discard('String')
print(mu_set)
