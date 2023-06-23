from pprint import pprint
import requests
import os
import urllib.parse

#appid = os.getenv('TPQ7XG-VR79QW8A2U', '...')
appid = 'TPQ7XG-VR79QW8A2U'

####################################################################
# Part 1
####################################################################

# equation = "7 + 2x = 12 - 3x"
# query = urllib.parse.quote_plus(f"solve {equation}")
# query_url = f"http://api.wolframalpha.com/v2/query?" \
#             f"appid={appid}" \
#             f"&input={query}" \
#             f"&includepodid=Result" \
#             f"&output=json"
#
# print(query_url)
# r = requests.get(query_url).json()
#
# print(r["queryresult"])
# data = r["queryresult"]["pods"][0]["subpods"][0]
# plaintext = data["plaintext"]
#
# print(f"Result of {equation} is '{plaintext}'.")
# # Result of 7 + 2x = 12 - 3x is 'x = 1'.


####################################################################
# Part 2
####################################################################

# equation = "7 + 2x = 12 - 3x"
# query = urllib.parse.quote_plus(f"solve {equation}")
# query_url = f"http://api.wolframalpha.com/v2/query?" \
#             f"appid={appid}" \
#             f"&input={query}" \
#             f"&scanner=Solve" \
#             f"&podstate=Result__Step-by-step+solution" \
#             "&format=plaintext" \
#             f"&output=json"
#
# r = requests.get(query_url).json()
#
# data = r["queryresult"]["pods"][0]["subpods"]
# result = data[0]["plaintext"]
# steps = data[1]["plaintext"]
#
# print(f"Result of {equation} is '{result}'.\n")
# print(f"Possible steps to solution:\n\n{steps}")
#


####################################################################
# Part 3
####################################################################
# equation = "7 + 2x = 12 - 3x"
# query = urllib.parse.quote_plus(f"solve {equation}")
# query_url = f"http://api.wolframalpha.com/v2/query?" \
#             f"appid={appid}" \
#             f"&input={query}" \
#             f"&scanner=Solve" \
#             f"&podstate=Result__Step-by-step+solution" \
#             "&format=mathml" \
#             f"&output=json"
#
# r = requests.get(query_url).json()
#
# data = r["queryresult"]["pods"][0]["subpods"]
# result = data[0]["mathml"]
# steps = data[1]["mathml"]
#
# print(f"MathML result of {equation} is:\n")
# print(f"{result}")
# print(f"Possible steps to solution:\n\n{steps}")


####################################################################
# Part 4
####################################################################

# formula = "((P AND (Q IMPLIES R)) OR S) AND T"
# query = urllib.parse.quote_plus(f"solve {formula}")
# query_url = f"http://api.wolframalpha.com/v2/query?" \
#             f"appid={appid}" \
#             f"&input=solve {formula}" \
#             f"&output=json" \
#             f"&includepodid=Input" \
#             f"&includepodid=MinimalForms" \
#             f"&includepodid=TruthDensity"
#
# r = requests.get(query_url).json()
#
# pods = r["queryresult"]["pods"]
# expression = pods[0]["subpods"][0]["plaintext"]
# min_forms = "\n".join(pods[1]["subpods"][0]["plaintext"].split("\n")[:-1])
# truth_density = pods[2]["subpods"][0]["plaintext"].split("=")
#
# print(f"Expression {expression}: \n")
# print(f"{min_forms}\n")
# print(f"Truth density equals {truth_density[0]} which is {truth_density[1]}")


####################################################################
# Part 5
####################################################################

# function = "sin x cos y"
# query = f"plot {function}"
# query_url = f"http://api.wolframalpha.com/v2/query?" \
#             f"appid={appid}" \
#             f"&input={query}" \
#             f"&output=json" \
#             f"&includepodid=3DPlot" \
#             f"&includepodid=ContourPlot"
#
# r = requests.get(query_url).json()
#
# pods = r["queryresult"]["pods"]
# plot_3d_url = pods[0]["subpods"][0]["img"]["src"]
# plot_contour_url = pods[1]["subpods"][0]["img"]["src"]
#
# img_name = "3d_plot.jpg"
# img_data = requests.get(plot_3d_url).content
# with open(img_name, 'wb') as handler:
#     handler.write(img_data)
#     print(f"3D Plot Image Saved to {img_name}.")


