if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    score_of_student = student_marks[query_name]
    average_score_of_student = sum(score_of_student)/3
    print(f"{average_score_of_student:.2f}")
