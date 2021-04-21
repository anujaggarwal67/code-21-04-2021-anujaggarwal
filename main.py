import sys
import json

def solve(data):
    result = []
    print(data)
    overweight = 0
    for ob in data:
            BMI = ob["WeightKg"]/(ob["HeightCm"]*ob["HeightCm"]/10000)
            BMI = round(BMI, 2)
            countofoverweight = 0
            BMICategory = ""
            HealthRisk = ""
            if BMI <= 18.4:
                BMICategory = "Under Weight"
                BMIRisk = "Malnutrition risk"
            elif BMI >=18.5 and BMI<=24.9:
                BMICategory = "Normal weight"
                BMIRisk = "Low risk"
            elif BMI >=25 and BMI<=29.9:
                BMICategory = "Overweight"
                BMIRisk = "Enhanced risk"
                overweight +=1
            elif BMI >=30 and BMI<=34.9:
                BMICategory = "Moderately obese"
                BMIRisk = "Medium risk"
            elif BMI >=35 and BMI<=39.9:
                BMICategory = "Severely obese"
                BMIRisk = "Very high risk"
            else:
                BMICategory = "Very severely obese"
                BMIRisk = "Malnutrition risk"
                
            temp = ob
            temp.update({"BMI":BMI, "BMICategory":BMICategory, "BMIRisk":BMIRisk})
            result.append(temp)
    return overweight, result




if __name__=="__main__":
    filepath = input("please provide the filepath contains jsondata\n")
    f = open(filepath,)
    data = json.load(f)
    overweight, res = solve(data)
    print(overweight, res)
    output = {}
    output['Overweight'] = overweight
    output['data'] = res
    with open('data.json', 'w') as outfile:
        json.dump(output, outfile, indent=4)