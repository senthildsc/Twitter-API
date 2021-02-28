# Twitter-API

In this exercise, I will be creating a twitter account and practice pulling data from Twitters publicly available API.

API Details       : Intellexer API is a cloud service that enables developers to embed natural language processing and text analysis tools in consumer and enterprise applications, or web-services using JSON or XML.
                    Intellexer API includes natural language processing solutions for sentiment analysis, entity recognition, summarization, document comparison, natural language interface for search engines, language detection, spell-checking, etc.
                    Intellexer API methods can be called from any programming language or software component that supports HTTP requests.

API Help          : http://esapi.intellexer.com/Home/Help
                    https://apilist.fun/api/intellexer


API Fields        :
                  summarizerDoc – information about the text
                  
                  id – document identifier                  
                  size – document size in bytes
                  title – document title
                  url – source of the request
                  error – information about processing errors
                  sizeFormat – formatted document size
                  structure – document structure
                  topics – array of detected document topics
                  items – summary items (important document sentences)
                  text – text of the summary item
                  rank – item rank. Larger rank means greater importance of the sentence
                  weight – item weight
                  totalItemsCount – total number of processed sentences
                  conceptTree – tree of important document concepts
                  sentenceIds – array of sentence identifiers containing detected concepts
                  text – concept text
                  w – concept weight
                  mp – “main phrase” – meaningful/important concepts used in NE relations tree
                  st – “status” – concept value change from 0 to 1, if the concept was selected for Rearrange operation
                  children array – concept tree that consists of root nodes (for ex. retrieval) and children nodes (for ex. information retrieval)
                  namedEntityTree – tree of relations among the detected entities
                  entityText – entity text
                  sentenceIds – array of sentence identifiers containing detected entities
                  text – entity text
                  w – entity weight
