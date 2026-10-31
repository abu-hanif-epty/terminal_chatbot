
# from chatbot import stream_response
# from config import GROQ_MODEL
# from utils import save_conversation,load_conversation
# import json


# def main():
#     print("\n===== TERMINAL AI CHATBOT =====")
#     print(f"Model: {GROQ_MODEL}")
#     print("Type /help for commands.\n")

#     messages = []

#     while True:
#         try:
#             user_input = input("You: ").strip()

#             if not user_input:
#                 continue

#             # Exit command
#             if user_input == "/exit":
#                 print("Chatbot: Goodbye!")
#                 break

#             # Help command
#             elif user_input == "/help":
#                 print("\nAvailable Commands:")
#                 print("/help  - Show available commands")
#                 print("/clear - Clear conversation history")
#                 print("/model - Show current model")
#                 print("/save -save conversation")
#                 print("/laod -Load save conversation")
#                 print("/exit  - Exit chatbot\n")
#                 continue

#             # Clear command
#             elif user_input == "/clear":
#                 messages.clear()
#                 print("Chatbot: Conversation cleared.\n")
#                 continue

#             # Model command
#             elif user_input == "/model":
#                 print(f"Current model: {GROQ_MODEL}\n")
#                 continue
#             elif user_input == "/save":
#                 if not messages:
#                     print("No conversation to save ")
#                     continue
#                 save_conversation(messages)
#                 print("chatbot conversation saved ")

#             elif user_input == "/load":
#                 try :
#                     save_messages = load_conversation()

#                     if save_messages is None:
#                         print("NO saved conversation found")
#                     else:
#                         messages = save_messages
#                         print("Chatbot : Conversation loaded ")

#                 except (json.JSONDecodeError,OSError) as e:
#                     print(f"Unable to load conversation:{e}")
#             # Send user message
#             messages.append({
#                 "role": "user",
#                 "content": user_input
#             })

#             answer = stream_response(messages)

#             # Handle API errors
#             if answer is None:

#                 print("ERROR: Unable to generate response")
#                 messages.pop()
#                 continue

#             messages.append({
#                 "role": "assistant",
#                 "content": answer
#             })

#             print(f"\nAI: {answer}")

#         except KeyboardInterrupt:
#             print("\nChatbot: Goodbye!")
#             break

#         except Exception as e:
#             print(f"\nUnexpected error: {e}")


# if __name__ == "__main__":
#     main()

from chatbot import stream_response
from config import GROQ_MODEL
from utils import save_conversation, load_conversation
import json


def main():
    print("\n===== TERMINAL AI CHATBOT =====")
    print(f"Model: {GROQ_MODEL}")
    print("Type /help for commands.\n")

    messages = []

    while True:
        try:
            user_input = input("You: ").strip()

            if not user_input:
                continue

            # Exit command
            if user_input == "/exit":
                print("Chatbot: Goodbye!")
                break

            # Help command
            elif user_input == "/help":
                print("\nAvailable Commands:")
                print("/help  - Show available commands")
                print("/clear - Clear conversation history")
                print("/model - Show current model")
                print("/save  - Save conversation")
                print("/load  - Load saved conversation")
                print("/exit  - Exit chatbot\n")
                continue

            # Clear command
            elif user_input == "/clear":
                messages.clear()
                print("Chatbot: Conversation cleared.\n")
                continue

            # Model command
            elif user_input == "/model":
                print(f"Current model: {GROQ_MODEL}\n")
                continue

            # Save command
            elif user_input == "/save":
                if not messages:
                    print("Chatbot: No conversation to save.\n")
                    continue
                try:
                    save_conversation(messages)
                    print("Chatbot: Conversation saved successfully.\n")
                except Exception as e:
                    print(f"Chatbot: Failed to save conversation: {e}\n")
                continue

            # Load command
            elif user_input == "/load":
                try:
                    saved_messages = load_conversation()

                    if not saved_messages:
                        print("Chatbot: No saved conversation found.\n")
                    else:
                        messages = saved_messages
                        print("Chatbot: Conversation loaded successfully.\n")

                except (json.JSONDecodeError, OSError) as e:
                    print(f"Chatbot: Unable to load conversation: {e}\n")
                continue

            # --- Regular Chat Flow ---
            messages.append({
                "role": "user",
                "content": user_input
            })

            answer = stream_response(messages)

            # Handle API errors
            if answer is None:
                print("ERROR: Unable to generate response\n")
                messages.pop()
                continue

            messages.append({
                "role": "assistant",
                "content": answer
            })
        except KeyboardInterrupt:
            print("\nChatbot: Goodbye!")
            break

        except Exception as e:
            print(f"\nUnexpected error: {e}\n")


if __name__ == "__main__":
    main()