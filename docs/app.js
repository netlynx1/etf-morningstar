async function loadData(){
 const rankings=await fetch('./data/rankings.json').then(r=>r.json());
 const analysis=await fetch('./data/analysis.json').then(r=>r.json());
 document.getElementById('top-sector').innerHTML=`<h2>Top Sector: ${rankings[0].sector}</h2>`;
 document.getElementById('analysis').innerText=analysis.daily_analysis;

 const ctx=document.getElementById('sectorChart');
 new Chart(ctx,{
  type:'bar',
  data:{
   labels:rankings.map(r=>r.ticker),
   datasets:[{label:'Score',data:rankings.map(r=>r.score)}]
  }
 });
}
loadData();