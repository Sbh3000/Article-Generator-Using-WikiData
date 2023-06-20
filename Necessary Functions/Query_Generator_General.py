# //General Query Formation Code

query2 = '''
  { ?article  schema:about       ?item ;
              schema:inLanguage  "en" ;
              schema:isPartOf    <https://en.wikipedia.org/>
              '''              
#   Note : Do not use the wiki data entity type link
query3 = f'''          
    FILTER ( ?item = <{//Input link specific to wiki data "Not the entity link"}> ) 
    '''
query4 = ''' 
   OPTIONAL
      { ?item  wdt:P735  ?Name }
   OPTIONAL
      { ?item wdt:P21  ?Gender }
   OPTIONAL
      { ?item  wdt:P103  ?F_language }
   OPTIONAL
      { ?item  wdt:P569  ?Born_date }
   OPTIONAL
      { ?item  wdt:P570  ?RIP }
   OPTIONAL
      { ?item  wdt:P19  ?Birth_City }
   OPTIONAL
      { ?item  wdt:P27  ?Ntn }
   OPTIONAL
      { ?item  wdt:P22  ?Father_Name }
   OPTIONAL
      { ?item  wdt:P25  ?Mother_Name }
   OPTIONAL
      { ?item  wdt:P69  ?Person_Edu }
   OPTIONAL
      { ?item  wdt:P21  ?Pronoun }
   OPTIONAL
      { ?item  wdt:P106  ?Person_Work }
   OPTIONAL
      { ?item  wdt:P2218  ?NetWorth }
   OPTIONAL
      { ?item  wdt:P8687  ?SocialMedia_Followers }
   OPTIONAL
      { ?item  wdt:P140  ?Person_Religion }
    SERVICE wikibase:label
      { bd:serviceParam
                  wikibase:language  "en"
      }
  }
GROUP BY ?item ?itemLabel ?itemDescription
'''


url = 'https://query.wikidata.org/sparql'
query1 = f'''
PREFIX  schema: <http://schema.org/>
PREFIX  bd:   <http://www.bigdata.com/rdf#>
PREFIX  wdt:  <http://www.wikidata.org/prop/direct/>
PREFIX  wikibase: <http://wikiba.se/ontology#>

SELECT DISTINCT  ?item ?itemLabel ?itemDescription (SAMPLE(?Name) AS ?NameSample) (SAMPLE(?F_language) AS ?F_languageSample) (SAMPLE(?Person_Edu) AS ?Person_EduSample) (SAMPLE(?Pronoun) AS ?PronounSample) (SAMPLE(?Person_Work) AS ?Person_WorkSample) (SAMPLE(?Father_Name) AS ?Father_NameSample) (SAMPLE(?Mother_Name) AS ?Mother_NameSample) (SAMPLE(?Born_date) AS ?Born_dateSample) (SAMPLE(?Birth_City) AS ?Birth_CitySample) (SAMPLE(?article) AS ?articleSample)(SAMPLE(?RIP) AS ?RIPSample) (SAMPLE(?Ntn) AS ?NtnSample) (SAMPLE(?Person_Religion) AS ?Person_ReligionSample) (SAMPLE(?SocialMedia_Followers) AS ?SocialMedia_FollowersSample) (SAMPLE(?NetWorth) AS ?NetWorthSample) (SAMPLE(?Gender) AS ?GenderSample)
WHERE

'''
query = query1 + query2 + query3 + query4


r = requests.get(url, params = {'format': 'json', 'query': query})
data = r.json()


# //OutPut Query General //
# PREFIX  schema: <http://schema.org/>
# PREFIX  bd:   <http://www.bigdata.com/rdf#>
# PREFIX  wdt:  <http://www.wikidata.org/prop/direct/>
# PREFIX  wikibase: <http://wikiba.se/ontology#>

# SELECT DISTINCT  ?item ?itemLabel ?itemDescription (SAMPLE(?Name) AS ?NameSample) (SAMPLE(?F_language) AS ?F_languageSample) (SAMPLE(?Person_Edu) AS ?Person_EduSample) (SAMPLE(?Pronoun) AS ?PronounSample) (SAMPLE(?Person_Work) AS ?Person_WorkSample) (SAMPLE(?Father_Name) AS ?Father_NameSample) (SAMPLE(?Mother_Name) AS ?Mother_NameSample) (SAMPLE(?Born_date) AS ?Born_dateSample) (SAMPLE(?Birth_City) AS ?Birth_CitySample) (SAMPLE(?article) AS ?articleSample)(SAMPLE(?RIP) AS ?RIPSample) (SAMPLE(?Ntn) AS ?NtnSample) (SAMPLE(?Person_Religion) AS ?Person_ReligionSample) (SAMPLE(?SocialMedia_Followers) AS ?SocialMedia_FollowersSample) (SAMPLE(?NetWorth) AS ?NetWorthSample) (SAMPLE(?Gender) AS ?GenderSample)
# WHERE


#   { ?article  schema:about       ?item ;
#               schema:inLanguage  "en" ;
#               schema:isPartOf    <https://en.wikipedia.org/>
                        
#     FILTER ( ?item = <http://www.wikidata.org/entity/Q1058> )
     
#    OPTIONAL
#       { ?item  wdt:P735  ?Name }
#    OPTIONAL
#       { ?item wdt:P21  ?Gender }
#    OPTIONAL
#       { ?item  wdt:P103  ?F_language }
#    OPTIONAL
#       { ?item  wdt:P569  ?Born_date }
#    OPTIONAL
#                   wikibase:language  "en"
#       }
#   }
# GROUP BY ?item ?itemLabel ?itemDescription