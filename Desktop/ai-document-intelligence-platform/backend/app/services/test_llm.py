from app.services.llm_service import ask_llm

context = """
Student Name: Siva Rama Krishna

Mathematics A: 75
Mathematics B: 48

Total Marks: 833
"""

question = "What is the total marks?"

answer = ask_llm(
    context,
    question
)

print(answer)
