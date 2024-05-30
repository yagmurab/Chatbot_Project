import gradio as gr
import logging
import google.generativeai as genai

genai.configure(api_key="Your_API_Key")

model = genai.GenerativeModel('gemini-pro')

logging.basicConfig(
    filename='chatbot_logs.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

chat_history = []

def generate(prompt):
    try:
        logging.info(f"Received prompt: {prompt}")
        cevap = model.generate_content(prompt)
        response_text = cevap.text
        logging.info(f"Generated response: {response_text}")

        chat_history.append({"prompt": prompt, "response": response_text})

        with open('chat_history.log', 'a') as f:
            f.write(f"User: {prompt}\nAI: {response_text}\n\n")

        return response_text
    except Exception as e:
        logging.error(f"Error generating response: {e}", exc_info=True)
        return "Bir hata oluştu. Lütfen tekrar deneyin."

title = 'Yapay Zeka Sohbet'
description = 'Gemini'

gr.Interface(
    fn=generate,
    inputs=["text"],
    outputs=["text"],
    title=title,
    description=description,
    theme='fşnlaymacklon/boxy_violet'
).launch(server_port=8000, share=True)
