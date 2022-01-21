import json
import tabulate

def calculate_bmi(weight_kg, height_cm):
    bmi = weight_kg / (height_cm/100)**2
    return (bmi)

def calculate_bmi_category_health_risk(bmi):

    if bmi <= 18.4:
        return "Underweight", "Malnutrition risk"
    elif    bmi >= 18.5 and bmi <= 24.9:  
        return "Normal weight", "Low risk"
    elif    bmi >= 25 and bmi <= 29.9:  
        return "Overweight", "Enhanced risk"
    elif    bmi >= 30 and bmi <= 34.9:  
        return "Moderately obese", "Medium risk"
    elif    bmi >= 35 and bmi <= 39.9:  
        return "Severely obese", "High risk"
    elif    bmi >= 40:
        return "Very severely obese", "Very high risk"

def calculate_overweight(bmi_category):

    if (bmi_category == "Overweight"):
        return 1
    else:
        return 0

def print_table(bmi_list):
    header = bmi_list[0].keys()
    rows =  [x.values() for x in bmi_list]
    print (tabulate.tabulate(rows, header))

input_file = open ('bmi_data.json')
json_array = json.load(input_file)
bmi_list = []

num_overweight=0

for item in json_array:
    bmi_details = {"Gender":None, "HeightCm":None, "WeightKg" : None, "BMI" : None, "BMICategory": None, "Healthrisk": None}
    bmi_details['Gender'] = item['Gender']
    bmi_details['HeightCm'] = item['HeightCm']
    bmi_details['WeightKg'] = item['WeightKg']
    bmi_details['BMI'] = calculate_bmi(item['WeightKg'], item['HeightCm'])
    bmi_details['BMICategory'], bmi_details['Healthrisk'] = calculate_bmi_category_health_risk(bmi_details['BMI'])

    num_overweight+=calculate_overweight(bmi_details['BMICategory'])

    bmi_list.append(bmi_details)

print_table(bmi_list)

print("\n Number of Overweight: ", num_overweight)

