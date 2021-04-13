import re


number_of_sportszone_gifs = 0

p = re.compile(r'^.*\bsportszone\b.*\.gif".*$')

txt = open('con267.tweetie.799608879')

set_of_gifs = set()

for line in txt: 
    if p.match(line)!= None:
        set_of_gifs.add(str(p.match(line).group()))

for i in set_of_gifs:
    print(i)
print(len(set_of_gifs))

txt.close()