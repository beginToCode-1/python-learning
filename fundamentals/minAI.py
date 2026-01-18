#mini AI agent
 
def user_input(prompt):
    return input(prompt)
def process_input(user_text):
    return user_text.lower()
def generate_response(processed_text):
    if "hello" in processed_text:
        return "Hello! How can I assist you today?"
    elif "help" in processed_text:
        return "Sure! What do you need help with?"
    else:
        return "I'm not sure how to respond to that."
def ai_agent():
    user_text = user_input("You: ")
    processed_text = process_input(user_text)
    response = generate_response(processed_text)
    print("AI: " + response)
ai_agent()
 


print("AI agent session ended.")

