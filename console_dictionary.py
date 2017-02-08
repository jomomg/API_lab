import requests
import argparse

"""This app consumes the pearson API to get access to the Longman Dictionary
   and return the definition for a given word."""

parser = argparse.ArgumentParser(
    description="A Simple Command Line Dictionary Program",
    usage="console_dictionary.py word1 word2 word3 ...")
parser.add_argument('word', nargs='*', type=str, help='enter words to get definitions')

args = parser.parse_args()
api_url = 'http://api.pearson.com/v2/dictionaries/ldoce5/entries'

for word in args.word:
    payload = {'headword': word}
    try:
        response = requests.get(api_url, params=payload)
        response.raise_for_status()
    except ConnectionError:
        print("Could not establish a connection")
        exit(2)
    except TimeoutError:
        print("The request timed out")
        exit(3)

    json_data = response.json()
    r = json_data['results']

    print("Word: {}".format(word))
    for i in range(0, len(r)):
        if word == r[i]['headword']:
            print("Part of speech: {}".format(r[i]['part_of_speech']))
            print("Definition:")
            print(r[i]['senses'][0]['definition'])
            print("")
    print("\n")





