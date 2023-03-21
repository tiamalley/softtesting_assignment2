# function to calculate user's bmi
def calculateBMI(heightIN, weightLB):
    weight = weightLB * .45

    height = heightIN * .025

    calc = height * height

    bmi = (weight/calc)

    rounded_bmi = "{:.1f}".format(bmi)

    return(rounded_bmi)

# function to display the user's category
def categoryBMI(bmi):
    if(bmi < '18.5'):
        return('Underweight')
    
    elif((bmi >= '18.5') and (bmi < '25.0')):
        return('Normal Weight')

    elif((bmi >= '25.0') and (bmi < '30.0')):
        return('Overweight')

    elif(bmi >= '30.0'):
        return('Obese')


def main():
    print('\n--- BMI Calculator ---')
    print('Height')

    feet = float(input('Feet: '))
    inches = float(input('Inches: '))

    heightIN = (feet * 12) + inches

    weightLB = float(input('\nWeight(lb): '))

    (user_bmi) = calculateBMI(heightIN, weightLB)
    user_category = categoryBMI(user_bmi)

    print('\n--- Results ---')
    print('BMI: {}'.format(user_bmi))
    print('Category: {}\n'.format(user_category))

if __name__ == "__main__":
    main()
