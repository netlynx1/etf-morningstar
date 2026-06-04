import json, yfinance as yf, pandas as pd, numpy as np
SECTORS={'Technology':'XLK','Healthcare':'XLV','Financials':'XLF','Industrials':'XLI','Energy':'XLE'}
results=[]
for sector,ticker in SECTORS.items():
    h=yf.Ticker(ticker).history(period='1y')
    if len(h)<252: continue
    current=float(h['Close'].iloc[-1])
    year=((current/h['Close'].iloc[0])-1)*100
    vol=float(h['Close'].pct_change().std()*np.sqrt(252)*100)
    results.append({'sector':sector,'ticker':ticker,'one_year_return':round(year,2),'volatility':round(vol,2)})
with open('docs/data/raw_data.json','w') as f: json.dump(results,f,indent=2)
