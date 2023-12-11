# https://youtu.be/bB7xkRsEq-g?t=1807
# 

import openai

# Use the OpenAI API key
openai.api_key = "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"

# Define the prompt for the GPT-3 model
who = input("\nWho would you like to read about?")
userPrompt = "write a long essay about " + who
# Get the response from the GPT-3 model
print("\n*** ",userPrompt.upper()," ***\n" )
response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=userPrompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

# Print the response from the model
print(response["choices"][0]["text"], '\n')
