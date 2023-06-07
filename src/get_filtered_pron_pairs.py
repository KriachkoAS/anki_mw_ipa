import json

from .get_pron_pairs import get_pron_pairs, Pron_pair



def _get_get_pron_pair_words():
    uncomplicated_container_word_fields = {
        "hwi": "hw",
        "ins": "if",
        "uros": "ure",
        "vrs": "va",
        "cats": "cat",
        "dros": "drp"
    }
  
    def get_pron_pair_words(self):
        strs_inner_path = tuple(struct.meaning for struct in self.inner_path)
        if strs_inner_path[-1] in uncomplicated_container_word_fields:
            if isinstance(self.inner_path[-1].subbody, list):
                return [value for (meaning, value) in self.inner_path[-1].subbody.items() if meaning == uncomplicated_container_word_fields[strs_inner_path[-1]]]
          
            elif isinstance(self.inner_path[-1].subbody, dict):
                if uncomplicated_container_word_fields[strs_inner_path[-1]] in self.inner_path[-1].subbody:
                    return [self.inner_path[-1].subbody[uncomplicated_container_word_fields[strs_inner_path[-1]]]]
                raise Exception("word of pron_pair is not found")

            else:
                raise Exception("unsupported response document structure")
      
        elif strs_inner_path == ('doc', 'def', 'sseq', 'sense') or strs_inner_path == ('doc', 'def', 'sseq', 'sen'):
            if 'hwi' in self.inner_path[0].subbody:
                if 'hw' in self.inner_path[0].subbody['hwi']:
                    return [self.inner_path[0].subbody['hwi']['hw']]
            raise Exception("word of pron_pair is not found")
      
        else:
            raise Exception("unsupported pron_pair.inner_path word extraction", strs_inner_path)


    return get_pron_pair_words
Pron_pair.get_pron_pair_words = _get_get_pron_pair_words()



def get_filtered_pron_pairs(word, response_body, filter_function = lambda word, pron_pair: word in [pair_word.replace('*', '') for pair_word in pron_pair.get_pron_pair_words()]):
    return [pair for pair in get_pron_pairs(json.loads(response_body)) if filter_function(word, pair)]