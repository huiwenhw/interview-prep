'''
Given data, event and array of segments, I want to find what's the analytics for a given event based on the segments 
Given event: 'Signup' and segments: ['city', 'gender', 'origin'], 
Output: {'Signup': {'NYC': {'M': {'twitter': 1}, 'F': {'google': 2, 'twitter': 1}}, 'Oakland': {'M': {'google': 1}}}}
'''

def getsegments(data, event, segments):
    nlist = []
    for i in range(len(data)):
        if data[i]['event'] == event:
            nlist.append(data[i]['properties'])

    # run once
    d = {event: {}}
    # run at the start of every loop
    newd = d[event]
    for i in range(len(nlist)):
        for k in range(len(segments)):
            key = nlist[i][segments[k]]
            if k == len(segments)-1:
                if key not in newd:
                    newd[key] = 0
                newd[key] += 1
            else:
                if key not in newd:
                    newd[key] = {}
            newd = newd[key]
        newd = d[event]
    d[event] = newd
    return d

data = [{'properties': {'item_id': 876, 'hair': 'brown', 'gender': 'M', 'city': 'NYC', 'value': 23}, 'event': 'Purchase'}, {'properties': {'hair': 'green', 'gender': 'M', 'city': 'NYC', 'origin': 'twitter'}, 'event': 'Signup'}, {'properties': {'item_id': 876, 'hair': 'blue', 'gender': 'M', 'city': 'SF', 'value': 20}, 'event': 'Purchase'}, {'properties': {'item_id': 123, 'hair': 'red', 'gender': 'F', 'city': 'SF', 'value': 55}, 'event': 'Purchase'}, {'properties': {'hair': 'brown', 'gender': 'F', 'city': 'NYC', 'origin': 'google'}, 'event': 'Signup'}, {'properties': {'hair': 'purple', 'gender': 'F', 'city': 'NYC', 'origin': 'twitter'}, 'event': 'Signup'}, {'properties': {'hair': 'brown', 'gender': 'M', 'city': 'Oakland', 'origin': 'google'}, 'event': 'Signup'}, {'properties': {'hair': 'blond', 'gender': 'F', 'city': 'NYC', 'origin': 'google'}, 'event': 'Signup'}, {'properties': {'item_id': 123, 'hair': 'red', 'gender': 'M', 'city': 'Oakland', 'value': 55}, 'event': 'Purchase'}]
print(getsegments(data, 'Signup', ['city', 'gender', 'origin']))
