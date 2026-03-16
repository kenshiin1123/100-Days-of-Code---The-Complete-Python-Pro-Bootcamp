import random ; import time

student_scores = []

for i in range(0,20):
    student_scores.append(random.randint(50,10000))

max_score = 0
for i, student_score in enumerate(student_scores):
    if student_score > max_score: max_score = student_score
    print(f"[{i + 1}]: Student Score: {student_score}")
    time.sleep(0.1)

print(f"\n\nHighest Student Score {max_score}")