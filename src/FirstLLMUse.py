import openai
env_file=open('./keys.env','r')
propn, propv=env_file.read().split("=")
openai.api_key=propv ## openai api key

def get_prompt_output(messages,model='gpt-3.5-turbo',temprature=0,max_tokens=1000):
    response=openai.ChatCompletion.create(
        messages=messages,
        model=model,
        temprature=temprature,
        max_tokens=max_tokens)
    return response.choices[0].message["content"]

messages=[{'role':'system','content':'Respond in 1 sentence'},{'role':'user','content':'What is the capital of India?'}]

response=get_prompt_output(messages)
print(response)
