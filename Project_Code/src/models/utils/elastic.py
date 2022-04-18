from elasticsearch import Elasticsearch, helpers
 
elastic_client = Elasticsearch([{'host': 'localhost', 'port': '9200'}])
  
helpers.bulk(elastic_client, dictvalue, index="ml-predictions-domains")