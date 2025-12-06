# Sean Hendry
# Date
# P4HW1
# Program that collects multiple scores, validates them,
# removes the lowest score, calculates the average, and
# displays the letter grade.


num_scores = int(input("How many scores do you want to enter? "))

scores = []

for i in range(1, num_scores + 1):
    score = float(input(f"Enter score #{i}: "))
    while score < 0 or score > 100:
        print("\nINVALID Score entered!!!!")
        print("Score should be between 0 and 100")
        score = float(input(f"Enter score #{i} again: "))
    scores.append(score)

lowest = min(scores)
scores.remove(lowest)
average = sum(scores) / len(scores)

if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

print("\n--------------Results--------------")
print(f"Lowest Score  : {lowest:.1f}")
print(f"Modified List : {scores}")
print(f"Scores Average: {average:.2f}")
print(f"Grade         : {grade}")
print("-----------------------------------")


# Pseudocode:
# 1. Ask the user how many scores they want to enter.
# 2. Create an empty list to store scores.
# 3. Use a loop to collect and validate each score.
# 4. If score < 0 or > 100, display error message and ask again.
# 5. Find the lowest score.
# 6. Remove the lowest score from the list.
# 7.Calculate average of remaining scores.
# 9.Determine letter grade based on average.
#  Display lowest score, modified list, average, and letter grade.
