import pandas as pd
from faker import Faker
import random
from tqdm import tqdm
import os

fake = Faker()

os.makedirs("data", exist_ok=True)

regions_and_cities = {
    "Bamako": ["Bamako", "Commune I", "Commune II", "Commune III", "Commune IV", "Commune V", "Commune VI"],
    "Kayes": ["Kayes", "Bafoulabe", "Kita", "Nioro du Sahel", "Yelimane"],
    "Koulikoro": ["Koulikoro", "Kati", "Dioila", "Banamba", "Kangaba"],
    "Sikasso": ["Sikasso", "Bougouni", "Koutiala", "Yanfolila", "Kolondieba"],
    "Segou": ["Segou", "Markala", "Niono", "San", "Bla"],
    "Mopti": ["Mopti", "Djenne", "Bandiagara", "Douentza", "Youwarou"],
    "Tombouctou": ["Tombouctou", "Goundam", "Dire", "Niafunke"],
    "Gao": ["Gao", "Ansongo", "Bourem", "Menaka"],
    "Kidal": ["Kidal", "Abeibara", "Tessalit", "Tin-Essako"]
}

first_names_male = [
    "Amadou", "Moussa", "Ibrahim", "Oumar", "Mamadou", "Seydou",
    "Bakary", "Modibo", "Abdoulaye", "Cheick", "Youssouf", "Boubacar"
]

first_names_female = [
    "Aminata", "Fatoumata", "Aissata", "Mariam", "Kadidia", "Fanta",
    "Oumou", "Hawa", "Adama", "Rokia", "Awa", "Kadiatou"
]

last_names = [
    "Sidibe", "Traore", "Coulibaly", "Keita", "Diarra", "Toure",
    "Cisse", "Sangare", "Kone", "Maiga", "Diallo", "Dembele"
]

records = []

TOTAL_RECORDS = 100000

for i in tqdm(range(TOTAL_RECORDS - 1)):
    gender = random.choice(["Male", "Female"])

    if gender == "Male":
        first_name = random.choice(first_names_male)
    else:
        first_name = random.choice(first_names_female)

    last_name = random.choice(last_names)

    region = random.choice(list(regions_and_cities.keys()))
    place_of_birth = random.choice(regions_and_cities[region])

    records.append({
        "national_id": f"MLI{i+1:08d}",
        "first_name": first_name,
        "last_name": last_name,
        "date_of_birth": fake.date_of_birth(minimum_age=0, maximum_age=90),
        "gender": gender,
        "place_of_birth": place_of_birth,
        "region": region,
        "phone_number": f"+223 {random.randint(60, 99)} {random.randint(10, 99)} {random.randint(10, 99)} {random.randint(10, 99)}",
        "email": fake.email(),
        "registration_date": fake.date_this_decade()
    })

records.append({
    "national_id": "MLI10000000",
    "first_name": "Amadou",
    "last_name": "Sidibe",
    "date_of_birth": "1988-06-17",
    "gender": "Male",
    "place_of_birth": "Markala",
    "region": "Segou",
    "phone_number": "TEST-0001",
    "email": "amadou.sidibe@test.mdip",
    "registration_date": "2026-06-17"
})

df = pd.DataFrame(records)

df.to_csv("data/citizens_100k.csv", index=False)

print("Done. 100,000 citizens created.")
print("File saved here: data/citizens_100k.csv")