####################################################################
# Part 6
####################################################################
#
# query = "AAGCTAGCTAGC"
# query_url = f"http://api.wolframalpha.com/v2/query?" \
#             f"appid={appid}" \
#             f"&input={query}" \
#             f"&scanner=Genome" \
#             f"&output=json" \
#             f"&includepodid=Length" \
#             f"&includepodid=AminoAcidSequence" \
#             f"&includepodid=MeltingTemperature" \
#
# r = requests.get(query_url).json()
#
# pods = r["queryresult"]["pods"]
#
# length = {
#     "title": pods[0]["title"],
#     "value": pods[0]["subpods"][0]["plaintext"]
# }
# amino_sequence = {
#     "title": pods[1]["title"],
#     "value": pods[1]["subpods"][0]["plaintext"].replace(") ", ")\n")
# }
# melting_temp = {
#     "title": pods[2]["title"],
#     "value": pods[2]["subpods"][0]["plaintext"]
# }
#
# print(f"{length['title']}: {length['value']}\n")
# print(f"{amino_sequence['title']}:\n {amino_sequence['value']}\n")
# print(f"{melting_temp['title']}: {melting_temp['value']}")



####################################################################
# Part 7
####################################################################
#
# question = "what is the most spoken language in the world?"
# query_url = f"http://api.wolframalpha.com/v1/spoken?" \
#             f"appid={appid}" \
#             f"&i={question}" \
#
# r = requests.get(query_url)
#
# print(r.text)
#

####################################################################
# Part 8
####################################################################

# question = "Where are Falkland Islands?"
# location = "47.01,16.93"
# query_url = f"http://api.wolframalpha.com/v1/conversation.jsp?" \
#             f"appid={appid}" \
#             f"&geolocation={appid}" \
#             f"&i={question}" \
#
# r = requests.get(query_url).json()
# answer = r["result"]
# conversation_id = r["conversationID"]
# host = r["host"]
#
# print(f"{question}: '{answer}'")
#
# followup_question = "How far is it from here?"
# query_url = f"http://{host}/api/v1/conversation.jsp?" \
#             f"appid={appid}" \
#             f"&conversationID={conversation_id}" \
#             f"&i={followup_question}" \
#
# r = requests.get(query_url).json()
# answer = r["result"]
# print(f"{followup_question}: '{answer}'")

#####################################################
# 2 additional services Conversational API
####################################################
#
third_question = "What is the capital of Nebraska?"
query_url = f"http://api.wolframalpha.com/v1/conversation.jsp?" \
            f"appid={appid}" \
            f"&i={third_question}" \

r = requests.get(query_url).json()
answer = r["result"]
conversation_id = r["conversationID"]
host = r["host"]

print(f"{third_question}: '{answer}'")

second_followup_question = "What is the population in the capital city of Nebraska?"
query_url = f"http://{host}/api/v1/conversation.jsp?" \
            f"appid={appid}" \
            f"&conversationID={conversation_id}" \
            f"&i={second_followup_question}" \

r = requests.get(query_url).json()
answer = r["result"]
print(f"{second_followup_question}: '{answer}'")

#####################################################
# first additional services Full API
####################################################

query = urllib.parse.quote_plus("wheat harvested in the united states in 2019")
query_url = f"http://api.wolframalpha.com/v2/query?" \
             f"appid={appid}" \
             f"&input={query}" \
             f"&format=plaintext" \
             f"&output=json"


r = requests.get(query_url).json()
#print(r)

data = r["queryresult"]["pods"][1]["subpods"][0]
datasource = ", ".join(data["datasources"]["datasource"])
microsource = data["microsources"]["microsource"]
plaintext = data["plaintext"]

print(query)
print(f"Result: '{plaintext}' from {datasource} ({microsource}).")

#####################################################
# second additional services Full API
####################################################

query = urllib.parse.quote_plus("What was the united states population in 2019")
query_url = f"http://api.wolframalpha.com/v2/query?" \
             f"appid={appid}" \
             f"&input={query}" \
             f"&format=plaintext" \
             f"&output=json"


r = requests.get(query_url).json()
#print(r)

data = r["queryresult"]["pods"][1]["subpods"][0]
datasource = ", ".join(data["datasources"]["datasource"])
microsource = data["microsources"]["microsource"]
plaintext = data["plaintext"]

print(query)
print(f"Result: '{plaintext}' from {datasource} ({microsource}).")
