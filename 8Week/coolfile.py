import questions

q = questions.get_random_question()
print q

q = questions.search_questions('deep state')
print q

print questions.get_nouns(q)

questions.make_video()
