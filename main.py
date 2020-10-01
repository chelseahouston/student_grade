# GRADE CALCULATOR --

def main():
  # USER INPUT: NAME --
  student_name = input("Enter your Full Name: ")

  def mark_grade():
    # USER INPUT: TARGET GRADE % --
    target_grade = input("Enter your target grade (%) (numbers only): ")

    # IS INPUT AN INTEGER? --
    try:
      target_grade = int(target_grade)
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
      print(f"TARGET GRADE: {target_grade}%") 
      print("FINAL RESULT: FAIL (0%-29%)")
    if 31 <= grade_percentage <= 49:
      print(f"NAME: {student_name}")
      print(f"TARGET GRADE: {target_grade}%") 
      print("FINAL RESULT: C (30%-49%)")
    if 50 <= grade_percentage <= 69:
      print(f"NAME: {student_name}")
      print(f"TARGET GRADE: {target_grade}%") 
      print("FINAL RESULT: B (50%-69%)")
    if 70 <= grade_percentage <= 84:
      print(f"NAME: {student_name}")
      print(f"TARGET GRADE: {target_grade}%") 
      print("FINAL RESULT: A (60%-84%)")
    if grade_percentage >= 85:
      print(f"NAME: {student_name}")
      print(f"TARGET GRADE: {target_grade}%") 
      print("FINAL RESULT: A* (85%-100%)")
    # END GRADE CALCULATOR --

    # MEET TARGET GRADE? --
    if grade_percentage < target_grade:
      print("Unfortunately, you did not meet your target grade.")
    if grade_percentage == target_grade:
      print("You achieved your target grade.")
    if grade_percentage > target_grade:
      print("You did better than expected and achieved above your target grade percentage!")

  mark_grade()
main()

