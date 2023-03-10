##
# class_scores.py
# Calculates the mean, lowest and highest scores
# of class_a list and class_b list combined
# Then prints them out
# Author: Eva Melling
# Date: 02.03.2023

# Function to calculate the average of lists
def average(list_class):
    # Create variables - count and total_score
    count = 0
    total_score = 0

    # Loop through list with a for loop
    for score in list_class:
        count += 1  # add 1 for everytime it loops through
        total_score += score    # add score onto total_score

    # Store total_score divided by count in variable called mean
    mean = total_score / count

    return mean
    

if __name__ == "__main__":

    # Defines class_a list and class_b list
    class_a = [44, 33, 28, 47, 12, 28, 32, 31, 11, 39, 40, 26, 36]
    class_b = [19, 26, 38, 31, 30, 42, 44, 14, 27, 43, 46, 49, 24, 26, 36]

    # Ask user if they want to add a score to both classes
    user_a = float(input("Score that you want to add to class a: "))
    user_b = float(input("Score that you want to add to class b: "))

    # Append users scores to class_a and class_b
    class_a.append(user_a)
    class_b.append(user_b)

    # Ask user if they want to modify list
    modify_class_a = input("Modify class a list? (y/n): ")
    if modify_class_a == "y":   # if y, ask user for index and replacing score
        where = int(input("Index of score you want to modify: "))
        what = int(input("What do you want to replace it with?: "))
        class_a[where] = what   # replace users index and replacing score
        
    modify_class_b = input("Modify class b list? (y/n): ")
    if modify_class_b == "y":   # if y, ask user for index and replacing score
        where = int(input("Index of score you want to modify: "))
        what = int(input("What do you want to replace it with?: "))
        class_b[where] = what   # replace users index and replacing score


    # Combined list equals class_a list plus class_b list
    combined_list = class_a + class_b


    # Print the title - 'Class Scores Part 1'
    print("Class Scores Part 1\n")

    # Print mean, lowest and highest score for combined list
    print("Mean score for both classes is: {}".format(average(combined_list)))
    print("Lowest score for both classes is: {}".format(min(combined_list)))
    print("Highest score for both classes is: {}".format(max(combined_list)))

    # Print mean, lowest and highest score for class_a list
    print("\nMean score for class a is: {}".format(average(class_a)))
    print("Lowest score for class a is: {}".format(min(class_a)))
    print("Highest score for class a is: {}".format(max(class_a)))

    # Print mean, lowest and highest score for class_b list
    print("\nMean score for class b is: {}".format(average(class_b)))
    print("Lowest score for class b is: {}".format(min(class_b)))
    print("Highest score for class b is: {}".format(max(class_b)))

