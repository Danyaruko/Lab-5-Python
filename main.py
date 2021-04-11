import re


number_of_sportszone_gifs = 0

p = re.compile(r'^.*\bsportszone\b.*\.gif".*$')

txt = open('con267.tweetie.799608879')

for line in txt: 
    if p.match(line)!= None:
        print(p.match(line).group())
        number_of_sportszone_gifs += 1

print(number_of_sportszone_gifs)

txt.close()