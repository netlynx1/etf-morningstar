import os,json
from openai import OpenAI
with open('docs/data/rankings.json') as f: rankings=json.load(f)
prompt='Analyze these ETF rankings: '+str(rankings[:5])
client=OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
resp=client.responses.create(model='gpt-4.1-mini',input=prompt)
with open('docs/data/analysis.json','w') as f:
 json.dump({'daily_analysis':resp.output_text},f,indent=2)
