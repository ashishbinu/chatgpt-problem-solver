import sys

from revChatGPT.V1 import Chatbot, configure


def main():
    chatbot = Chatbot(configure())
    problem = input("Explain your problem here\n").strip()
    conversation_id = None

    if not problem:
        print("Problem is empty", file=sys.stderr)
        return

    # prompt1
    three_ideas = ""
    with open("prompts/prompt1") as f:
        prompt1 = f.read().replace("PROBLEM", problem)
        try:
            for data in chatbot.ask(prompt1):
                three_ideas = data["message"]
                if conversation_id is None:
                    conversation_id = data["conversation_id"]
        except Exception as e:
            print("Error:", e, file=sys.stderr)
        finally:
            print("THREE IDEAS : ", three_ideas)

    evaluated_three_ideas = ""
    with open("prompts/prompt2") as f:
        prompt2 = f.read().replace("3IDEAS", three_ideas)
        try:
            for data in chatbot.ask(prompt2, conversation_id=conversation_id):
                evaluated_three_ideas = data["message"]
        except Exception as e:
            print("Error:", e, file=sys.stderr)
        finally:
            print("EVALUATED THREE IDEAS : ", evaluated_three_ideas)

    winning_idea = ""
    with open("prompts/prompt3") as f:
        prompt3 = f.read().replace("WINNINGIDEA", evaluated_three_ideas)
        try:
            for data in chatbot.ask(prompt3, conversation_id=conversation_id):
                winning_idea = data["message"]
        except Exception as e:
            print("Error:", e, file=sys.stderr)
        finally:
            print("WINNING IDEA : ", winning_idea)

    for _ in range(5):
        new_ideas = ""
        with open("prompts/prompt4") as f:
            prompt4 = (
                f.read().replace("WINNING2", winning_idea).replace("PROBLEM", problem)
            )
            try:
                for data in chatbot.ask(prompt4, conversation_id=conversation_id):
                    new_ideas = data["message"]
            except Exception as e:
                print("Error:", e, file=sys.stderr)
            finally:
                print("NEW IDEAS : ", new_ideas)

        evaluated_new_ideas = ""
        with open("prompts/prompt5") as f:
            prompt4 = f.read().replace("WLOOP", winning_idea)
            try:
                for data in chatbot.ask(prompt4, conversation_id=conversation_id):
                    evaluated_new_ideas = data["message"]
            except Exception as e:
                print("Error:", e, file=sys.stderr)
            finally:
                print("EVALUATED NEW IDEAS : ", evaluated_new_ideas)

        with open("prompts/prompt3") as f:
            prompt3 = f.read().replace("WINNINGIDEA", evaluated_new_ideas)
            try:
                for data in chatbot.ask(prompt3, conversation_id=conversation_id):
                    winning_idea = data["message"]
            except Exception as e:
                print("Error:", e, file=sys.stderr)
            finally:
                print("SUB WINNING IDEA : ", winning_idea)

    evaluated_winner_idea = ""
    with open("prompts/prompt6") as f:
        prompt6 = f.read().replace("WINNER", winning_idea)
        try:
            for data in chatbot.ask(prompt6, conversation_id=conversation_id):
                evaluated_winner_idea = data["message"]
        except Exception as e:
            print("Error:", e, file=sys.stderr)
        finally:
            print("WINNER IDEA : ", evaluated_winner_idea)

    solution = ""
    with open("prompts/prompt7") as f:
        prompt7 = f.read().replace("WINNER2", evaluated_winner_idea)
        try:
            for data in chatbot.ask(prompt7, conversation_id=conversation_id):
                solution = data["message"]
        except Exception as e:
            print("Error:", e, file=sys.stderr)
        finally:
            print("FINISHED WINNER IDEA : ", solution)


if __name__ == "__main__":
    main()
