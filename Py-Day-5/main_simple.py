from my_experience.administration import simple_file_operations

simple_filename = "F:\\ITI\\Intake 45 Data\\09. Introduction to Python Programming (Python)\\Eng. Josephine Boles\\Day 5\\Lab\\test_file.txt"

simple_file_operations.write_file(
    simple_filename, "Hello world, My name is Yasmine.\n")

simple_file_operations.append_file(
    simple_filename, "I am a System Admin student at ITI.\n")

print("File Content:\n", simple_file_operations.read_file(simple_filename))
