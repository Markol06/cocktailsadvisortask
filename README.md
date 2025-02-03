# 🍹 Cocktail Advisor Chatbot

This is an AI-powered chatbot that provides cocktail recommendations based on user preferences. The chatbot integrates **Llama 2**, **FAISS** for vector search, and stores user preferences for better recommendations.

## 🚀 Features
- **Chatbot Interface**: Users can ask about cocktails and receive personalized recommendations.
- **LLM Integration**: Uses `Llama 2` for answering queries.
- **Vector Search**: Utilizes FAISS for finding similar cocktails.
- **User Preferences**: Saves user likes, dislikes, and allergies.

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Markol06/cocktailsadvisortask.git
   cd cocktailsadvisortask
2. Install dependencies
pip install -r requirements.txt
3. Download the dataset and model
Place final_cocktails.csv in data/
Download llama-2-7b-chat.Q4_K_M.gguf and place it in models/
4. Run the chatbot
python src/chatbot.py
