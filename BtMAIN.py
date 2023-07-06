#BotTalk 

#Created by Adam Brook on May 17 2023


import os
import openai
import gradio as gr


openai.api_key = "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"

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "
prompt = "The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: ",

# openai responses
def openai_new(ques):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt = prompt,
    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=[" Human:", " AI:"]
    )
    return response.choices[0].text

#Human responses
def convo(input, old):
    old = old or []
    su = list(sum(old,()))
    su.append(input)
    inp = ''.join(su)
    out = openai_new(inp)
    old.append((input,out))
    return old, old

blocks = gr.Blocks()

#Textbox functionality

with blocks:
  chatb = gr.Chatbot()
  mess = gr.Textbox(placeholder=prompt)
  state = gr.State()
  submit = gr.Button("Tap")
  submit.click(convo, inputs = [mess,state], outputs = [chatb,state])
  blocks.launch(debug=True)
