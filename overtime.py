print("Weekly Overtime Calculator")

total = 0.0

Days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

for i in range(5):
    overtime = float(input("Enter Overtime to the nearest Quarter-hour for " + str(Days[i]) + ": "))
    total += overtime

print(str(total) + " Hours")
print("Also Known As: ", str(total * 60), "Minutes")