import wolframalpha

user_input = input("Question: the lifespan of a mosquito")
app_id = "TPQ7XG-VR79QW8A2U"
client = wolframalpha.Client(app_id)

res = client.query(user_input)
answer = next(res.results).text

print (answer)
