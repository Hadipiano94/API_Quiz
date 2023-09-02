import requests

parameters = {"amount": 10,
              "category": 18,
              # "difficulty": "easy",
              "type": "boolean",
              }
response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()

question_data = response.json()["results"]
# for question in question_data:
#     question["question"] = question["question"].replace("&quot;", "\"")
#     question["question"] = question["question"].replace("&#039;", "'")

# print(*[question["question"] + "   " + question["correct_answer"] for question in question_data], sep="\n")
