from collections import namedtuple

from .doc_struct import doc_struct



Struct = namedtuple("Struct", ["meaning", "subbody"])
Pron_pair = namedtuple("Pron_pair", ["inner_path", "prons"])



def _get_obj_pairs(body, meaning):
    res = [
        Pron_pair([Struct(meaning, body)] + pair.inner_path, pair.prons)
        for key, val in body.items()
        for pair in get_pron_pairs(val, key)
        ]
    if 'prs' in body or 'altprs' in body:
        res.append(Pron_pair(
            [Struct(meaning, body)],
            {key: body[key] for key in ['prs', 'altprs'] if key in body}
            ))
    return res

def _get_item_list_pairs(body, meaning):
    pair, res = {}, []
    for key, val in body:
        if key == 'prs':
            if 'prs' in pair:
                raise Exception('Double prs')
            pair['prs'] = val
        if key == 'altprs':
            if 'altprs' in pair:
                raise Exception('Double altprs')
            pair['altprs'] = val
        res += [
            Pron_pair([Struct(meaning, body)] + pair.inner_path, pair.prons)
            for pair in get_pron_pairs(val, key)
            ]
    if len(pair) > 0:
        res.append(Pron_pair([Struct(meaning, body)], pair))
    return res



def get_pron_pairs(body, meaning = "doc"):
    if meaning in doc_struct:

        if doc_struct[meaning]["type"] == 'obj':
            return _get_obj_pairs(body, meaning)

        elif doc_struct[meaning]["type"] == 'obj_list':
            return [pair
                    for obj in body
                    for pair in _get_obj_pairs(obj, meaning)]

        elif doc_struct[meaning]["type"] == 'item_list':
            return _get_item_list_pairs(body, meaning)

        elif doc_struct[meaning]["type"] == 'item_matr':
            return [pair
                    for item_list in body
                    for pair in _get_item_list_pairs(item_list, meaning)]

        else:
            raise Exception("unhandled type of json structure unit")
  
    return []