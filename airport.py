import numpy as np
import matplotlib.pyplot as plt
import csv 
import matplotlib.dates as mdates
import pandas as pd
import seaborn as sns
from datetime import datetime

def airport_emission(location):   

    # Lijst om de density-waarden op te slaan
    densities_2019 = []
    date_density_list_2019 = []
    dates_2019 = []


#2019 jaar
    # Lees het CSV-bestand
    with open(f'{location}_2019_1.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            
            # Zorg ervoor dat je geen lege rijen hebt
            if len(row) > 0:
                date_and_density_2019 = row[0].strip()  # Verwijder eventuele extra spaties aan het begin of einde van de string
                if '""' in date_and_density_2019:
                    pass
                else:
                    # Als '""' niet in de string staat, splits dan op basis van de enkele dubbele aanhalingstekens
                    parts_2019 = date_and_density_2019.split('"')
                    if len(parts_2019) > 1:  # Zorg ervoor dat er een waarde na de datum is
                        #print(f"Parts after alternative split: {parts}")
                        date_2019 = parts_2019[0]
                        density_2019 = parts_2019[1].strip()  # De waarde na de datum
                        try:
                            densities_2019.append(float(density_2019))  # Zet de density om naar een float
                        except ValueError:
                            print(f"Fout bij het converteren van density: {density_2019}")
                        date_density_list_2019.append(parts_2019)
                        
                    if len(parts_2019) < 1:
                        pass

    #print(date_density_list_2019)


    dates_2019 = [item[0] for item in date_density_list_2019]  # Haal de datum uit elk element
    densities_2019 = [float(item[1]) for item in date_density_list_2019 if item[1] != ""]  # Haal de density uit elk element en zet om naar float

    # Print de twee lijsten
    #print("Dates:", dates_2019)
    #print("densities_2019:", densities_2019)



    densities_2019_2  = []
    date_density_list_2019_2 = []
    dates_2019_2 = []
    with open(f'{location}_2019_2.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            
            # Zorg ervoor dat je geen lege rijen hebt
            if len(row) > 0:
                date_and_density_2019_2 = row[0].strip()  # Verwijder eventuele extra spaties aan het begin of einde van de string
                if '""' in date_and_density_2019_2:
                    pass
                else:
                    # Als '""' niet in de string staat, splits dan op basis van de enkele dubbele aanhalingstekens
                    parts_2019_2 = date_and_density_2019_2.split('"')
                    if len(parts_2019_2) > 1:  # Zorg ervoor dat er een waarde na de datum is
                        #print(f"Parts after alternative split: {parts}")
                        date_2019_2 = parts_2019_2[0]
                        density_2019_2 = parts_2019_2[1].strip()  # De waarde na de datum
                        try:
                            densities_2019_2.append(float(density_2019_2))  # Zet de density om naar een float
                        except ValueError:
                            print(f"Fout bij het converteren van density: {density_2019_2}")
                        date_density_list_2019_2.append(parts_2019_2)
                        
                    if len(parts_2019_2) < 1:
                        pass
    dates_2019_2 = [item[0] for item in date_density_list_2019_2]  # Haal de datum uit elk element
    densities_2019_2 = [float(item[1]) for item in date_density_list_2019_2 if item[1] != ""]  # Haal de density uit elk element en zet om naar float


    dates_2019.extend(dates_2019_2)
    densities_2019.extend(densities_2019_2)

    densities_calculated_2019 = []
    for x in densities_2019:
        x = x / 1000000000
        densities_calculated_2019.append(x)

    # Lijst om de density-waarden op te slaan
    densities_2020 = []
    date_density_list_2020 = []
    dates_2020 = []


#2020 jaar
    # Lees het CSV-bestand
    with open(f'{location}_2020_1.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            
            # Zorg ervoor dat je geen lege rijen hebt
            if len(row) > 0:
                date_and_density_2020 = row[0].strip()  # Verwijder eventuele extra spaties aan het begin of einde van de string
                if '""' in date_and_density_2020:
                    pass
                else:
                    # Als '""' niet in de string staat, splits dan op basis van de enkele dubbele aanhalingstekens
                    parts_2020 = date_and_density_2020.split('"')
                    if len(parts_2020) > 1:  # Zorg ervoor dat er een waarde na de datum is
                        #print(f"Parts after alternative split: {parts}")
                        date_2020 = parts_2020[0]
                        density_2020 = parts_2020[1].strip()  # De waarde na de datum
                        try:
                            densities_2020.append(float(density_2020))  # Zet de density om naar een float
                        except ValueError:
                            print(f"Fout bij het converteren van density: {density_2020}")
                        date_density_list_2020.append(parts_2020)
                        
                    if len(parts_2020) < 1:
                        pass

    #print(date_density_list_2020)


    dates_2020 = [item[0] for item in date_density_list_2020]  # Haal de datum uit elk element
    densities_2020 = [float(item[1]) for item in date_density_list_2020 if item[1] != ""]  # Haal de density uit elk element en zet om naar float

    # Print de twee lijsten
    #print("Dates:", dates_2020)
    #print("densities_2020:", densities_2020)



    densities_2020_2  = []
    date_density_list_2020_2 = []
    dates_2020_2 = []
    with open(f'{location}_2020_2.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            
            # Zorg ervoor dat je geen lege rijen hebt
            if len(row) > 0:
                date_and_density_2020_2 = row[0].strip()  # Verwijder eventuele extra spaties aan het begin of einde van de string
                if '""' in date_and_density_2020_2:
                    pass
                else:
                    # Als '""' niet in de string staat, splits dan op basis van de enkele dubbele aanhalingstekens
                    parts_2020_2 = date_and_density_2020_2.split('"')
                    if len(parts_2020_2) > 1:  # Zorg ervoor dat er een waarde na de datum is
                        #print(f"Parts after alternative split: {parts}")
                        date_2020_2 = parts_2020_2[0]
                        density_2020_2 = parts_2020_2[1].strip()  # De waarde na de datum
                        try:
                            densities_2020_2.append(float(density_2020_2))  # Zet de density om naar een float
                        except ValueError:
                            print(f"Fout bij het converteren van density: {density_2020_2}")
                        date_density_list_2020_2.append(parts_2020_2)
                        
                    if len(parts_2020_2) < 1:
                        pass
    dates_2020_2 = [item[0] for item in date_density_list_2020_2]  # Haal de datum uit elk element
    densities_2020_2 = [float(item[1]) for item in date_density_list_2020_2 if item[1] != ""]  # Haal de density uit elk element en zet om naar float


    dates_2020.extend(dates_2020_2)
    densities_2020.extend(densities_2020_2)

    densities_calculated_2020 = []
    for x in densities_2020:
        x = x / 1000000000
        densities_calculated_2020.append(x)
    

#2021 jaar
 # Lijst om de density-waarden op te slaan
    densities_2021 = []
    date_density_list_2021 = []
    dates_2021 = []
# Lees het CSV-bestand
    with open(f'{location}_2021_1.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            
            # Zorg ervoor dat je geen lege rijen hebt
            if len(row) > 0:
                date_and_density_2021 = row[0].strip()  # Verwijder eventuele extra spaties aan het begin of einde van de string
                if '""' in date_and_density_2021:
                    pass
                else:
                    # Als '""' niet in de string staat, splits dan op basis van de enkele dubbele aanhalingstekens
                    parts_2021 = date_and_density_2021.split('"')
                    if len(parts_2021) > 1:  # Zorg ervoor dat er een waarde na de datum is
                        #print(f"Parts after alternative split: {parts}")
                        date_2021 = parts_2021[0]
                        density_2021 = parts_2021[1].strip()  # De waarde na de datum
                        try:
                            densities_2021.append(float(density_2021))  # Zet de density om naar een float
                        except ValueError:
                            print(f"Fout bij het converteren van density: {density_2021}")
                        date_density_list_2021.append(parts_2021)
                        
                    if len(parts_2021) < 1:
                        pass

    #print(date_density_list_2021)


    dates_2021 = [item[0] for item in date_density_list_2021]  # Haal de datum uit elk element
    densities_2021 = [float(item[1]) for item in date_density_list_2021 if item[1] != ""]  # Haal de density uit elk element en zet om naar float

    # Print de twee lijsten
    #print("Dates:", dates_2021)
    #print("densities_2021:", densities_2021)



    densities_2021_2  = []
    date_density_list_2021_2 = []
    dates_2021_2 = []
    with open(f'{location}_2021_2.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            
            # Zorg ervoor dat je geen lege rijen hebt
            if len(row) > 0:
                date_and_density_2021_2 = row[0].strip()  # Verwijder eventuele extra spaties aan het begin of einde van de string
                if '""' in date_and_density_2021_2:
                    pass
                else:
                    # Als '""' niet in de string staat, splits dan op basis van de enkele dubbele aanhalingstekens
                    parts_2021_2 = date_and_density_2021_2.split('"')
                    if len(parts_2021_2) > 1:  # Zorg ervoor dat er een waarde na de datum is
                        #print(f"Parts after alternative split: {parts}")
                        date_2021_2 = parts_2021_2[0]
                        density_2021_2 = parts_2021_2[1].strip()  # De waarde na de datum
                        try:
                            densities_2021_2.append(float(density_2021_2))  # Zet de density om naar een float
                        except ValueError:
                            print(f"Fout bij het converteren van density: {density_2021_2}")
                        date_density_list_2021_2.append(parts_2021_2)
                        
                    if len(parts_2021_2) < 1:
                        pass
    dates_2021_2 = [item[0] for item in date_density_list_2021_2]  # Haal de datum uit elk element
    densities_2021_2 = [float(item[1]) for item in date_density_list_2021_2 if item[1] != ""]  # Haal de density uit elk element en zet om naar float


    dates_2021.extend(dates_2021_2)
    densities_2021.extend(densities_2021_2)

    densities_calculated_2021 = []
    for x in densities_2021:
        x = x / 1000000000
        densities_calculated_2021.append(x)


#2023 jaar
 # Lijst om de density-waarden op te slaan
    densities_2023 = []
    date_density_list_2023 = []
    dates_2023 = []
# Lees het CSV-bestand
    with open(f'{location}_2023_1.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            
            # Zorg ervoor dat je geen lege rijen hebt
            if len(row) > 0:
                date_and_density_2023 = row[0].strip()  # Verwijder eventuele extra spaties aan het begin of einde van de string
                if '""' in date_and_density_2023:
                    pass
                else:
                    # Als '""' niet in de string staat, splits dan op basis van de enkele dubbele aanhalingstekens
                    parts_2023 = date_and_density_2023.split('"')
                    if len(parts_2023) > 1:  # Zorg ervoor dat er een waarde na de datum is
                        #print(f"Parts after alternative split: {parts}")
                        date_2023 = parts_2023[0]
                        density_2023 = parts_2023[1].strip()  # De waarde na de datum
                        try:
                            densities_2023.append(float(density_2023))  # Zet de density om naar een float
                        except ValueError:
                            print(f"Fout bij het converteren van density: {density_2023}")
                        date_density_list_2023.append(parts_2023)
                        
                    if len(parts_2023) < 1:
                        pass

    #print(date_density_list_2023)


    dates_2023 = [item[0] for item in date_density_list_2023]  # Haal de datum uit elk element
    densities_2023 = [float(item[1]) for item in date_density_list_2023 if item[1] != ""]  # Haal de density uit elk element en zet om naar float

    # Print de twee lijsten
    #print("Dates:", dates_2023)
    #print("densities_2023:", densities_2023)



    densities_2023_2  = []
    date_density_list_2023_2 = []
    dates_2023_2 = []
    with open(f'{location}_2023_2.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            
            # Zorg ervoor dat je geen lege rijen hebt
            if len(row) > 0:
                date_and_density_2023_2 = row[0].strip()  # Verwijder eventuele extra spaties aan het begin of einde van de string
                if '""' in date_and_density_2023_2:
                    pass
                else:
                    # Als '""' niet in de string staat, splits dan op basis van de enkele dubbele aanhalingstekens
                    parts_2023_2 = date_and_density_2023_2.split('"')
                    if len(parts_2023_2) > 1:  # Zorg ervoor dat er een waarde na de datum is
                        #print(f"Parts after alternative split: {parts}")
                        date_2023_2 = parts_2023_2[0]
                        density_2023_2 = parts_2023_2[1].strip()  # De waarde na de datum
                        try:
                            densities_2023_2.append(float(density_2023_2))  # Zet de density om naar een float
                        except ValueError:
                            print(f"Fout bij het converteren van density: {density_2023_2}")
                        date_density_list_2023_2.append(parts_2023_2)
                        
                    if len(parts_2023_2) < 1:
                        pass
    dates_2023_2 = [item[0] for item in date_density_list_2023_2]  # Haal de datum uit elk element
    densities_2023_2 = [float(item[1]) for item in date_density_list_2023_2 if item[1] != ""]  # Haal de density uit elk element en zet om naar float


    dates_2023.extend(dates_2023_2)
    densities_2023.extend(densities_2023_2)

    densities_calculated_2023 = []
    for x in densities_2023:
        x = x / 1000000000
        densities_calculated_2023.append(x)
    

#2024 jaar
    # Lijst om de density-waarden op te slaan
    densities_2024 = []
    date_density_list_2024 = []
    dates_2024 = []

    # Lees het CSV-bestand
    with open(f'{location}_2024_1.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            
            # Zorg ervoor dat je geen lege rijen hebt
            if len(row) > 0:
                date_and_density_2024 = row[0].strip()  # Verwijder eventuele extra spaties aan het begin of einde van de string
                if '""' in date_and_density_2024:
                    pass
                else:
                    # Als '""' niet in de string staat, splits dan op basis van de enkele dubbele aanhalingstekens
                    parts_2024 = date_and_density_2024.split('"')
                    if len(parts_2024) > 1:  # Zorg ervoor dat er een waarde na de datum is
                        #print(f"Parts after alternative split: {parts}")
                        date_2024 = parts_2024[0]
                        density_2024 = parts_2024[1].strip()  # De waarde na de datum
                        try:
                            densities_2024.append(float(density_2024))  # Zet de density om naar een float
                        except ValueError:
                            print(f"Fout bij het converteren van density: {density_2024}")
                        date_density_list_2024.append(parts_2024)
                        
                    if len(parts_2024) < 1:
                        pass

    #print(date_density_list_2024)
    # Print de lijst met densities_2024
    #print("densities_2024:", densities_2024, "Dates:", date)


    dates_2024 = [item[0] for item in date_density_list_2024]  # Haal de datum uit elk element
    densities_2024 = [float(item[1]) for item in date_density_list_2024 if item[1] != ""]  # Haal de density uit elk element en zet om naar float

    # Print de twee lijsten
    #print("Dates:", dates_2024)
    #print("densities_2024:", densities_2024)

    densities_2024_2  = []
    date_density_list_2024_2 = []
    dates_2024_2 = []
    with open(f'{location}_2024_2.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            
            # Zorg ervoor dat je geen lege rijen hebt
            if len(row) > 0:
                date_and_density_2024_2 = row[0].strip()  # Verwijder eventuele extra spaties aan het begin of einde van de string
                if '""' in date_and_density_2024_2:
                    pass
                else:
                    # Als '""' niet in de string staat, splits dan op basis van de enkele dubbele aanhalingstekens
                    parts_2024_2 = date_and_density_2024_2.split('"')
                    if len(parts_2024_2) > 1:  # Zorg ervoor dat er een waarde na de datum is
                        #print(f"Parts after alternative split: {parts}")
                        date_2024_2 = parts_2024_2[0]
                        density_2024_2 = parts_2024_2[1].strip()  # De waarde na de datum
                        try:
                            densities_2024_2.append(float(density_2024_2))  # Zet de density om naar een float
                        except ValueError:
                            print(f"Fout bij het converteren van density: {density_2024_2}")
                        date_density_list_2024_2.append(parts_2024_2)
                        
                    if len(parts_2024_2) < 1:
                        pass
    dates_2024_2 = [item[0] for item in date_density_list_2024_2]  # Haal de datum uit elk element
    densities_2024_2 = [float(item[1]) for item in date_density_list_2024_2 if item[1] != ""]  # Haal de density uit elk element en zet om naar float


    dates_2024.extend(dates_2024_2)
    densities_2024.extend(densities_2024_2)

    densities_calculated_2024 = []
    for x in densities_2024:
        x = x / 1000000000
        densities_calculated_2024.append(x)














#2020 jaar BACKGROUND
    # Lijst om de density-waarden op te slaan
    densities_2019_background = []
    date_density_list_2019_background = []
    dates_2019_background = []

    # Lees het CSV-bestand
    with open(f'{location}_2019_1_background.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            
            # Zorg ervoor dat je geen lege rijen hebt
            if len(row) > 0:
                date_and_density_2019_background = row[0].strip()  # Verwijder eventuele extra spaties aan het begin of einde van de string
                if '""' in date_and_density_2019_background:
                    pass
                else:
                    # Als '""' niet in de string staat, splits dan op basis van de enkele dubbele aanhalingstekens
                    parts_2019_background = date_and_density_2019_background.split('"')
                    if len(parts_2019_background) > 1:  # Zorg ervoor dat er een waarde na de datum is
                        #print(f"Parts after alternative split: {parts}")
                        date_2019_background = parts_2019_background[0]
                        density_2019_background = parts_2019_background[1].strip()  # De waarde na de datum
                        try:
                            densities_2019_background.append(float(density_2019_background))  # Zet de density om naar een float
                        except ValueError:
                            print(f"Fout bij het converteren van density: {density_2019_background}")
                        date_density_list_2019_background.append(parts_2019_background)
                        
                    if len(parts_2019_background) < 1:
                        pass

   # print(date_density_list_2019_background)


    dates_2019_background = [item[0] for item in date_density_list_2019_background]  # Haal de datum uit elk element
    densities_2019_background = [float(item[1]) for item in date_density_list_2019_background if item[1] != ""]  # Haal de density uit elk element en zet om naar float

    # Print de twee lijsten
    #print("Dates:", dates_2019_background)
    #print("densities_2019_background:", densities_2019_background)



    densities_2019_background_2  = []
    date_density_list_2019_background_2 = []
    dates_2019_background_2 = []
    with open(f'{location}_2019_2_background.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            
            # Zorg ervoor dat je geen lege rijen hebt
            if len(row) > 0:
                date_and_density_2019_background_2 = row[0].strip()  # Verwijder eventuele extra spaties aan het begin of einde van de string
                if '""' in date_and_density_2019_background_2:
                    pass
                else:
                    # Als '""' niet in de string staat, splits dan op basis van de enkele dubbele aanhalingstekens
                    parts_2019_background_2 = date_and_density_2019_background_2.split('"')
                    if len(parts_2019_background_2) > 1:  # Zorg ervoor dat er een waarde na de datum is
                        #print(f"Parts after alternative split: {parts}")
                        date_2019_background_2 = parts_2019_background_2[0]
                        density_2019_background_2 = parts_2019_background_2[1].strip()  # De waarde na de datum
                        try:
                            densities_2019_background_2.append(float(density_2019_background_2))  # Zet de density om naar een float
                        except ValueError:
                            print(f"Fout bij het converteren van density: {density_2019_background_2}")
                        date_density_list_2019_background_2.append(parts_2019_background_2)
                        
                    if len(parts_2019_background_2) < 1:
                        pass
    dates_2019_background_2 = [item[0] for item in date_density_list_2019_background_2]  # Haal de datum uit elk element
    densities_2019_background_2 = [float(item[1]) for item in date_density_list_2019_background_2 if item[1] != ""]  # Haal de density uit elk element en zet om naar float


    dates_2019_background.extend(dates_2019_background_2)
    densities_2019_background.extend(densities_2019_background_2)

    densities_calculated_2019_background = []
    for x in densities_2019_background:
        x = x / 1000000000
        densities_calculated_2019_background.append(x)


#2020 jaar BACKGROUND
    # Lijst om de density-waarden op te slaan
    densities_2020_background = []
    date_density_list_2020_background = []
    dates_2020_background = []

    # Lees het CSV-bestand
    with open(f'{location}_2020_1_background.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            
            # Zorg ervoor dat je geen lege rijen hebt
            if len(row) > 0:
                date_and_density_2020_background = row[0].strip()  # Verwijder eventuele extra spaties aan het begin of einde van de string
                if '""' in date_and_density_2020_background:
                    pass
                else:
                    # Als '""' niet in de string staat, splits dan op basis van de enkele dubbele aanhalingstekens
                    parts_2020_background = date_and_density_2020_background.split('"')
                    if len(parts_2020_background) > 1:  # Zorg ervoor dat er een waarde na de datum is
                        #print(f"Parts after alternative split: {parts}")
                        date_2020_background = parts_2020_background[0]
                        density_2020_background = parts_2020_background[1].strip()  # De waarde na de datum
                        try:
                            densities_2020_background.append(float(density_2020_background))  # Zet de density om naar een float
                        except ValueError:
                            print(f"Fout bij het converteren van density: {density_2020_background}")
                        date_density_list_2020_background.append(parts_2020_background)
                        
                    if len(parts_2020_background) < 1:
                        pass

   # print(date_density_list_2020_background)


    dates_2020_background = [item[0] for item in date_density_list_2020_background]  # Haal de datum uit elk element
    densities_2020_background = [float(item[1]) for item in date_density_list_2020_background if item[1] != ""]  # Haal de density uit elk element en zet om naar float

    # Print de twee lijsten
    #print("Dates:", dates_2020_background)
    #print("densities_2020_background:", densities_2020_background)



    densities_2020_background_2  = []
    date_density_list_2020_background_2 = []
    dates_2020_background_2 = []
    with open(f'{location}_2020_2_background.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            
            # Zorg ervoor dat je geen lege rijen hebt
            if len(row) > 0:
                date_and_density_2020_background_2 = row[0].strip()  # Verwijder eventuele extra spaties aan het begin of einde van de string
                if '""' in date_and_density_2020_background_2:
                    pass
                else:
                    # Als '""' niet in de string staat, splits dan op basis van de enkele dubbele aanhalingstekens
                    parts_2020_background_2 = date_and_density_2020_background_2.split('"')
                    if len(parts_2020_background_2) > 1:  # Zorg ervoor dat er een waarde na de datum is
                        #print(f"Parts after alternative split: {parts}")
                        date_2020_background_2 = parts_2020_background_2[0]
                        density_2020_background_2 = parts_2020_background_2[1].strip()  # De waarde na de datum
                        try:
                            densities_2020_background_2.append(float(density_2020_background_2))  # Zet de density om naar een float
                        except ValueError:
                            print(f"Fout bij het converteren van density: {density_2020_background_2}")
                        date_density_list_2020_background_2.append(parts_2020_background_2)
                        
                    if len(parts_2020_background_2) < 1:
                        pass
    dates_2020_background_2 = [item[0] for item in date_density_list_2020_background_2]  # Haal de datum uit elk element
    densities_2020_background_2 = [float(item[1]) for item in date_density_list_2020_background_2 if item[1] != ""]  # Haal de density uit elk element en zet om naar float


    dates_2020_background.extend(dates_2020_background_2)
    densities_2020_background.extend(densities_2020_background_2)

    densities_calculated_2020_background = []
    for x in densities_2020_background:
        x = x / 1000000000
        densities_calculated_2020_background.append(x)
    

#2021 jaar BACKGROUND
 # Lijst om de density-waarden op te slaan
    densities_2021_background = []
    date_density_list_2021_background = []
    dates_2021_background = []
# Lees het CSV-bestand
    with open(f'{location}_2021_1_background.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            
            # Zorg ervoor dat je geen lege rijen hebt
            if len(row) > 0:
                date_and_density_2021_background = row[0].strip()  # Verwijder eventuele extra spaties aan het begin of einde van de string
                if '""' in date_and_density_2021_background:
                    pass
                else:
                    # Als '""' niet in de string staat, splits dan op basis van de enkele dubbele aanhalingstekens
                    parts_2021_background = date_and_density_2021_background.split('"')
                    if len(parts_2021_background) > 1:  # Zorg ervoor dat er een waarde na de datum is
                        #print(f"Parts after alternative split: {parts}")
                        date_2021_background = parts_2021_background[0]
                        density_2021_background = parts_2021_background[1].strip()  # De waarde na de datum
                        try:
                            densities_2021_background.append(float(density_2021_background))  # Zet de density om naar een float
                        except ValueError:
                            print(f"Fout bij het converteren van density: {density_2021_background}")
                        date_density_list_2021_background.append(parts_2021_background)
                        
                    if len(parts_2021_background) < 1:
                        pass

    #print(date_density_list_2021_background)


    dates_2021_background = [item[0] for item in date_density_list_2021_background]  # Haal de datum uit elk element
    densities_2021_background = [float(item[1]) for item in date_density_list_2021_background if item[1] != ""]  # Haal de density uit elk element en zet om naar float

    # Print de twee lijsten
    #print("Dates:", dates_2021_background)
    #print("densities_2021_background:", densities_2021_background)



    densities_2021_background_2  = []
    date_density_list_2021_background_2 = []
    dates_2021_background_2 = []
    with open(f'{location}_2021_2_background.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            
            # Zorg ervoor dat je geen lege rijen hebt
            if len(row) > 0:
                date_and_density_2021_background_2 = row[0].strip()  # Verwijder eventuele extra spaties aan het begin of einde van de string
                if '""' in date_and_density_2021_background_2:
                    pass
                else:
                    # Als '""' niet in de string staat, splits dan op basis van de enkele dubbele aanhalingstekens
                    parts_2021_background_2 = date_and_density_2021_background_2.split('"')
                    if len(parts_2021_background_2) > 1:  # Zorg ervoor dat er een waarde na de datum is
                        #print(f"Parts after alternative split: {parts}")
                        date_2021_background_2 = parts_2021_background_2[0]
                        density_2021_background_2 = parts_2021_background_2[1].strip()  # De waarde na de datum
                        try:
                            densities_2021_background_2.append(float(density_2021_background_2))  # Zet de density om naar een float
                        except ValueError:
                            print(f"Fout bij het converteren van density: {density_2021_background_2}")
                        date_density_list_2021_background_2.append(parts_2021_background_2)
                        
                    if len(parts_2021_background_2) < 1:
                        pass
    dates_2021_background_2 = [item[0] for item in date_density_list_2021_background_2]  # Haal de datum uit elk element
    densities_2021_background_2 = [float(item[1]) for item in date_density_list_2021_background_2 if item[1] != ""]  # Haal de density uit elk element en zet om naar float


    dates_2021_background.extend(dates_2021_background_2)
    densities_2021_background.extend(densities_2021_background_2)

    densities_calculated_2021_background = []
    for x in densities_2021_background:
        x = x / 1000000000
        densities_calculated_2021_background.append(x)


#2023 jaar BACKGROUND
 # Lijst om de density-waarden op te slaan
    densities_2023_background = []
    date_density_list_2023_background = []
    dates_2023_background = []
# Lees het CSV-bestand
    with open(f'{location}_2023_1_background.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            
            # Zorg ervoor dat je geen lege rijen hebt
            if len(row) > 0:
                date_and_density_2023_background = row[0].strip()  # Verwijder eventuele extra spaties aan het begin of einde van de string
                if '""' in date_and_density_2023_background:
                    pass
                else:
                    # Als '""' niet in de string staat, splits dan op basis van de enkele dubbele aanhalingstekens
                    parts_2023_background = date_and_density_2023_background.split('"')
                    if len(parts_2023_background) > 1:  # Zorg ervoor dat er een waarde na de datum is
                        #print(f"Parts after alternative split: {parts}")
                        date_2023_background = parts_2023_background[0]
                        density_2023_background = parts_2023_background[1].strip()  # De waarde na de datum
                        try:
                            densities_2023_background.append(float(density_2023_background))  # Zet de density om naar een float
                        except ValueError:
                            print(f"Fout bij het converteren van density: {density_2023_background}")
                        date_density_list_2023_background.append(parts_2023_background)
                        
                    if len(parts_2023_background) < 1:
                        pass

    print(date_density_list_2023_background)


    dates_2023_background = [item[0] for item in date_density_list_2023_background]  # Haal de datum uit elk element
    densities_2023_background = [float(item[1]) for item in date_density_list_2023_background if item[1] != ""]  # Haal de density uit elk element en zet om naar float

    # Print de twee lijsten
    #print("Dates:", dates_2023_background)
    #print("densities_2023_background:", densities_2023_background)



    densities_2023_background_2  = []
    date_density_list_2023_background_2 = []
    dates_2023_background_2 = []
    with open(f'{location}_2023_2_background.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            
            # Zorg ervoor dat je geen lege rijen hebt
            if len(row) > 0:
                date_and_density_2023_background_2 = row[0].strip()  # Verwijder eventuele extra spaties aan het begin of einde van de string
                if '""' in date_and_density_2023_background_2:
                    pass
                else:
                    # Als '""' niet in de string staat, splits dan op basis van de enkele dubbele aanhalingstekens
                    parts_2023_background_2 = date_and_density_2023_background_2.split('"')
                    if len(parts_2023_background_2) > 1:  # Zorg ervoor dat er een waarde na de datum is
                        #print(f"Parts after alternative split: {parts}")
                        date_2023_background_2 = parts_2023_background_2[0]
                        density_2023_background_2 = parts_2023_background_2[1].strip()  # De waarde na de datum
                        try:
                            densities_2023_background_2.append(float(density_2023_background_2))  # Zet de density om naar een float
                        except ValueError:
                            print(f"Fout bij het converteren van density: {density_2023_background_2}")
                        date_density_list_2023_background_2.append(parts_2023_background_2)
                        
                    if len(parts_2023_background_2) < 1:
                        pass
    dates_2023_background_2 = [item[0] for item in date_density_list_2023_background_2]  # Haal de datum uit elk element
    densities_2023_background_2 = [float(item[1]) for item in date_density_list_2023_background_2 if item[1] != ""]  # Haal de density uit elk element en zet om naar float


    dates_2023_background.extend(dates_2023_background_2)
    densities_2023_background.extend(densities_2023_background_2)

    densities_calculated_2023_background = []
    for x in densities_2023_background:
        x = x / 1000000000
        densities_calculated_2023_background.append(x)
    

#2024 jaar BACKGROUND
    # Lijst om de density-waarden op te slaan
    densities_2024_background = []
    date_density_list_2024_background = []
    dates_2024_background = []

    # Lees het CSV-bestand
    with open(f'{location}_2024_1_background.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            
            # Zorg ervoor dat je geen lege rijen hebt
            if len(row) > 0:
                date_and_density_2024_background = row[0].strip()  # Verwijder eventuele extra spaties aan het begin of einde van de string
                if '""' in date_and_density_2024_background:
                    pass
                else:
                    # Als '""' niet in de string staat, splits dan op basis van de enkele dubbele aanhalingstekens
                    parts_2024_background = date_and_density_2024_background.split('"')
                    if len(parts_2024_background) > 1:  # Zorg ervoor dat er een waarde na de datum is
                        #print(f"Parts after alternative split: {parts}")
                        date_2024_background = parts_2024_background[0]
                        density_2024_background = parts_2024_background[1].strip()  # De waarde na de datum
                        try:
                            densities_2024_background.append(float(density_2024_background))  # Zet de density om naar een float
                        except ValueError:
                            print(f"Fout bij het converteren van density: {density_2024_background}")
                        date_density_list_2024_background.append(parts_2024_background)
                        
                    if len(parts_2024_background) < 1:
                        pass

    #print(date_density_list_2024_background)
    # Print de lijst met densities_2024
    #print("densities_2024:", densities_2024, "Dates:", date)


    dates_2024_background = [item[0] for item in date_density_list_2024_background]  # Haal de datum uit elk element
    densities_2024_background = [float(item[1]) for item in date_density_list_2024_background if item[1] != ""]  # Haal de density uit elk element en zet om naar float

    # # Print de twee lijsten
    # print("Dates:", dates_2024_background)
    # print("densities_2024:", densities_2024_background)

    densities_2024_background_2  = []
    date_density_list_2024_background_2 = []
    dates_2024_background_2 = []
    with open(f'{location}_2024_2_background.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            
            # Zorg ervoor dat je geen lege rijen hebt
            if len(row) > 0:
                date_and_density_2024_background_2 = row[0].strip()  # Verwijder eventuele extra spaties aan het begin of einde van de string
                if '""' in date_and_density_2024_background_2:
                    pass
                else:
                    # Als '""' niet in de string staat, splits dan op basis van de enkele dubbele aanhalingstekens
                    parts_2024_background_2 = date_and_density_2024_background_2.split('"')
                    if len(parts_2024_background_2) > 1:  # Zorg ervoor dat er een waarde na de datum is
                        #print(f"Parts after alternative split: {parts}")
                        date_2024_background_2 = parts_2024_background_2[0]
                        density_2024_background_2 = parts_2024_background_2[1].strip()  # De waarde na de datum
                        try:
                            densities_2024_background_2.append(float(density_2024_background_2))  # Zet de density om naar een float
                        except ValueError:
                            print(f"Fout bij het converteren van density: {density_2024_background_2}")
                        date_density_list_2024_background_2.append(parts_2024_background_2)
                        
                    if len(parts_2024_background_2) < 1:
                        pass
    dates_2024_background_2 = [item[0] for item in date_density_list_2024_background_2]  # Haal de datum uit elk element
    densities_2024_background_2 = [float(item[1]) for item in date_density_list_2024_background_2 if item[1] != ""]  # Haal de density uit elk element en zet om naar float


    dates_2024_background.extend(dates_2024_background_2)
    densities_2024_background.extend(densities_2024_background_2)

    densities_calculated_2024_background = []
    for x in densities_2024_background:
        x = x / 1000000000
        densities_calculated_2024_background.append(x)






#dataframes voor alle jaren
    # # Maak pandas DataFrame's voor de jaren 2020 en 2024
    df_2019 = pd.DataFrame({'Date': dates_2019, 'Density': densities_calculated_2019})
    df_2020 = pd.DataFrame({'Date': dates_2020, 'Density': densities_calculated_2020})
    df_2021 = pd.DataFrame({'Date': dates_2021, 'Density': densities_calculated_2021})
    df_2023 = pd.DataFrame({'Date': dates_2023, 'Density': densities_calculated_2023})
    df_2024 = pd.DataFrame({'Date': dates_2024, 'Density': densities_calculated_2024})
    df_2019_background = pd.DataFrame({'Date': dates_2019_background, 'Density': densities_calculated_2019_background})
    df_2020_background = pd.DataFrame({'Date': dates_2020_background, 'Density': densities_calculated_2020_background})
    df_2021_background = pd.DataFrame({'Date': dates_2021_background, 'Density': densities_calculated_2021_background})
    df_2023_background = pd.DataFrame({'Date': dates_2023_background, 'Density': densities_calculated_2023_background})
    df_2024_background = pd.DataFrame({'Date': dates_2024_background, 'Density': densities_calculated_2024_background})

    # # Zet de datumkolom als index
    df_2019['Date'] = pd.to_datetime(df_2019['Date'])
    df_2020['Date'] = pd.to_datetime(df_2020['Date'])
    df_2021['Date'] = pd.to_datetime(df_2021['Date'])
    df_2023['Date'] = pd.to_datetime(df_2023['Date'])
    df_2024['Date'] = pd.to_datetime(df_2024['Date'])
    df_2019_background['Date'] = pd.to_datetime(df_2019_background['Date'])
    df_2020_background['Date'] = pd.to_datetime(df_2020_background['Date'])
    df_2021_background['Date'] = pd.to_datetime(df_2021_background['Date'])
    df_2023_background['Date'] = pd.to_datetime(df_2023_background['Date'])
    df_2024_background['Date'] = pd.to_datetime(df_2024_background['Date'])

    #maanden aanmaken
    df_2019['month']= df_2019['Date'].dt.month
    df_2020['month']= df_2020['Date'].dt.month
    df_2021['month']= df_2021['Date'].dt.month
    df_2023['month']= df_2023['Date'].dt.month
    df_2024['month']= df_2024['Date'].dt.month
    df_2019_background['month']= df_2019_background['Date'].dt.month
    df_2020_background['month']= df_2020_background['Date'].dt.month
    df_2021_background['month']= df_2021_background['Date'].dt.month
    df_2023_background['month']= df_2023_background['Date'].dt.month
    df_2024_background['month']= df_2024_background['Date'].dt.month

    # # Groepeer per maand en bereken het maandgemiddelde
    df_2019.set_index('Date', inplace=True)
    df_2020.set_index('Date', inplace=True)
    df_2021.set_index('Date', inplace=True)
    df_2023.set_index('Date', inplace=True)
    df_2024.set_index('Date', inplace=True)
    df_2019_background.set_index('Date', inplace=True)
    df_2020_background.set_index('Date', inplace=True)
    df_2021_background.set_index('Date', inplace=True)
    df_2023_background.set_index('Date', inplace=True)
    df_2024_background.set_index('Date', inplace=True)
    

    #jaar dataframes aanmaken
    df_2019['year']= 2019
    df_2020['year']= 2020
    df_2021['year']= 2021
    df_2023['year']= 2023
    df_2024['year']= 2024
    df_2019_background['year']= 2019
    df_2020_background['year']= 2020
    df_2021_background['year']= 2021
    df_2023_background['year']= 2023
    df_2024_background['year']= 2024

    # # Bereken het maandgemiddelde van de NO₂-dichtheid
    monthly_avg_2019 = df_2019.resample('M').mean()
    monthly_avg_2020 = df_2020.resample('M').mean()
    monthly_avg_2021 = df_2021.resample('M').mean()
    monthly_avg_2023 = df_2023.resample('M').mean()
    monthly_avg_2024 = df_2024.resample('M').mean()
    monthly_avg_2019_background = df_2019_background.resample('M').mean()
    monthly_avg_2020_background = df_2020_background.resample('M').mean()
    monthly_avg_2021_background = df_2021_background.resample('M').mean()
    monthly_avg_2023_background = df_2023_background.resample('M').mean()
    monthly_avg_2024_background = df_2024_background.resample('M').mean()

    # Netto maandgemiddelde berekenen door de achtergrondwaarden af te trekken van de totale waarden
    netto_monthly_avg_2019 = monthly_avg_2019['Density'] - monthly_avg_2019_background['Density']
    netto_monthly_avg_2020 = monthly_avg_2020['Density'] - monthly_avg_2020_background['Density']
    netto_monthly_avg_2021 = monthly_avg_2021['Density'] - monthly_avg_2021_background['Density']
    netto_monthly_avg_2023 = monthly_avg_2023['Density'] - monthly_avg_2023_background['Density']
    netto_monthly_avg_2024 = monthly_avg_2024['Density'] - monthly_avg_2024_background['Density']
    

    months_axis = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    plt.plot(months_axis, monthly_avg_2019['Density'], 'o-',label='Average NO₂ 2019')
    plt.plot(months_axis, monthly_avg_2020['Density'], 'o-',label='Average NO₂ 2020')
    plt.plot(months_axis, monthly_avg_2021['Density'], 'o-',label='Average NO₂ 2021')
    plt.plot(months_axis, monthly_avg_2023['Density'], 'o-',label='Average NO₂ 2023')
    plt.plot(months_axis, monthly_avg_2024['Density'], 'o-',label='Average NO₂ 2024')
    plt.xlabel('Date (Month-Year)')
    plt.ylabel('Average NO₂ Density (mol/m²)')
    plt.title(f'(Heathrow {location} average monthly NO₂ density)')

    # Voeg de legenda toe
    plt.legend(loc='upper left')

    plt.tight_layout()
    plt.show()

    plt.plot(months_axis, netto_monthly_avg_2019, 'o-',label='Average NO₂ 2019')
    plt.plot(months_axis, netto_monthly_avg_2020, 'o-',label='Average NO₂ 2020')
    plt.plot(months_axis, netto_monthly_avg_2021, 'o-',label='Average NO₂ 2021')
    plt.plot(months_axis, netto_monthly_avg_2023, 'o-',label='Average NO₂ 2023')
    plt.plot(months_axis, netto_monthly_avg_2024, 'o-',label='Average NO₂ 2024')
    plt.xlabel('Date (Month-Year)')
    plt.ylabel('Average NO₂ Density (mol/m²)')
    plt.title(f'(Heathrow {location} average monthly NO₂ density)')

    # Voeg de legenda toe
    plt.legend(loc='upper left')

    plt.tight_layout()
    plt.show()


    df_big = pd.concat([df_2019, df_2020, df_2021, df_2023, df_2024])
    sns.boxplot(df_big, x='month' , y="Density", hue="year")
    plt.show()

   # print(df_big)


    # Totale uitstoot per jaar berekenen
    total_density_2019 = df_2019['Density'].sum()
    total_density_2020 = df_2020['Density'].sum()
    total_density_2021 = df_2021['Density'].sum()
    total_density_2023 = df_2023['Density'].sum()
    total_density_2024 = df_2024['Density'].sum()
    total_density_2019_background = df_2019_background['Density'].sum()
    total_density_2020_background = df_2020_background['Density'].sum()
    total_density_2021_background = df_2021_background['Density'].sum()
    total_density_2023_background = df_2023_background['Density'].sum()
    total_density_2024_background = df_2024_background['Density'].sum()

    # Overzicht maken
    total_emissions = {
        'Year': [2019, 2020, 2021, 2023, 2024],
        'Total NO2 Emission': [total_density_2019, total_density_2020, total_density_2021, total_density_2023, total_density_2024],
        'Total NO2 Emission background': [total_density_2019_background, total_density_2020_background, total_density_2021_background, total_density_2023_background, total_density_2024_background]
    }

    # Pandas DataFrame maken voor overzicht
    df_total_emissions = pd.DataFrame(total_emissions)


    print(df_total_emissions)

    # print(netto_monthly_avg_2020)

airport_emission(location="London")
