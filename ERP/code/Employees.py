# ref = https://jobs.sap.com/content/Leadership/?locale=en_US

import csv
from nltk.chat.util import Chat, reflections

with open("C:\\study\\ERP_chatbot\\datasets\\Employees.csv", 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    header = next(reader)  # Get the header
    rows = list(reader)  # Get all the rows

# Combine the header and each row into a dictionary, then convert to a string
rows_str = ['\n'.join(f'{k} : {v}' for k, v in zip(header, row)) for row in rows]

# Generate pairs using a loop
pairs = [[f"{i+30001}", [rows_str[i],]] for i in range(len(rows_str))]

pairs.append([r"quit", ["Thank you.\nIt was nice talking to you.\nHave a wonderful day!:)"]])

def chatbot():
    print("Hello!\nI am here to help you find sample of SAP employee contacts.\n"
          "Please enter the Employee ID you wish to search for.\n"
          "Employee ID is a 5 digit number starting from 30001 to 30020."
          )

    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()