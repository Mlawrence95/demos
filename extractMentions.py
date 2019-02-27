def extractMentionsScript(entities, remove = ['invoca']):
    import numpy as np
    import pandas as pd
    
    
    mentions = entities['user_mentions']
    numMentions = len(mentions)
    
    names = []
    
    for i in range(numMentions):
        name = mentions[i]['name'].lower()
        
        if name not in remove:
            names += [name]
            
    return names