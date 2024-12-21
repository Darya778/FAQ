import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
from tkinter import *
from tkinter import ttk
import json

with open("faq_data.json", "r", encoding="utf-8") as file:
    faq_data = json.load(file)

questions = [item["question"] for item in faq_data]
answers = [item["answer"] for item in faq_data]

tf.get_logger().setLevel('ERROR')

bert_url = "https://tfhub.dev/tensorflow/bert_multi_cased_L-12_H-768_A-12/3"
bpre_url = "https://tfhub.dev/tensorflow/bert_multi_cased_preprocess/3"

print("Loading BERT...")
bert_preprocess_model = hub.KerasLayer(bpre_url)
bert_model = hub.KerasLayer(bert_url)
loaded_model = tf.keras.models.load_model("model1.keras")
dataset = np.load("dataset1.npy")


def show_message():
    question = entry.get().strip().lower()
    if not question:
        label["text"] = "Введите вопрос!"
        return
    
    emb1 = bert_model(bert_preprocess_model([question]))["pooled_output"].numpy()[0]
    p = []
    for i in range(dataset.shape[0]):
        emb2 = dataset[i, 1]
        emb3 = np.concatenate([emb1, emb2])
        p.append(emb3)
    p = np.array(p)
    
    predicted_index = loaded_model.predict(p).argmax()
    label["text"] = answers.get(predicted_index, "Ответ не найден")


root = Tk()
root.title("Чат-бот")
root.geometry("500x400")

entry = ttk.Entry(root, width=50)
entry.pack(pady=10)

btn = ttk.Button(root, text="Задать вопрос", command=show_message)
btn.pack(pady=10)

label = ttk.Label(root, text="Задайте вопрос", wraplength=400, justify="center")
label.pack(pady=10)

root.mainloop()
