import elasticsearch
from elasticsearch_dsl import Search
#import awswrangler as wr
import time
''' 
ELASTIC_HOST = 'https://search-wikidata-wfuu4kroubibtcbnwl77vh226a.us-east-2.es.amazonaws.com/'

client = wr.opensearch.connect(
    host=ELASTIC_HOST,
    username='admin',
    password='Wikidata@2022'
)
'''

ELASTIC_HOST = 'http://localhost:9200/'

client = elasticsearch.Elasticsearch(hosts=[ELASTIC_HOST])

def lookup(query, index='wikidata_index', fields=['arlabel', 'enlabel' ,'araliases','enaliases','arwiki','arwikiquote']):
    if not query:
        return 
    results = Search(
        index=index).using(client).query("multi_match", fields=fields, fuzziness='AUTO', query=query)
    start= time.time()    

    q_results = []
    wikidats_base_url ='https://www.wikidata.org/wiki/'
    wikipedia_base_url='https://ar.wikipedia.org/wiki/'


    seen = set()
  
         
    for hit in results:
        print(hit)
        if hit.id in seen:
            continue
        else:
            seen.add(hit.id)
            data = {
                "id": hit.id,
                "url":wikidats_base_url+hit.id,
                "arlabel": hit.arlabel,
                "araliases": hit.araliases,
                "aleniases":hit.enaliases,
                "enlabel":hit.enlabel,
                "arwiki":hit.arwiki,
                "arwiki_url":wikipedia_base_url + hit.arwiki.replace(' ','_'),
                "ardescription": hit.ardescription,
                "endescription": hit.endescription,
                "score": hit.meta.score
            }
            q_results.append(data)

    #q_results['url'] = wikidats_base_url+ q_results.id
    #q_results['arwiki_url'] = wikipedia_base_url + q_results.arwiki.replace(' ','_')
    end=time.time() 
    hours, rem = divmod(end-start, 3600)
    minutes, seconds = divmod(rem, 60)

    if len(q_results) >0:
        msg= 'The number of the results for the query {} are {}. Execution time {:0>2}:{:0>2}:{:05.2f}'.format(query, len(q_results),int(hours),int(minutes),seconds) 

    else:
        msg='Sorry, we can not find any result that matchs your query' 

    print(msg)
    return q_results, msg


def lookup_ned(query, index='wikidata_index', fields=['arlabel', 'enlabel' ,'araliases','enaliases','arwiki','arwikiquote']):
    if not query:
        return 
    results = Search(
        index=index).using(client).query("multi_match", fields=fields, fuzziness='AUTO', query=query)
    start= time.time()    

    q_results = []
    wikidats_base_url ='https://www.wikidata.org/wiki/'
    wikipedia_base_url='https://ar.wikipedia.org/wiki/'


    seen = set()
  
         
    for hit in results:
        print(hit)
        if hit.id in seen:
            continue
        else:
            seen.add(hit.id)
            data = {
                "id": hit.id,
                "url":wikidats_base_url+hit.id,
                "arlabel": hit.arlabel,
                "araliases": hit.araliases,
                "aleniases":hit.enaliases,
                "enlabel":hit.enlabel,
                "arwiki":hit.arwiki,
                "arwiki_url":wikipedia_base_url + hit.arwiki.replace(' ','_'),
                "ardescription": hit.ardescription,
                "endescription": hit.endescription,
                "score": hit.meta.score
            }
            q_results.append(data)

    #q_results['url'] = wikidats_base_url+ q_results.id
    #q_results['arwiki_url'] = wikipedia_base_url + q_results.arwiki.replace(' ','_')
    end=time.time() 
    hours, rem = divmod(end-start, 3600)
    minutes, seconds = divmod(rem, 60)

    if len(q_results) >0:
        msg= 'The number of the results for the query {} are {}. Execution time {:0>2}:{:0>2}:{:05.2f}'.format(query, len(q_results),int(hours),int(minutes),seconds) 

    else:
        msg='Sorry, we can not find any result that matchs your query' 

    print(msg)
    return q_results, msg    