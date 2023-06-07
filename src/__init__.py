from urllib.request import urlopen
from urllib.parse import quote

from .get_aggregated_html_pron import get_aggregated_html_pron

from aqt import mw
from aqt.qt import QAction
from aqt.utils import qconnect



config = mw.addonManager.getConfig(__name__)
api_key = config['key']
notes_info = config['notes_info']


def transcript_by_filter(search_string) -> None:
    notes = [mw.col.get_card(card_id).note() for card_id in list(mw.col.find_cards(search_string))]

    for note in notes:
        note_type = note.note_type()['name']
        if note_type in notes_info:
            note_info = notes_info[note_type]
            word = note[note_info['word_field']]
            try:
                with urlopen('https://www.dictionaryapi.com/api/v3/references/learners/json/' + quote(word) + '?key=' + api_key) as f:
                    html_pron = get_aggregated_html_pron(word, f.read())
            except:
                html_pron = ''
            if note[note_info['ipa_field']] != html_pron:
                note[note_info['ipa_field']] = html_pron
                mw.col.update_note(note)



transcript_all_action = QAction("(nw_ipa) transcript all", mw)
qconnect(transcript_all_action.triggered, lambda : transcript_by_filter(''))
mw.form.menuTools.addAction(transcript_all_action)

transcript_new_action = QAction("(mw_ipa) transcript new", mw)
qconnect(transcript_new_action.triggered, lambda : transcript_by_filter('is:new'))
mw.form.menuTools.addAction(transcript_new_action)