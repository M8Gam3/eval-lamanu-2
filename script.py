import numpy as np
import matplotlib.pyplot as plt

# Initial year
original_date = 2016
date = original_date

# Dictionary to store temperature data
temp_dict = {}

# Loop to read temperature data for 7 years
for item in range(7):
    # Initialize a nested dictionary for the current year
    temp_dict[str(date)] = {}

    # Read temperature data from CSV files
    tmax = np.genfromtxt('./data/' + str(date) + '/tmax.csv', delimiter=',')
    tmin = np.genfromtxt('./data/' + str(date) + '/tmin.csv', delimiter=',')
    tmoy = np.genfromtxt('./data/' + str(date) + '/tmoy.csv', delimiter=',')

    # Convert data to NumPy arrays
    tmax = np.array(tmax)
    tmin = np.array(tmin)
    tmoy = np.array(tmoy)

    # Combine temperature data into a single array
    temp = np.array((tmax, tmin, tmoy))
    temp = np.column_stack(temp)
    
    # Calculate temperature difference and add it to the array
    tdelta = tmax - tmin
    tdelta = tdelta.reshape(temp.shape[0], 1)
    temp = np.append(temp, tdelta, axis=1)
    
    # Store temperature data in the dictionary
    temp_dict[str(date)]['values'] = temp
    
    # Calculate and store additional temperature statistics
    temp_dict[str(date)]['tmax'] = np.max(temp_dict[str(date)]['values'][:, 0])
    temp_dict[str(date)]['tmin'] = np.min(temp_dict[str(date)]['values'][:, 1])
    temp_dict[str(date)]['tmoy'] = np.mean(temp_dict[str(date)]['values'][:, 2])
    temp_dict[str(date)]['tmean'] = np.mean(temp_dict[str(date)]['values'][:, 3])
    
    # Move to the next year
    date += 1

# Display the temperature dictionary
# print(temp_dict)

# Dictionary to store calculated temperature values over the years
values = {
    "tmax": [],
    "tmin": [],
    "tmoy": [],
    "tmean": []
}

# Extract calculated values from the temperature dictionary
for date, item in temp_dict.items():
    values['tmax'].append(item['tmax'])
    values['tmin'].append(item['tmin'])
    values['tmoy'].append(item['tmoy'])
    values['tmean'].append(item['tmean'])

# List to store years
dates = []
for date, item in temp_dict.items():
    dates.append(date)

# Convert lists to NumPy arrays for plotting
xtmax = np.array(dates)
ytmax = np.array(values['tmax'])
xtmin = np.array(dates)
ytmin = np.array(values['tmin'])
xtmoy = np.array(dates)
ytmoy = np.array(values['tmoy'])
xtmean = np.array(dates)
ytmean = np.array(values['tmean'])

# Plotting temperature data over the years
plt.plot(xtmax, ytmax, label='température max')
plt.plot(xtmin, ytmin, label='température min')
plt.plot(xtmoy, ytmoy, label='température moyenne')
plt.plot(xtmean, ytmean, label='moyenne écart de température')

# Adding labels and title
plt.ylabel('Températures')
plt.xlabel('Années')
plt.title('Evolution des températures sur ces 7 dernières années')

# Adding legend
plt.legend(title='Températures')

print(temp_dict)
# Display the plot
plt.show()





## moi
#Les courbes révèlent des fluctuations subtiles, suggérant une tendance générale à l'augmentation des températures au fil des années. Ces résultats indiquent un possible impact du réchauffement climatique, avec une hausse d'environ 3 degrés sur l'ensemble des courbes de 2016 à 2022.
# je remarque que chacune des courbes montre de légères fluctuations dont des résultats qui démontrent l'augmentation de la température général d'années en années laissant paraître l'impact du réchauffement climatique. une augmentation d'environ 3 degrés sur chacune des courbes de 2016 a 2022.

## gpt