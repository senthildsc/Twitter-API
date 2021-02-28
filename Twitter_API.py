'''
Name              : Senthilraj Srirangan
Date              : 02/29/2020
Description       : working on a term project to either pull data from an API
'''

'''
API Details       : Intellexer API is a cloud service that enables developers to embed natural language processing and text analysis tools in consumer and enterprise applications, or web-services using JSON or XML.
                    Intellexer API includes natural language processing solutions for sentiment analysis, entity recognition, summarization, document comparison, natural language interface for search engines, language detection, spell-checking, etc.
                    Intellexer API methods can be called from any programming language or software component that supports HTTP requests.

API Help          : http://esapi.intellexer.com/Home/Help
                    https://apilist.fun/api/intellexer

API Fields        :
                  ‘summarizerDoc’ – information about the text
                      ‘id’ – document identifier
                      ‘size’ – document size in bytes
                      ‘title’ – document title
                      ‘url’ – source of the request
                      ‘error’ – information about processing errors
                      ‘sizeFormat’ – formatted document size
                ‘structure’ – document structure
                ‘topics’ – array of detected document topics
                ‘items’ – summary items (important document sentences)
                      ‘text’ – text of the summary item
                      ‘rank’ – item rank. Larger rank means greater importance of the sentence
                      ‘weight’ – item weight
                ‘totalItemsCount’ – total number of processed sentences
                ‘conceptTree’ – tree of important document concepts
                      ‘sentenceIds’ – array of sentence identifiers containing detected concepts
                      ‘text’ – concept text
                      ‘w’ – concept weight
                      ‘mp’ – “main phrase” – meaningful/important concepts used in NE relations tree
                      ‘st’ – “status” – concept value change from 0 to 1, if the concept was selected for Rearrange operation
                      ‘children’ array – concept tree that consists of root nodes (for ex. retrieval) and children nodes (for ex. information retrieval)
                ‘namedEntityTree’ – tree of relations among the detected entities
                      ‘entityText’ – entity text
                      ‘sentenceIds’ – array of sentence identifiers containing detected entities
                      ‘text’ – entity text
                      ‘w’ – entity weight

'''
# Libraries Needed for this project
import os
import json
import requests
import sys

API_KEY = os.getenv('INTELLEXER_API_KEY')  # API_KEY saved as Environmental Variable and passing to the API Request.


def Parse_json_response_data(data):
    # ‘summarizerDoc’ – information about the text

    print('SUMMARIZERDOC')
    for item, value in data['summarizerDoc'].items():
        print(item, '-->', value)

    print('\n')

    # ‘structure’ – document structure

    print('STRUCTURE')
    print('structure', '-->', data['structure'], '\n')

    # ‘topics’ – array of detected document topics
    print('TOPICS')

    for topic in data['topics']:
        print(topic)
    print('\n')

    # ‘items’ – summary items (important document sentences)

    print('ITEMS')

    for item in data['items']:
        for item, value in item.items():
            print(item, '-->', value)
    print('\n')

    # ‘totalItemsCount’ – total number of processed sentences

    print('TOTALITEMSCOUNT')

    print('totalItemsCount', '--->', data['totalItemsCount'], '\n')

    # ‘conceptTree’ – tree of important document concepts

    print('CONCEPT TREE')

    for item, value in data['conceptTree'].items():
        print(item, '--->', value)
    print('\n')

    # ‘namedEntityTree’ – tree of relations among the detected entities

    print('NAMED ENTITY TREE')
    print(data['namedEntityTree'])

    for item, value in data['namedEntityTree'].items():
        print(item, '--->', value)


def establish_api_connection():
    try:
        url = "https://api.intellexer.com/summarize?apikey={}&conceptsRestriction=1&fullTextTrees=true&loadConceptsTree=true&loadNamedEntityTree=true&options=%7B%22topics%22%3A%20%5B%5D%2C%20%22reorderConcepts%22%3A%20%5B%7B%22term%22%3A%22fish%22%2C%20%22selection%22%3A%20%5B%22farmed%20fish%22%2C%20%22commercial%20fish%22%5D%7D%2C%20%7B%22term%22%3A%22fishing%22%2C%20%22selection%22%3A%20%5B%22sport%20fishing%22%5D%7D%5D%7D&returnedTopicsCount=1&structure=General&summaryRestriction=1&textStreamLength=1000&url=http%3A%2F%2Fwww.infoplease.com%2Fbiography%2Fvar%2Fbarackobama.html&useCache=true&usePercentRestriction=true&wrapConcepts=true".format(
            API_KEY)
        response = requests.request("GET", url)
        response.raise_for_status()
        code = response.status_code
        data = json.loads(response.text)
        return data
    except requests.exceptions.HTTPError as err:
        code = str(err)
        if code == 400:
            print('Bad Request')
        if code == 500:
            print('Internal Server Error')
        else:
            print(code)
        sys.exit(1)


def main():
    data = establish_api_connection()  # Function Call to Establish API Connection
    Parse_json_response_data(data)


if __name__ == "__main__":
    main()
