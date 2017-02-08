import requests
import argparse

"""This app consumes the pearson API to get access to the Longman Dictionary
   and return the definition for a given word."""

parser = argparse.ArgumentParser(
    description="A Simple Command Line Dictionary Program")
parser.add_argument('word', type=str, help='enter a word to be translated')

args = parser.parse_args()
api_url = 'http://api.pearson.com/v2/dictionaries/ldoce5/entries'


payload = {'headword': args.word}
try:
    response = requests.get(api_url, params=payload)
except ConnectionError:
    print("Could not establish a connection")
except TimeoutError:
    print("The request timed out")

json_data = response.json()

r = json_data['results']
print("Word: {}".format(args.word))
for i in range(0, len(r)):
    if r[i]['headword'] == args.word:
        print("Part of speech: {}".format(r[i]['part_of_speech']))

        print("Definition:")
        print(r[i]['senses'][0]['definition'])
        print("\n")







