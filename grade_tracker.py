"""
author: Japjot Singh Rajbans
date: September 29, 2025
Student Grade Tracker
"""

# Using import time to make the program feel fancier and fluid!
import time

def reading_data(filename):
    """
    This function reads student names and marks from a text file.

    Args:
        Name of the input file = filename

    Returns:
        List of lists containing student data = students
    """
    students = []

    # Opening and reading the text file
    with open(filename, "r") as file:
        lines = file.readlines()

    # Now the function will split "=" and strip away "," to read marks as well as the student's name
    for line_num, line in enumerate(lines, 1):
        line = line.strip()
        if '=' in line:
            parts = line.split('=')
            name = parts[0].strip()
            marks_string = parts[1].strip()
            mark_strings = marks_string.split(",")
            marks = []

            # The function will now add the floats into the marks list
            for mark_str in mark_strings:
                    mark_str = mark_str.strip()
                    if mark_str:
                        mark = float(mark_str)
                        if 0 <= mark <= 100:
                            marks.append(mark)

            # Now it will create a student data list if marks exist
            average = sum(marks) / len(marks)
            student_data = [name, marks, average]
            students.append(student_data)
    return students

def statistics(students):
    """
    This function calculates different statistics for the class.
   
    Args:
        List of student data lists = students (list)
   
    Returns:
        List containing statistics of the entire class = stats (list)
    """
    # If the function cannot find the students list
    if not students:
        return [0, 0, 0, 0, 0, 0, 0]
    averages = []
    for student in students:
        average = student[2]
        averages.append(average)
   
    class_average = sum(averages) / len(averages)
    highest = max(averages)
    lowest = min(averages)
    total_students = len(students)
    class_median = median(students)

    # It will now count how many people failed and how many people passed
    # Setting the number to 0, as the function hasn't counted who's failing and who's not yet
    passing_count = 0
    failing_count = 0
    for avg in averages:
        if avg >= 50:
            passing_count += 1
        else:
            failing_count += 1

    stats = [class_average, highest, lowest, total_students, passing_count, failing_count, class_median]
    return stats

def performance(average):
    """
    This function categorizes student performance based on average grade using lists and for loop.
   
    Args:
        A student's average grade = average (float)
   
    Returns:
        Performance category = (str)
    """
    # Defining two different lists here, "thresholds" and "categories"
    thresholds = [90, 85, 80, 75, 70, 65, 60, 55, 50, 0]
    categories = ["Outstanding (A+)", "Excellent (A)", "Very Good (A-)", "Good (B+)", "Average (B)",
                  "Approaching Average (B-)", "Below Average (C+)", "Needs Improvement (C)",
                  "Barely Passing (C-)", "Failing (F)"]
   
    # Finding the correct category by checking the thresholds
    for i in range(len(thresholds)):
        if average >= thresholds[i]:
            return categories[i]
    return "Oh no, invalid grade!"

