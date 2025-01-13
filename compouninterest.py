question1 = str(input("Do u wanna to invest some money by % of getting every year?(Y/N): "))

if question1 == "Y":
    print("Alright!")
else:
    print("Have a nice day, see you!")
    breakpoint()

profile_name = input("Enter ur full name: ")
while not profile_name.isalpha():
    print("You profile name can't contain any numbers")
    profile_name = input("Enter ur full name: ")
while not profile_name.find(" ") == -1:
    print("Your profile name can't contain spaces")
    profile_name = input("Enter ur full name: ")
while len(profile_name) > 12:
    print("Your profile name is more than 12 characters or equal 12 characters")
    profile_name = input("Enter ur full name: ")
else: print(f"Welcome , {profile_name}")

age = int(input("Enter your age: "))

while age < 18:
    print("You haven't allowed to invest, see you later")
    age = int(input("Enter your age: "))
else:
    print(f"Okey, now u've allowed to invest")


principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = int(input("Enter the principle amount: "))
    if principle <= 0:
        print("Principle can't be less than or equal to zero")

while rate <= 0:
    rate = int(input("Enter the principle rate(Our rate is 10%/year): "))
    if rate <= 0:
        print("rate can't be less than or equal to zero")
while time <= 0:
    time = int(input("Enter the principle time in years: "))
    if time <= 0:
        print("Time can't be less than or equal to zero")

total_bonus = principle * pow((1 + rate / 100), time)
print(f"Your balance will be: {total_bonus:.2f}$ after {time} year/s")