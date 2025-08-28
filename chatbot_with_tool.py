import os
import re
from dotenv import load_dotenv
import google.generativeai as genai
from datetime import datetime
from calculator_tool import calculate

# Load environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file!")

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

# Predefined prompts for non-math queries
PREDEFINED_PROMPTS = {
    "what is the capital of france": "What is the capital of France?",
    "what is the capital of japan": "What is the capital of Japan?"
}

LOG_FILE = "logs_with_tool.txt"

def log_interaction(user_input, bot_reply):
    """Log chat interactions with timestamps."""
    with open(LOG_FILE, "a") as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] You: {user_input}\n")
        f.write(f"[{timestamp}] Bot: {bot_reply}\n\n")

def is_math_question(user_input):
    """
    Detect math questions (natural language or operators).
    Returns:
    - True → math only
    - False → non-math
    - "multi_step" → combined math + non-math (not yet supported)
    """
    user_input_lower = user_input.lower()
    math_keywords = ["add", "plus", "sum", "subtract", "minus", "multiply", "times",
                     "divide", "by", "difference of"]

    # Split input by common separators
    parts = re.split(r',|;|\band\b|\balso\b', user_input_lower)

    math_count = sum(1 for part in parts if any(word in part for word in math_keywords)
                     or bool(re.search(r"\d+\s*[\+\-\*/]\s*\d+", part)))
    non_math_count = sum(1 for part in parts if any(c.isalpha() for c in part)
                         and not any(word in part for word in math_keywords))

    if math_count > 0 and non_math_count > 0:
        return "multi_step"  # Combined math + non-math detected

    return math_count > 0

def ask_llm(prompt):
    """Generate response from Gemini LLM with error handling."""
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error: {e}"

def chatbot():
    print("🤖 Smart Assistant with Calculator Tool. Type 'exit' to quit.\n")
    
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        math_check = is_math_question(user_input)
        
        if math_check == "multi_step":
            bot_reply = "Graceful failure (no multi-step yet)."
        
        elif math_check:
            bot_reply = calculate(user_input)
        
        elif user_input.lower() in PREDEFINED_PROMPTS:
            bot_reply = ask_llm(PREDEFINED_PROMPTS[user_input.lower()])
        
        else:
            bot_reply = ask_llm(f"Answer this question clearly: {user_input}")

        print("Bot:", bot_reply, "\n")
        log_interaction(user_input, bot_reply)

if __name__ == "__main__":
    chatbot()