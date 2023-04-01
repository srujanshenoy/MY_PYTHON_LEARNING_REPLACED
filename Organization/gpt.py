import os
import openai
openai.organization = "org-dbTAYmDzpKNWvuR5dgfi6mfL"
openai.api_key = "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"

def generate_response(prompt):
    completions = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = prompt,
        max_tokens = 1024,
        n = 1,
        stop = None,
        temperature = 0.5
    )

    message = completions.choices[0].text
    return message.strip()

while True:
    prompt = input(">>>")
    print(generate_response(prompt))



