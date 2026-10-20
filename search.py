"""Search public Google News RSS indexes; results are leads, not verified solicitations."""
import datetime,json,urllib.parse,urllib.request,xml.etree.ElementTree as ET,pathlib,time
QUERIES=[
 'Florida commercial building maintenance RFP Orlando',
 'Tampa facility maintenance contractor bid',
 'Lakeland Florida property maintenance solicitation',
 'Central Florida drywall painting maintenance subcontractor opportunity',
 'Orlando commercial property management vendor maintenance',
 'Florida government building repairs invitation to bid',
]
items=[];seen=set()
for query in QUERIES:
    url='https://news.google.com/rss/search?q='+urllib.parse.quote(query)+'&hl=en-US&gl=US&ceid=US:en'
    try:
        req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0 (compatible; ContractHunter/1.0)'})
        with urllib.request.urlopen(req,timeout=20) as response: xml=response.read()
        root=ET.fromstring(xml)
        for item in root.findall('.//channel/item')[:15]:
            title=item.findtext('title','').strip();link=item.findtext('link','').strip()
            if not title or not link or link in seen:continue
            seen.add(link)
            items.append({'title':title,'link':link,'published':item.findtext('pubDate',''),'query':query})
    except Exception as exc:
        print('Search failed:',query,repr(exc))
    time.sleep(1)
out={'updated_at':datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M'),'items':items}
pathlib.Path(__file__).with_name('opportunities.json').write_text(json.dumps(out,indent=2))
print('Search results:',len(items))
