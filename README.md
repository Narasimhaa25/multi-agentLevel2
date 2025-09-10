Multi-Agent Level 2
Level 2  LLM + Basic Tool Use (One Tool Integration)

This project is the second level of a multi-stage AI assignment. At this level, we extend the LLM-only chatbot from Level 1 by integrating a basic calculator tool.

The focus here is on tool usage:
	•	The LLM detects when a math query is asked.
	•	Instead of solving it itself, the LLM delegates the task to a calculator tool.
	•	Non-math queries are still answered directly by the LLM.
	•	Multi-step tool + LLM queries are not supported yet (handled in Level 3).
⸻

⚙️ Setup and Installation
	1.	Ensure you have Python 3.9 or higher installed.

  	
   2.	Clone this repository and navigate to the level1 directory.
	
 3.	Install the required dependencies:
            pip install -r ../requirements.txt
            
   		 The requirements.txt file includes:
                    •	google-generativeai
                    •	python-dotenv
   4.	Create a .env file in the same directory with your Gemini API key:

     		GEMINI_API_KEY=your_api_key_here
5.	Run the chatbot:

  			 python chatbot_with_tool.py



💬 Example Interactions

   ✅ Example 1 —Math with tool
        You: What is 12 times 7?
        Bot: 
            Result: 84


 ✅ Example 2 — Math with tool     

        You:  Add 45 and 30   
        Bot: 
              Result: 75 

✅ Example 3 — Normal LLM response:

         You: What is the capital of France?
         Bot: 
                Paris
✅ Example 4 — Mixed query (not supported yet):      
        	
		  You:  Multiply 9 and 8, and also tell me the capital of Japan
         Bot:
               Graceful failure (no multi-step yet). 


