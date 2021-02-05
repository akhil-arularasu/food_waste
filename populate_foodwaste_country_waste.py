import os
os.environ["DJANGO_SETTINGS_MODULE"] = "mysite.settings"

import django
django.setup()

import pandas as pd
df = pd.read_csv('C:/Users/Arul/Documents/country_level_data_0.csv')
df = df[df['country'].notna()]

df['gdp'].fillna(0, inplace=True)
df['population'].fillna(0, inplace=True)
df['total_waste'].fillna(0, inplace=True)
df['organic_pct'].fillna(0, inplace=True)
print(df.isnull().sum())
print(df.convert_dtypes())

print(df.dtypes)
df = df.astype({'country': 'string'})
df = df.astype({'income_id': 'string'})
df = df.astype({'gdp': 'int64'})
df = df.astype({'population': 'int64'})
df = df.astype({'total_waste': 'int64'})
print(df.dtypes)

from foodwaste.models import CountryLevelWaste

def populate():

    for index, row in df.iterrows():
        print(row['country'], row['gdp'])
        name = row['country']
        gdp = row['gdp']
        total_waste = row['total_waste']
        organic_pct = row['organic_pct']
        population = row['population']
        ctywaste = CountryLevelWaste.objects.get_or_create(name=name,gdp=gdp,total_waste=total_waste,organic_pct=organic_pct,population=population)[0]


if __name__ == '__main__':
    populate()
    print("populating complete")
