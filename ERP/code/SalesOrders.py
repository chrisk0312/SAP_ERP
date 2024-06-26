# ref = https://www.sap.com/products/erp.html 
import csv
from nltk.chat.util import Chat, reflections

with open("C:\\study\\ERP_chatbot\\datasets\\SalesOrders.csv", 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    header = next(reader)  # Get the header
    rows = list(reader)  # Get all the rows

# Combine the header and each row into a dictionary, then convert to a string
rows_str = ['\n'.join(f'{k} : {v}' for k, v in zip(header, row)) for row in rows]

# Generate pairs using a loop
pairs = [[f"{i+50001}", [rows_str[i],]] for i in range(len(rows_str))]

pairs.append([r"quit", ["Thank you.\nIt was nice talking to you.\nHave a wonderful day!:)"]])

def chatbot():
    print("Hello!\nI am here to help you find sample of SAP Sales Order.\n"
          "Please enter the Sales Order Item ID you wish to search for.\n"
          "Sales Order Item ID is a 5 digit number starting from 50001 to 50009."
          )

    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()
#tests


