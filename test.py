# import site; print(site.getsitepackages())


from transformers import pipeline
from openai import OpenAI
# IN TERMINAL, or bashrc: export OPENAI_API_KEY='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'
# or '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' or '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'
# or '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' or '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'

# import torch
# print(torch.__version__)
# print("CUDA available: ", torch.cuda.is_available())

# -------------------------------------------
#           Sentiment Classification
# -------------------------------------------

# clf = pipeline("sentiment-analysis")

# print(clf("I'm so happy!"))

# -------------------------------------------
#                Generation
# -------------------------------------------

prompt = input("Prompt: ")

# gpt2 = pipeline("text-generation",model="gpt2")
# num_return_sequences = int(input("num_return_sequences: "))

# generations = gpt2(prompt, max_length=120, num_return_sequences=num_return_sequences)

# # print(prompt)
# for generation in generations:
#     print(f"Response:\n{generation['generated_text']}")

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role":"user","content":prompt}]
)

print(f"response={response}")
print(f"response.choices={response.choices}")
print(f"response.choices[0].message={response.choices[0].message}") 