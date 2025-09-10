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

✅ Example 5 —Normal


			You: Explain more about Paris
			Bot: 
				Paris, officially Paris, is the capital and most populous city of France.  It's a global center for art, fashion, gastronomy, and culture, renowned for its history, architecture, and influence on world affairs.  Here's a breakdown of key aspects:
				
				* **History:**  Paris boasts a history spanning millennia, from a Celtic settlement to a Roman town (Lutetia), a medieval capital, and the center of the French Revolution and subsequent empires.  Its historical landmarks, like the Louvre Museum, Notre Dame Cathedral, and the Arc de Triomphe, reflect this rich past.
				
				* **Architecture:** Paris is famous for its classic Haussmann-era architecture, characterized by wide boulevards, elegant buildings, and a consistent aesthetic.  It also features a diverse range of architectural styles, from medieval gothic to modern and contemporary designs.
				
				* **Culture and Arts:**  Paris is a global hub for art and culture, home to world-class museums like the Louvre (housing the Mona Lisa), the Musée d'Orsay (Impressionist and Post-Impressionist art), and the Centre Pompidou (modern art).  It's also a significant center for theatre, opera, music, and literature.
				
				* **Gastronomy:**  Parisian cuisine is globally renowned, offering everything from Michelin-starred restaurants to charming bistros and vibrant street food scenes.  The city is also known for its bakeries, patisseries, and wine culture.
				
				* **Fashion:**  Paris is a leading global fashion capital, hosting prestigious fashion weeks and housing flagship stores of major designers.  Its influence on trends and style is undeniable.
				
				* **Tourism:** Paris is one of the world's most visited cities, attracting millions of tourists annually.  Iconic landmarks, charming neighborhoods, and a vibrant atmosphere contribute to its appeal.
				
				* **Modern Life:** While steeped in history, Paris is a modern metropolis with a bustling business district, a diverse population, and a vibrant contemporary cultural scene.  Challenges include overcrowding, high cost of living, and managing the influx of tourists.
				
				
				In short, Paris is more than just a city; it's a symbol of romance, elegance, and cultural richness, constantly evolving while retaining its historical charm.
<img width="1680" height="1050" alt="Screenshot 2025-09-10 at 19 11 39" src="https://github.com/user-attachments/assets/d7d66f17-6119-4d6d-ad34-4baf4078be90" />

 
