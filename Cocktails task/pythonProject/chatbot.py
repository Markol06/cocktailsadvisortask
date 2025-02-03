import os
from vector_db import load_dataset, create_faiss_index, search_similar_cocktails
from user_preferences import update_user_preferences, user_preferences
from model import load_llama_model, generate_response

# 📌 Шляхи до файлів
dataset_path = "../data/final_cocktails.csv"
model_path = "../models/llama-2-7b-chat.Q4_K_M.gguf"

# 📌 Завантажуємо базу даних
df = load_dataset(dataset_path)
index, _ = create_faiss_index(df)

# 📌 Завантажуємо Llama 2
llm = load_llama_model(model_path)


def chat():
    print("💬 Чат з Llama 2 (введи 'exit' для виходу)")

    while True:
        user_input = input("👤 Ви: ")
        if user_input.lower() in ["exit", "quit"]:
            print("👋 Вихід із чату.")
            break

        detected_likes, detected_dislikes, detected_allergies = update_user_preferences("user1", user_input)
        print(
            f"✅ Оновлені вподобання: Likes: {detected_likes}, Dislikes: {detected_dislikes}, Allergies: {detected_allergies}")

        response = generate_response(llm, user_input)
        print(f"\n🤖 Llama: {response}")


if __name__ == "__main__":
    chat()