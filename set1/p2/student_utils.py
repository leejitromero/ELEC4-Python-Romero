# Full Name: Jit Lee S. Romero
# Section: IV-BSIT C
# Activity: P2 - Custom Module: student_utils
# Date: November 16, 2026


PASSING_AVERAGE = 75


# These functions return results so another program can decide how to display them.
def compute_average(grades):
    return sum(grades) / len(grades)


def determine_status(grades):
    average = compute_average(grades)
    if average >= PASSING_AVERAGE:
        return "PASS"
    else:
        return "FAIL"


def get_highest_grade(grades):
    return max(grades)


def get_lowest_grade(grades):
    return min(grades)
