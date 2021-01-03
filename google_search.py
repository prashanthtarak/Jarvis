from googlesearch import search 
# import testing_audio
import webbrowser

query = ""



sr = []
for j in search(query, tld="co.in", num=5, stop=5, pause=1): 
    result = j.split('/')
    print(result[2])
    
    sr.append(j)


# print(sr)
# webbrowser.open(sr[0])
