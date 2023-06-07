import json

from .get_filtered_pron_pairs import get_filtered_pron_pairs



def unite_pron_pairs(pron_pairs):
    if len(pron_pairs) == 0:
        return None
    
    max_pair_len = max(len(pair.prons) for pair in pron_pairs)
    if max_pair_len == 1:
        if len(set(json.dumps(list(pair.prons.values())) for pair in pron_pairs)) == 1:
            return {'*': list(pron_pairs[0].prons.values())[0]}

        bodies = [list(pair.prons.values())[0] for pair in pron_pairs]
        if max(len(body) for body in bodies) != 1:
            raise Exception('unhandled pron_pairs unition case')
        bodies = [body[0] for body in bodies]
        if max(len(body) for body in bodies) != 2:
            raise Exception('unhandled pron_pairs unition case')
        for body in bodies:
            if not(set(body.keys()) <= set(['ipa', 'sound'])):
                raise Exception('unhandled pron_pairs unition case')
        subres = {}
        for body in bodies:
            for key, val in body.items():
                if key in subres:
                    if json.dumps(subres[key]) != json.dumps(val):
                        raise Exception('unhandled pron_pairs unition case')
                else:
                    subres[key] = val
        return {'*': [subres]}


    if max_pair_len == 1:
        res = {}
        for pair in pron_pairs:
            for key, val in pair.prons.items():
                if key in res:
                    if json.dumps(res[key]) != json.dumps(val):
                        raise Exception('unhandled pron_pairs unition case')
                else:
                    res[key] = val
        return res



def get_aggregated_pron_pairs(word, response_body):
    pairs = get_filtered_pron_pairs(word, response_body)

    try:
        subres = unite_pron_pairs(pairs)
        if subres is None:
            return None
        return {'*': subres}
    
    except:
        res = {}
        for pair in pairs:
            if pair.inner_path[-1].meaning != 'hwi':
                raise Exception('unhandled aggregation case')
        for pair in pairs:
            if 'fl' not in pair.inner_path[-2].subbody:
                raise Exception('unhandled aggregation case')
            if pair.inner_path[-2].subbody['fl'] not in res:
                res[pair.inner_path[-2].subbody['fl']] = []
            res[pair.inner_path[-2].subbody['fl']].append(pair)
        if len(res) != 2:
            raise Exception('unhandled aggregation case')
        for key, val in res.items():
            res[key] = unite_pron_pairs(val)
        return res