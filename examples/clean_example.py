"""Student grade program (CLEAN version: does the same job, no smells)."""

PASSING_AVERAGE = 60
GRADE_THRESHOLDS = [(90, "A"), (80, "B"), (70, "C"), (PASSING_AVERAGE, "D")]
FAILING_GRADE = "F"
PASS_STATUS = "PASS"
FAIL_STATUS = "FAIL"


def calculate_average(scores):
    return sum(scores) / len(scores)


def determine_letter_grade(average):
    for minimum_average, letter_grade in GRADE_THRESHOLDS:
        if average >= minimum_average:
            return letter_grade
    return FAILING_GRADE


def determine_pass_status(average):
    if average >= PASSING_AVERAGE:
        return PASS_STATUS
    return FAIL_STATUS


def format_student_result(student_name, scores):
    average = calculate_average(scores)
    letter_grade = determine_letter_grade(average)
    pass_status = determine_pass_status(average)
    return f"{student_name}: {average:.1f} {letter_grade} {pass_status}"


def main():
    print(format_student_result("Memo", [90, 85, 78]))


if __name__ == "__main__":
    main()
