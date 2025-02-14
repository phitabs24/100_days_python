from data import question_data, question_data2
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
n = 0
for question in question_data2:
    question_bank.append(Question(question['question'], question['correct_answer']))
    # print(f"{n+1}). {question_bank[n].text}: {question_bank[n].answer}")
    # n += 1

quiz = QuizBrain(question_bank)

# is_on = True
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score is: {quiz.score}/{quiz.q_number}")