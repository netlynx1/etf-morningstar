import json
with open('docs/data/raw_data.json') as f:data=json.load(f)
for d in data:
    d['score']=round(d['one_year_return']-d['volatility']*0.1,2)
ranked=sorted(data,key=lambda x:x['score'],reverse=True)
with open('docs/data/rankings.json','w') as f: json.dump(ranked,f,indent=2)
