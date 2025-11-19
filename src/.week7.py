import requests
import json
headers={"User-Agent" : "test/0.0"}
s = requests.Session()
s.headers.update({"User-Agent" : "test/0.0"})

#gets the revision history and sorces count
params = {"action" : "query", "format" : "json" , "formatversion" : 2, "meta" : "siteinfo", 
          "generator" : "random" , "grnnamespace" : 0, 
          "prop" : "revisions|extracts|contributors|extlinks|info","ellimit" : "max","rvlimit" : "max", "explaintext" :1, "inprop":"url" , "rvdir":"newer"}

outp = s.get("https://en.wikipedia.org/w/api.php",params=params).json()
print("article " + outp["query"]["pages"][0]["title"])
print("date of first revision " + (str)((outp["query"]["pages"][0]["revisions"][0]["timestamp"])))
print("amount of revisions " + (str)(len(outp["query"]["pages"][0]["revisions"])))
print("number of contributors " + (str)(len(outp["query"]["pages"][0]["contributors"])))
print("number of characters in the text " + (str)(len(outp["query"]["pages"][0]["extract"])))
if "extlinks" in outp["query"]["pages"][0]:
    print("amount of sources " + (str)(len(outp["query"]["pages"][0]["extlinks"])))
else:
    print("amount of sources 0")

print(outp["query"]["pages"][0]["extract"])


url = (outp["query"]["pages"][0]["fullurl"]).replace("https://en.wikipedia.org/wiki/","")
date = outp["query"]["pages"][0]["revisions"][0]["timestamp"].replace("-","").split("T")[0]
query = f"https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia.org/all-access/user/{url}/monthly/{date}/20251118"
outb = s.get(query).json()

totalviews = 0
for view in outb["items"]:
    totalviews += view["views"]
print()
print("ratio views/revisions " + (str)(totalviews/len(outp["query"]["pages"][0]["revisions"])))