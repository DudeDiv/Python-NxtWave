#A company decided to give a bonus of 5% to an employee if his/her years of service is more than five years.
#Write a program that reads an employee's salary and years of service and decides whether the employee gets the bonus or not.
salary = int(input())
years_of_service = int(input())

if(years_of_service>5):
    print((5/100)*salary)
else:
    print("No Bonus")
