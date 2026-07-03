from utils.similarity import get_answer

def chat():

    print("=" * 50)
    print("        FAQ CHATBOT")
    print("=" * 50)
    print("Type 'exit' to quit.\n")

    while True:

        user_question = input("You: ")

        if user_question.lower() == "exit":
            print("Bot: Thank you! Goodbye.")
            break

        answer = get_answer(user_question)

        print("Bot:", answer)