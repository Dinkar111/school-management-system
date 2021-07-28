from simple_term_menu import TerminalMenu


# SELECT GRADE
def select_grade(grade_manager):
    grades = grade_manager.show_all_grades()
    if grades["status"] == 404:
        print("\n -------> " + grades["message"] + "\n")
        return None
    else:
        grade_names = [grade.get_grade for grade in grades["grades"]]
        terminal = TerminalMenu(
            grade_names,
            title="""
        Choose Grade:
        """,
        )
        show = terminal.show()
        grade_name = grade_names[show]
        return grade_name
