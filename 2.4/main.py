responses = open("2.4/responses.csv")

for response in responses:
    response = response.split(",")
    if "5" or "7" in response:
        print(response)
