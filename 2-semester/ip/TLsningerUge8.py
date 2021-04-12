#Exercise 13.1 (sum of two integers)

while True:
    try:
        x, y = input("Input two integers, separated by space: ").split(" ")
        print(f'Sum = {int(x) + int(y)}')
    except Exception:  # Exception to allow keyboard interrupt
        print("invalid input")
        continue
    break

# Exercise 13.2 (transposing)
import os.path

while True:
    in_filename = input("File to transpose: ")
    out_filename = input("Output file transpose: ")
    try:
        in_file = open(in_filename)
    except:
        print("Cannot open ", in_filename)
        continue
    try:
        lines = []
        for line in in_file:
            lines.append(line[:-1].split(";"))
    finally: # uanset om noget går galt eller ej, så husker vi at lukke filen igen
        in_file.close()

    columns = [len(line) for line in lines]

    if min(columns) != max(columns):
        print("Rows in file do not contain same number of columns")
        break
    if os.path.isfile(out_filename):
        print("File %s already exist" % out_filename)
        overwrite = input("overwrite existing file ('yes' will overwrite): ")
        if overwrite.lower() != 'yes':
            continue
    try:
        out_file = open(out_filename, "w")
    except Exception:
        print("Failed to open output file", out_filename)
        continue
    try:
        for col in range(columns[0]):
            values = [lines[row][col] for row in range(len(lines))]
            txt = ";".join(values) + '\n'
            out_file.write(txt)
        print("done writting to", out_filename)
        break
    finally:
        out_file.close()

#Exercise 13.3 (grade statistics)
student_filename = "grades.students" #input("file with student list: ")
exam_filename = "grades.exams" #input("file with exam results: ")
student_file = open(student_filename)

names = {}
for line in student_file:
    student_id, name, address = line[:-1].split(';')
    names[student_id] = name
student_file.close()

courses = {}
grade_sum = {}

for student_id in names:
    courses[student_id] = 0
    grade_sum[student_id] = 0

exam_results = open(exam_filename)
for line in exam_results:
    student_id, course, grade = line[:-1].split(';')
    courses[student_id] += 1
    grade_sum[student_id] += int(grade)
exam_results.close()

name_width = max([len(name) for name in names.values()])

fmt = "%-10s %-" + str(name_width) + "s %8s %8s"
header = fmt % ("Student id", "Name", "Average", "#Courses")
print(header)
print('=' * len(header))
for student_id, name in sorted(names.items()):
    cnt = courses[student_id]
    average = grade_sum[student_id] / cnt if cnt else 0
    print(fmt % (student_id, name, "%5.2f" % average, cnt))


# Exercise 13.4 (subset sum)
def subset_sum(x, L):
    class SolutionFound(Exception):
        pass

    def solve(x, L):
        """Try to find a subset L' of a list L with sum x.
        solution are already selected elements
        (and removed from L and subtracted from x)"""

        if x == 0:
            raise SolutionFound

        if L:
            solve(x, L[1:])
            solution.append(L[0])
            solve(x - L[0], L[1:])
            solution.pop()

    solution = []

    try:
        solve(x, L)
    except SolutionFound:
        return solution
    else:
        return None


print(subset_sum(8, [2, 3, 8, 11, -1]))

print(subset_sum(6, [2, 3, 8, 11, -1]))

