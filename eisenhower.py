print("Welcome to the Eisenhower matrix prioritization app!")

# Get user input for tasks
important_urgent = input("Enter tasks that are important and urgent (separated by commas): ").split(",")
important_not_urgent = input("Enter tasks that are important but not urgent (separated by commas): ").split(",")
not_important_urgent = input("Enter tasks that are not important but urgent (separated by commas): ").split(",")
not_important_not_urgent = input("Enter tasks that are not important and not urgent (separated by commas): ").split(",")

# Print out tasks in the appropriate quadrants of the matrix
print("\nHere are your tasks:\n")
print("Important and Urgent:")
for task in important_urgent:
    print(" - " + task)
print("\nImportant but Not Urgent:")
for task in important_not_urgent:
    print(" - " + task)
print("\nNot Important but Urgent:")
for task in not_important_urgent:
    print(" - " + task)
print("\nNot Important and Not Urgent:")
for task in not_important_not_urgent:
    print(" - " + task)
