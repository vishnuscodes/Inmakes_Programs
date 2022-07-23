def BMICalculator(height,weight):
    BMI = weight/(height)**2
    return BMI

height = float(input("Enter your height in metres"))
weight = float(input("Enter your weight in kg"))
print(BMICalculator(height,weight))