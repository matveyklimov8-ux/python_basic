names = ["student_name", "2student", "student2", "student-name", "student name", "total_price", "class", "my_age"]
for name in names:
    valid = name.isidentifier() and not __import__('keyword').iskeyword(name)
    print(f"{name}: {'lubatud' if valid else 'ei ole lubatud'}")
