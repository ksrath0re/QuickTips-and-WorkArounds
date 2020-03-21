1. Converting colon separated list into a dict

def list_to_dict(rlist):
    return dict(map(lambda s : s.split(':'), rlist))
   
 or
 
 dict(e.split(':') for e in li)
https://stackoverflow.com/questions/42059332/converting-colon-separated-list-into-a-dict

2. Dump a dict to a json file

import json
with open('result.json', 'w') as fp:
    json.dump(sample, fp)

https://stackoverflow.com/questions/17043860/how-to-dump-a-dict-to-a-json-file
