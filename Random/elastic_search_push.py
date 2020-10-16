import certifi
from elasticsearch import Elasticsearch

def push_to_elastic_search(json_dict):
    elasticsearch = Elasticsearch(
        "https://a10:M0d3rnPyth0n@25c2c5d443a5685f26eaa48ac052325c.us-west-2.aws.found.io:9243",
        ca_certs=certifi.where())
    elasticsearch.index(index="a10_zapr", body=json_dict)