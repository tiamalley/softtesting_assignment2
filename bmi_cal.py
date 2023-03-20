# function to calculate user's bmi
def calculateBMI(heightIN, weightLB):
    weight = weightLB * .45

    height = heightIN * .025

    calc = height * height

    bmi = (weight/calc)

    return(bmi)

# function to display the user's category
def categoryBMI(bmi):
    if(bmi < 18.5):
        return('Underweight')
    
    elif((bmi >= 18.5) and (bmi < 24.9)):
        return('Normal Weight')

    elif((bmi >= 24.9) and (bmi < 29.9)):
        return('Overweight')

    elif(bmi >= 29.9):
        return('Obese')



print('\n--- BMI Calculator ---')
print('Height')

feet = float(input('Feet: '))
inches = float(input('Inches: '))

heightIN = (feet * 12) + inches

weightLB = float(input('\nWeight(lb): '))

user_bmi = calculateBMI(heightIN, weightLB)
user_bmi_rounded = "{:.1f}".format(user_bmi)
user_category = categoryBMI(user_bmi)

print('\n--- Results ---')
print('BMI: {}'.format(user_bmi_rounded))
print('Category: {}\n'.format(user_category))