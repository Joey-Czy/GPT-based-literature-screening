import openai
from openai import OpenAI
client = OpenAI()
import csv
import os

sys_input = "You are ChatGPT-4o, a large language model trained by OpenAI. Knowledge cutoff: 2024-07. Current date: 2024-07"
results = []
Num = 1
with open(r"YourFileName.csv",encoding='utf-8') as file_obj:
    reader_obj = csv.reader(file_obj) 
    for row in reader_obj:
        print('Num: ', Num)
        Num += 1
        input1 = row[0]
        input2 = row[1]
        input = "Evaluate the relevance of the following paper to robotic assembly in the construction industry.\
        - Title: {} \
        - Abstract:{} \
        - Please ensure the paper meets the following criteria before making your judgment:\
        1.The paper must present original research data, workflows, applications, or detailed case studies.\
        2.The paper should focus on dedicated research rather than being a compilation or review of existing works.\
        3.The paper can study any type of robots, except exoskeletons and tele-operated machines.\
        4.The paper must focus on robotic assembly technologies. If the paper is only about robotic manufacturing techniques (e.g., cutting or 3D printing) or joining technique (e.g., bolting or screwing), then it should be excluded.\
        5.The research must explicitly address robotic assembly technologies within the construction industry. The materials or structures discussed should be directly related to construction.\
        Respond with '1' if the paper satisfies all of the above criteria, and with '0' if it does not, providing a concise explanation. The output format should be 1:... or 0:... (don't be str format)\ \ ".format(input1,input2)
        
        # print(input)
        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=[ 
                {"role": "system", "content": sys_input},
                    {"role": "user", "content": input},
                ],
                temperature = 0.1
            )
        message = response.choices[0].message.content
        results.append([message[0], message[2:]])
        
        