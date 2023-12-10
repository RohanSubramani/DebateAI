# import site; print(site.getsitepackages())


from transformers import pipeline
from openai import OpenAI
# In terminal, or bashrc: export OPENAI_API_KEY='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'
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
cont = True
user_defines_debate = True
while cont:

    if user_defines_debate:
        
        print("Complete the following sentences to elicit the desired behavior from the LLMs.")
        debate_desc = input("Write a debate between P1 and P2 about ")
        P1_desc = input("Here is some info about P1: ")
        P2_desc = input("Here is some info about P2: ")
        bonus_details = input("Bonus criteria for the debate (leave blank if none): ")

        prompt = f"Write a debate between P1 and P2 about {debate_desc}\nHere is some info about P1: {P1_desc}\nHere is some info about P2: {P2_desc}\nMake the debate as interesting and educational as possible for someone interested in this topic. Before the start of the debate, list some key points that the reader should pay attention to, and make sure those come up in the debate."

        if bonus_details != "":
            prompt += f"Bonus criteria for the debate: {bonus_details}"

    else:
        prompt = f"Write another debate in the following format, but use an entirely different topic and speaking style.\n{response.choices[0].message.content}. Recall, your job is to write another debate in the same format, but use an entirely different topic and speaking style.\n"

    print("Wait a moment while the debate is prepared.")

    # gpt2 = pipeline("text-generation",model="gpt2")
    # num_return_sequences = int(input("num_return_sequences: "))

    # generations = gpt2(prompt, max_length=120, num_return_sequences=num_return_sequences)

    # # print(prompt)
    # for generation in generations:
    #     print(f"Response:\n{generation['generated_text']}")

    client = OpenAI()

    response = client.chat.completions.create(
        model="gpt-3.5-turbo", # "gpt-4",
        messages=[{"role":"user","content":prompt}]
    )

    # print(f"response={response}")
    # print(f"response.choices={response.choices}")
    print(response.choices[0].message.content)

    with open("debates.txt","a+") as file:
        file.write("   ----------------------   \n" + response.choices[0].message.content + "\n")

    print("Debate written to debate.txt.")

    cont = True if input("Generate another debate? [y/n]: ") in "yesYes" else False
    if cont:
        user_defines_debate = True if input("User defines next debate? [y/n]: ") in "yesYes" else False