# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np

import matplotlib.pyplot as plt
## for 2020input8 dataset
df=np.genfromtxt('2020input8.csv',delimiter='')

## for 2024inputdataset
df1=np.genfromtxt('2024input8.csv',delimiter='')
"""
midpoint = the addition of the class interval/2 

mean=multiplication of midpoint * column 3 (which is the frequency)

"""
# Extract the first two columns
column1 = df[:, 0]
column2 = df[:, 1]

# Extract the third column
column3 = df[:, 2]

# Calculate the sum of the first two columns and divide by 2
midpoint = (column1 + column2) / 2

# Multiply the sum by the values in the third column
mean = midpoint * column3

# Calculate the total number of values in the third column
frequency = np.sum(column3)

# Calculate the mean using the calculated sum and the total number of values in the third column
sum_third_columns = np.sum(mean)

mean_2020=np.round(sum_third_columns/frequency,4)

print("Mean for 2020 dataset", mean_2020)








## standard deviation
"""
final first value is the summation of x-x(bar)

freq = frequency 

std = standard deviation 
"""


first_value =(midpoint-mean_2020)**2

final_first_value =np.sum(first_value)

first_freq_value= first_value*column3

final_first_freq= np.sum(first_freq_value)

freq= frequency - 1

std=np.sqrt(final_first_freq/frequency)

std=np.round(std,4)

print ('standard deviation for 2020 dataset',std)






## Value V calculation for 2020 dataset
# Sort the grades in ascending order
sorted_grades_2020 = np.sort(midpoint)

# Calculate the index corresponding to the 90th percentile (top 10% of grades)
index_90th_percentile = int(0.9 * len(sorted_grades_2020))

##index_90th_percentile_2020 = np.argmax(cum_total_students_2020 >= 0.9 * total_students_2020)

# Determine the grade value at the 90th percentile
grade_90th_percentile = sorted_grades_2020[index_90th_percentile]

grade_90th_percentile =np.round(grade_90th_percentile ,4)
print("Grade value at the 90th percentile (V):", grade_90th_percentile)





"""
sum_2024= sum of the numbers in the column 
num_values_2024= total number in the column

"""


## mean for 2024 dataset
# Calculate the sum of values and the total number of values for 2024
sum_2024= np.sum(df1)
num_values_2024 = len(df1)


# Calculate the mean for 2020 using the simple formula
mean_2024 = sum_2024 / num_values_2024
mean_2024 =np.round(mean_2024 ,4)
print("Mean for 2024 dataset:", mean_2024)

## standard deviation


second_mean= (df1-mean_2024)**2
final_second_mean=np.sum(second_mean)

frequency2= num_values_2024

std2=np.sqrt(final_second_mean/frequency2)
std2=np.round(std2,4)

print ('standard deviation for 2024 dataset',std2)




## Value V calculation for 2020 dataset
# Sort the grades in ascending order
sorted_grades_2024 = np.sort(df1)

# Calculate the index corresponding to the 90th percentile (top 10% of grades)
index_90th_percentile2 = int(0.9 * len(sorted_grades_2024))

##index_90th_percentile_2020 = np.argmax(cum_total_students_2020 >= 0.9 * total_students_2020)

# Determine the grade value at the 90th percentile
grade_90th_percentile2 = sorted_grades_2024[index_90th_percentile2]
grade_90th_percentile2=np.round(grade_90th_percentile2,4)
print("Grade value at the 90th percentile (V):", grade_90th_percentile2)






# Plot histograms for the entire datasets
plt.hist(df.flatten(), bins=20, color='blue', alpha=0.7, label='2020 Dataset')
plt.hist(df1.flatten(), bins=20, color='green', alpha=0.7, label='2024 Dataset')

# Add vertical lines for mean, mean ± std deviation, and 90th percentile for 2020 dataset
plt.axvline(mean_2020, color='red', linestyle='--', label='Mean (2020)=60.7067')
plt.axvline(std, color='purple', linestyle='--', label='std(2020)=14.3919')
plt.axvline(grade_90th_percentile, color='purple', linestyle='--', label='90th Percentile (2020)=90.0')

# Add vertical lines for mean, mean ± std deviation, and 90th percentile for 2024 dataset
plt.axvline(mean_2024, color='black', linestyle='--', label='Mean (2024)=67.1821')
plt.axvline(std2, color='gray', linestyle='--', label='std (2024)= 13.2516')
plt.axvline(grade_90th_percentile2, color='gray', linestyle='--', label='90th Percentile (2024)= 85.0')
# Add labels and legend
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Histogram of Datasets 2020 and 2024 with Statistics')
plt.legend()

# Show plot
plt.show()