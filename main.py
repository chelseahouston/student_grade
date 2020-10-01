def main():
  student_name = input("Enter your Full Name: ")
  def mark_grade():
    predicted_grade = input("Enter your predicted grade (%) (numbers only): ")
    try:
      predicted_grade = int(predicted_grade)
    except ValueError:
      print("Incorrect Value. Please enter your precentages in numbers only.")
      mark_grade()
    grade_percentage = input("Enter your awarded grade (%) (numbers only): ")
    try:
      grade_percentage = int(grade_percentage)
    except ValueError:
      print("Incorrect Value. Please enter your precentages in numbers only.")
      mark_grade()
    if grade_percentage <= 30:
      print(f"NAME: {student_name}")
      print(f"PREDICTED GRADE: {predicted_grade}%") 
      print("FINAL RESULT: FAIL (0%-29%)")
    if 31 <= grade_percentage <= 49:
      print(f"NAME: {student_name}")
      print(f"PREDICTED GRADE: {predicted_grade}%") 
      print("FINAL RESULT: C (30%-49%)")
    if 50 <= grade_percentage <= 69:
      print(f"NAME: {student_name}")
      print(f"PREDICTED GRADE: {predicted_grade}%") 
      print("FINAL RESULT: B (50%-69%0")
    if 70 <= grade_percentage <= 84:
      print(f"NAME: {student_name}")
      print(f"PREDICTED GRADE: {predicted_grade}%") 
      print("FINAL RESULT: A (60%-84%)")
    if grade_percentage >= 85:
      print(f"NAME: {student_name}")
      print(f"PREDICTED GRADE: {predicted_grade}%") 
      print("FINAL RESULT: A* (85%-100%)")
    if grade_percentage < predicted_grade:
      print("Unfortunately, you did not meet your predicted grade.")
    if grade_percentage == predicted_grade:
      print("You achieved your Predicted Grade.")
    if grade_percentage > predicted_grade:
      print("You did better than expected and achieved above your predicted grade percentage!")
  mark_grade()
main()

