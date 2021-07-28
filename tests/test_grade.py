def test_add_grade(grade_manager):
    new_grade = grade_manager.add_grades("Class 2")
    assert new_grade["status"] == 200


# def test_all_grade(grade_manager):
#     new_grade = grade_manager.all_grades()
#     assert type(new_grade["grades"]) == list
