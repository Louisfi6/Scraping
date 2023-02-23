import pandas as pd


def remove_duplicates(filename, cols_to_check):
    data = pd.read_csv(filename)
    data.drop_duplicates(subset=cols_to_check, keep='first', inplace=True)
    data.to_csv(filename, index=False)

# Exemple d'utilisation :
cols_to_check = ['Name', 'Address', 'Email', 'Phone', 'Cases', 'Sworn Date']
remove_duplicates('Lawyers.csv', cols_to_check)
