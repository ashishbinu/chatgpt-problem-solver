import os
import sys
from typing import Tuple

from dotenv import load_dotenv
from revChatGPT.V1 import Chatbot
from tqdm import tqdm


def chatgpt_answer_to_prompt_file(
    chatbot_instance: Chatbot,
    prompt_file: str,
    to_be_replaced_word: str,
    string: str,
    conversation_id: str | None = None,
) -> Tuple[str, str]:
    answer = ""
    convo_id = conversation_id or ""
    with open(prompt_file) as f:
        prompt = f.read().replace(to_be_replaced_word, string)
        try:
            for data in chatbot_instance.ask(
                prompt, conversation_id=conversation_id, auto_continue=True
            ):
                answer = data["message"]
                if not convo_id:
                    convo_id = data["conversation_id"]
        except Exception as e:
            print("Error: ", e, file=sys.stderr)
        finally:
            return answer, convo_id


def main():
    load_dotenv()
    access_token = os.environ.get("OPENAI_ACCESS_TOKEN")
    if not access_token:
        print("Error: OPENAI_ACCESS_TOKEN not set", file=sys.stderr)
        sys.exit(1)

    chatbot = Chatbot(config={"access_token": access_token})
    problem = input("Explain your problem here\n").strip()
    conversation_id = None
    iterations = 2
    total_work_units = 5 + iterations * 3
    progress_bar = tqdm(
        total=total_work_units, desc="Processing", ncols=100, ascii=True
    )

    if not problem:
        print("Problem is empty", file=sys.stderr)
        return

    # prompt1
    three_ideas, conversation_id = chatgpt_answer_to_prompt_file(
        chatbot, "prompts/prompt1", "PROBLEM", problem
    )
    progress_bar.update(1)

    evaluated_three_ideas, _ = chatgpt_answer_to_prompt_file(
        chatbot, "prompts/prompt2", "3IDEAS", three_ideas, conversation_id
    )
    progress_bar.update(1)

    winning_idea, _ = chatgpt_answer_to_prompt_file(
        chatbot,
        "prompts/prompt3",
        "WINNINGIDEA",
        evaluated_three_ideas,
        conversation_id,
    )
    progress_bar.update(1)

    for _ in range(iterations):
        new_ideas = ""
        with open("prompts/prompt4") as f:
            prompt4 = (
                f.read().replace("WINNING2", winning_idea).replace("PROBLEM", problem)
            )
            try:
                for data in chatbot.ask(
                    prompt4, conversation_id=conversation_id, auto_continue=True
                ):
                    new_ideas = data["message"]
            except Exception as e:
                print("Error:", e, file=sys.stderr)
            finally:
                pass
                # print("NEW IDEAS : ", new_ideas)
        progress_bar.update(1)

        evaluated_new_ideas, _ = chatgpt_answer_to_prompt_file(
            chatbot,
            "prompts/prompt5",
            "WLOOP",
            new_ideas,
            conversation_id,
        )
        progress_bar.update(1)

        winning_idea, _ = chatgpt_answer_to_prompt_file(
            chatbot,
            "prompts/prompt3",
            "WINNINGIDEA",
            evaluated_new_ideas,
            conversation_id,
        )
        progress_bar.update(1)

    evaluated_winner_idea, _ = chatgpt_answer_to_prompt_file(
        chatbot,
        "prompts/prompt6",
        "WINNER",
        winning_idea,
        conversation_id,
    )
    progress_bar.update(1)

    solution, _ = chatgpt_answer_to_prompt_file(
        chatbot, "prompts/prompt7", "WINNER2", evaluated_winner_idea, conversation_id
    )
    progress_bar.update(1)

    print()
    print(solution)

    chatbot.delete_conversation(conversation_id)


if __name__ == "__main__":
    main()
