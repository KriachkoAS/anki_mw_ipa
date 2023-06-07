import html

from .get_aggregated_pron_pairs import get_aggregated_pron_pairs



def get_html_pron_pair(aggregated_pron_pair):
    for key in ['*', 'altprs', 'prs']:
        if key in aggregated_pron_pair.keys():
            chosen_key = key
            break

    for sub_pron in aggregated_pron_pair[chosen_key][:-1]:
        if 'pun' not in sub_pron:
            sub_pron['pun'] = ','

    res = '\\'
    for sub_pron in aggregated_pron_pair[chosen_key]:

        if 'l' in sub_pron:
            res += '<i>' + sub_pron['l'] + '</i>'
        res += sub_pron['ipa']
        if 'l2' in sub_pron:
            res += '<i>' + sub_pron['l2'] + '</i>'

        if 'pun' in sub_pron:
            res += sub_pron['pun'] + ' '
        
    return res + '\\'



def get_aggregated_html_pron(word, response_body):
    aggregated_pron_pairs = get_aggregated_pron_pairs(word, response_body)
    if len(aggregated_pron_pairs) == 1:
        return get_html_pron_pair(list(aggregated_pron_pairs.values())[0])
    
    res = '<ul style="list-style-type: none;" class="ipa_ul">'
    keys = list(aggregated_pron_pairs.keys())
    keys.sort(key = lambda x: x == 'adjective')
    keys.sort(key = lambda x: x == 'adverb')
    keys.sort(key = lambda x: x != 'noun')
    keys.sort(key = lambda x: x == 'verb')

    for key in keys:
        res += '<li><b>' + key + '</b></li><ul style="list-style-type: none;"><li>' + get_html_pron_pair(aggregated_pron_pairs[key]) + '</li></ul>'
    return res + '</ul>'