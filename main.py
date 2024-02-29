import os
import csv
import openai
from time import time
from pathlib import Path
from conf import prompt_desc, structure, finish_detail


# from openai import OpenAI
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
prompt = openai.OpenAI(api_key=OPENAI_API_KEY)
prompt_chat_id = None
description = openai.OpenAI(api_key=OPENAI_API_KEY)
desc_chat_id = None
# thread = client.beta.threads.create()


class RequestToAI:
    def make_request(self, chat, content: str):
        response = chat.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "Ты превосходный копирайтер и пишешь тексты на русском языке. Тексты, которые ты пишешь касаются только тематик из списка: Пентхаусы, Квартиры и апартаменты,Виллы и дома,Таунхаусы,Земельные участки,Дуплексы,Жилой комплекс,Коммерческая недвижимость. Никаких других тем. Данные о типе недвидимости будут подаваться в запросе.",
                },
                {
                    "role": "user",
                    "content": content,
                },
            ],
        )
        return response


def sanitize(row_str: str) -> str:
    if row_str:
        return row_str.replace("\t", "").strip().replace("\r", "")
    else:
        return row_str


def check_response(response: str):
    if len(response) < 200:
        print(f"Something wrong, response`s length is only {len(response)}")
        input()


in_file = Path("1000.csv")
out_file = Path("1000 descriptions.csv")
request = RequestToAI()
fields_read = [
    "\ufeffСсылка",
    "H1",
    "City",
    "Area",
    "Type property",
    "Number of Bedrooms",
    "Square",
    "Price in AED",
    "Address",
    "To the sea",
    "To the center",
    "Due date",
    "Description",
    "Rent",
    "categoriya po komnatam",
    "Type",
    "Location",
    "Peculiarities",
    "Internal infrastructure",
    "External infrastructure",
    "",
]
fields_write = fields_read.copy()
fields_write.append("response")

start_time = time()


def main():
    counter = 0
    with open(out_file, "w", newline="", encoding="utf-8") as fo:
        writer = csv.DictWriter(
            fo, fieldnames=fields_write, delimiter=";", lineterminator="\r"
        )
        writer.writeheader()
        with open(in_file, "r", newline="", encoding="utf-8") as fi:
            while True:
                reader = csv.DictReader(fi, delimiter=";")
                for row in reader:
                    counter += 1
                    if counter == 31:
                        break
                    cur_time = time()
                    for k in fields_read:
                        row[k] = sanitize(row[k])

                    parameters = "Характеристики объекта недвижимости: "
                    for i in range(2, len(fields_read)):
                        parameters += f"{fields_read[i]} - {row[fields_read[i]]}, "

                    prompt_result = request.make_request(prompt, prompt_desc)

                    prompt_description = prompt_result.choices[0].message.content
                    check_response(prompt_description)
                    content = (
                        f"{prompt_description} {structure} {parameters} {finish_detail}"
                    )

                    completion = request.make_request(description, content)
                    result = completion.choices[0].message.content.replace("\n", "")
                    check_response(result)

                    row.update({"response": f"\t{result}"})
                    writer.writerow(row)

                    print(
                        f"Iteration #{counter}   Duration time {time()-cur_time} second"
                    )
                break
    print(f"Process was working {time()-start_time}")


if __name__ == "__main__":
    main()
