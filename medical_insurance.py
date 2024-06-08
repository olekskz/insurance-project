import csv
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd




age = []
sex = []
bmi = []
children = []
smoker = []
region = []
charges = []


with open('insurance.csv') as main_file:
    main_file_read = csv.DictReader(main_file)
    for i in main_file_read:
        age.append(i['age'])
        sex.append(i['sex'])
        bmi.append(i['bmi'])
        children.append(i['children'])
        smoker.append(i['smoker'])
        region.append(i['region'])
        charges.append(i['charges'])


#AVARAGE AGE OF PEOPLE

total_age = 0
for i in age:
    total_age += int(i)    
avarage_age = total_age/len(age) 
print("Avarage age of insurance list is " + str(round(avarage_age, 1))+ "years.")

###################################

#MAJORITY OF PEOPLE THAT CAME FROM

def major_counter():
    region_list = []
    northwest = region.count("northwest")
    northeast = region.count("northeast")
    southwest = region.count("southwest")
    southeast = region.count("southeast")
    region_list.append(northeast)
    region_list.append(northwest)
    region_list.append(southeast)
    region_list.append(southwest)
    max_value = max(region_list)
    print("Majority of people come from  southwest which count is " + str(max_value))
    
major_counter()

##########################################


#avarage age if the person has at least one child

age_child_dict = {key: value for key, value in zip(age, children)}
one_more_child_list = []
for i in age_child_dict:
    if int(age_child_dict.get(i)) >= 1:
        one_more_child_list.append(i) 



total_age_kid = 0

for i in one_more_child_list:
    total_age_kid += int(i)
    
avarage_age_kid = round(total_age_kid/len(one_more_child_list), 1)
print("Avarage age which have at least one kid is "+ str(avarage_age_kid))




# avarage cost if the person has at least one children
one_more_charges_list = []

cost_children_dict = {key: value for key, value in zip(charges, children)}
for i in cost_children_dict:
    if float(cost_children_dict.get(i)) >= 1:
        one_more_charges_list.append(i)
        
total_cost = 0

for i in one_more_charges_list:
    total_cost += float(i)
    
avarage_cost = total_cost/len(one_more_charges_list)
print("People that have at least one kid, avarage cost is " + str(round(avarage_cost)))    
    



##############################################################
#USING PANDAS


insurance_csv = pd.read_csv('insurance.csv')


#smoker vs not smoker charges
smoker_df =  insurance_csv.groupby('smoker').charges.mean().reset_index()



#people that majority come from
majority_counter = insurance_csv.region.max()
print(majority_counter)

insurance_csv.region.value_counts().plot.pie()
#plt.show()
plt.close()

#BMI to age

bmi_to_age = insurance_csv.groupby('age').bmi.mean().reset_index()
#print(bmi_to_age)


#CHILDREN TO CHARGES


children_cost = insurance_csv.groupby('children').charges.mean().round(1)
print(children_cost)
 
 
children_cost_series = pd.Series(insurance_csv['charges'], index=insurance_csv['children'], name='children')
children_cost_series.plot.pie()
#plt.show()
plt.close()









