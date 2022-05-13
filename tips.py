#tip calculator
# ***Kp Martin

bill = int(float(input("What is your bill total? ").replace("$","")))

tip1 = bill * .15
tip2 = bill * .18
tip3 = bill * .20

print(f"Tip totals come to 15% ${tip1:.2f}, 18% ${tip2:.2f}, and 20% ${tip3:.2f}  ")