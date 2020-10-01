# GRADE CALCULATOR --

def main():
  # USER INPUT: NAME --
  student_name = input("Enter your Full Name: ")

  def mark_grade():
    # USER INPUT: PREDICTED GRADE % --
    predicted_grade = input("Enter your predicted grade (%) (numbers only): ")

    # IS INPUT AN INTEGER? --
    try:
      predicted_grade = int(predicted_grade)
    except ValueError:
      print("Incorrect Value. Please enter your precentages in numbers only.")
      mark_grade()

    # USER INPUT: GRADE % ACHIEVED --
    grade_percentage = input("Enter your awarded grade (%) (numbers only): ")

    # IS INPUT AN INTEGER? --
    try:
      grade_percentage = int(grade_percentage)
    except ValueError:
      print("Incorrect Value. Please enter your precentages in numbers only.")
      mark_grade()

    # GRADE CALCULATOR --
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
      print("FINAL RESULT: B (50%-69%)")
    if 70 <= grade_percentage <= 84:
      print(f"NAME: {student_name}")
      print(f"PREDICTED GRADE: {predicted_grade}%") 
      print("FINAL RESULT: A (60%-84%)")
    if grade_percentage >= 85:
      print(f"NAME: {student_name}")
      print(f"PREDICTED GRADE: {predicted_grade}%") 
      print("FINAL RESULT: A* (85%-100%)")
    # END GRADE CALCULATOR --

    # MEET PREDICTED GRADE? --
    if grade_percentage < predicted_grade:
      print("Unfortunately, you did not meet your predicted grade.")
    if grade_percentage == predicted_grade:
      print("You achieved your Predicted Grade.")
    if grade_percentage > predicted_grade:
      print("You did better than expected and achieved above your predicted grade percentage!")

  mark_grade()
main()