def median(students):
    """
    This function calculates the median of all student averages.
    
    Args:
        List of student data lists = students (list)
    
    Returns:
        Median average grade = class_median (float)
    """
    # If the function cannot find the students list
    if not students:
        return 0
    
    averages = []
    for student in students:
        average = student[2]
        averages.append(average)
    
    # Sorting the averages
    sorted_averages = sorted(averages)
    
    # Calculating median now
    n = len(sorted_averages)
    if n % 2 == 0:
        # If even
        middle1 = sorted_averages[n // 2 - 1]
        middle2 = sorted_averages[n // 2]
        class_median = (middle1 + middle2) / 2
    else:
        # If odd
        class_median = sorted_averages[n // 2]
    return class_median

def top_bottom_students(students):
    """
    This function shows us the top 3 and bottom 3 performing students.
    
    Args:
        Sorted list of student data lists = students (list)
    
    Returns:
        Lists containing top 3 and bottom 3 students = [top_3, bottom_3] (list)
    """
    # If there is no student data
    if not students:
        return [[], []]
    
    # Getting top 3 students
    top_3 = []
    for i in range(min(3, len(students))):
        top_3.append(students[i])
    
    # Getting bottom 3 students and reversing the list to show worst performer first!
    bottom_3 = []
    start_index = max(0, len(students) - 3)
    for i in range(start_index, len(students)):
        bottom_3.append(students[i])
    bottom_3.reverse()

    return [top_3, bottom_3]

def report_writer(students, stats, output_filename):
    """
    This function writes a detailed report and saves it to a file.
   
    Args:
        Sorted list of student data lists = students (list)
        Class statistics list = stats (list)
        Name of output file = output_filename (str)
   
    Returns:
        None
    """
    # Getting top and bottom 3 students
    top_to_bottom = top_bottom_students(students)
    top_3 = top_to_bottom[0]
    bottom_3 = top_to_bottom[1]

    # Printing every single information in a line using a list, much more convenient than using print()
    report_lines = []

    # Header for the report
    report_lines.append("=" * 30)
    report_lines.append(" STUDENT GRADE TRACKER REPORT")
    report_lines.append("=" * 30)
    report_lines.append("")

    # Statistics for the entire class
    report_lines.append("CLASS STATISTICS:")
    report_lines.append("-" * 31)
    report_lines.append("Total Students: " + str(stats[3]))
    report_lines.append("Class Average: " + str(round(stats[0], 2)) + "%")
    report_lines.append("Class Median: " + str(round(stats[6], 2)) + "%")
    report_lines.append("Highest Average: " + str(round(stats[1], 2)) + "%")
    report_lines.append("Lowest Average: " + str(round(stats[2], 2)) + "%")
    report_lines.append("Passing Students (>=50%): " + str(stats[4]))
    report_lines.append("Failing Students (<50%): " + str(stats[5]))
    report_lines.append("")

    # Top 3 and Bottom 3 Students
    report_lines.append("TOP 3 AND BOTTOM 3 STUDENTS:")
    report_lines.append("-" * 50)
    
    # Top 3
    report_lines.append("Top 3 students:")
    if top_3:
        for i in range(len(top_3)):
            student = top_3[i]
            name = student[0]
            average = student[2]
            rank_str = str(i + 1) + ". "
            line = rank_str + name + " - " + str(round(average, 2)) + "%"
            report_lines.append(line)
    else:
        report_lines.append("No students found.")
    report_lines.append("")
    
    # Bottom 3
    report_lines.append("Bottom 3 students:")
    if bottom_3:
        for i in range(len(bottom_3)):
            student = bottom_3[i]
            name = student[0]
            average = student[2]
            rank_str = str(i + 1) + ". "
            line = rank_str + name + " - " + str(round(average, 2)) + "%"
            report_lines.append(line)
    else:
        report_lines.append("No students found.")
    report_lines.append("")
    
    # Details for each and every student, essentially creating a sort of table here with proper symmetry
    report_lines.append("INDIVIDUAL STUDENT DETAILS:")
    report_lines.append("-" * 64)
    report_lines.append(("Name" + " " * (31 - len(name))) + "Marks                    Average   Category")
    report_lines.append("-" * 64)

    # Listing their name, marks, average, and what category they ended up in
    for student in students:
        name = student[0]
        marks = student[1]
        average = student[2]
        category = performance(average)

    # It will now make a marks list
        marks_list = []
        for mark in marks:
            marks_list.append(str(round(mark, 1)))
        marks_str = ", ".join(marks_list)

    # Formatting the line with constant spacing
        name_part = name + " " * (20 - len(name))
        marks_part = marks_str + " | "
        avg_part = str(round(average, 2)) + "%" + " " * (10 - len(str(round(average, 2)) + "%"))
        line = name_part + marks_part + avg_part + category
        report_lines.append(line)
    report_lines.append("")

    # Rankings for students with suitable spacing from each other
    report_lines.append("STUDENT RANKINGS (From Highest to Lowest):")
    report_lines.append("-" * 50)
    report_lines.append("Rank  Name                     Average")
    report_lines.append("-" * 50)

    for rank in range(len(students)):
        student = students[rank]
        name = student[0]
        average = student[2]
       
        rank_str = str(rank + 1)
        rank_part = rank_str + " " * (6 - len(rank_str))
        name_part = name + " " * (25 - len(name))
        avg_str = str(round(average, 2)) + "%"
       
        line = rank_part + name_part + avg_str
        report_lines.append(line)

    # Distribution of students' performance
    report_lines.append("")
    report_lines.append("PERFORMANCE DISTRIBUTION:")
    report_lines.append("-" * 40)

    # Counting students in each category using lists
    category_names = []
    category_counts = []
   
    for student in students:
        category = performance(student[2])

        # Checking if category already exists in our lists
        found_index = -1
        for i in range(len(category_names)):
            if category_names[i] == category:
                found_index = i
                break
       
        if found_index >= 0:
            category_counts[found_index] += 1
        else:
            category_names.append(category)
            category_counts.append(1)

    # Displaying the distribution
    for i in range(len(category_names)):
        count = category_counts[i]
        if students:
            percentage = (count / len(students)) * 100
        else:
            percentage = 0
        line = category_names[i] + ": " + str(count) + " students (" + str(round(percentage, 1)) + "%)"
        report_lines.append(line)

    # Writing to file and printing to the terminal
    with open(output_filename, 'w') as file:
        for line in report_lines:
            file.write(line + '\n')
            print(line)

def bubble_sort(students):
    """
    This function sorts the list of students in descending order of their average using bubble sort.
    
    Args:
        List of student data lists [name, marks, average] = students (list)
    
    Returns:
        Sorted list of students, from highest average to lowest = students (list)
    """
    for i in range(len(students)):
        for j in range(0, len(students) - i - 1):
            if students[j][2] < students[j + 1][2]:
                students[j], students[j + 1] = students[j + 1], students[j]
    return students

def main():
    """
    The function that brings the entire program to life!

    Args:
        None

    Returns:
        None
    """
    print("Welcome to the Student Grade Tracker Program!")
    print("This is our expected file format: Name = mark1, mark2, mark3, and so on...\n")
   
    time.sleep(1)
    # Getting the input filename, and if they don't write ".txt"
    input_filename = input(">>> Enter the input filename (for example, 'grades.txt'): ").strip()
    if not input_filename.lower().endswith(".txt"):
        input_filename += ".txt"

    # Read student marks
    print("\n>>> Reading marks from " + input_filename)
    students = reading_data(input_filename)
   
    if not students:
        print(">>> Oh no! We couldn't find any valid student marks in the file. :(")
        print(">>> Please check the file format: Name = mark1, mark2, mark3, and so on...")
   
    time.sleep(1)
    print("\n>>> Successfully loaded " + str(len(students)) + " students and their marks!")
   
    # It will now sort students by average (highest to lowest) using bubble sort (something that hasn't been covered in the Grade 11 review)
    students = bubble_sort(students)
   
    # Calculating statistics now
    stats = statistics(students)
   
    time.sleep(1)
    # Generating and saving the report as a .txt file
    output_filename = input("\n>>> Before we continue, what would you like to call your file as? (do not write .txt): ").strip(" ")
   
    # Even if they do write ".txt" despite advising them not to
    if not output_filename.lower().endswith(".txt"):
        output_filename += ".txt"

    time.sleep(1)
    print("\n>>> Done! Creating a report now...\n")
    time.sleep(2)
    report_writer(students, stats, output_filename)
   
    # Asking the user to name their output filename
    time.sleep(1)
    print("\n>>> We have saved your report as '" + output_filename + "'.")
    time.sleep(1)
    print(">>> Program completed successfully! Thank you for using the program! :)")

# Finally, running the program and bringing it to life!
if __name__ == "__main__":
    main()