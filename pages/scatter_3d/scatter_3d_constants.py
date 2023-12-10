import plotly.graph_objects as go

HOVER_MAP = {'token': True,
             'lemma': True,
             'prediction': True,
             'subtype': True,
             'amyloid_detail': False,
             'csf': False,
             'weight': True,
             'context': True,
             'weight_norm': False,
             'Y': False,
             'X': False,
             'Z': False,
             'alt_pos': True}

NAME_MAP = {'ADJ': 'Adjectives',
            'ADP': 'Adpositions',
            'ADV': 'Adverbs',
            'AUX': 'Auxiliaries',
             'CONJ': 'Conjunctions',
             'CCONJ': 'Coordinating conjunctions',
             'DET': 'Determiners',
             'INTJ': 'Interjections',
             'NOUN': 'Nouns',
             'NUM': 'Numerals',
             'PART': 'Particles',
             'PRON': 'Pronouns',
             'PROPN': 'Proper nouns',
             'PUNCT': 'Punctuation',
             'SCONJ': 'Subordinating conjunctions',
             'SYM': 'Symbols',
             'VERB': 'Verbs',
             'X': 'other',
             'SPACE': 'spaces',
             'EX': "Existential 'there'"}

CAT_MAP = {"AMYLOID_NEG": "Amyloid negative", "AMYLOID_POS": "Amyloid positive"}

# =============================================================================
# NULL RESULTS
# =============================================================================
null_result = {
    "layout": {
        "font": go.layout.Font(
            family="Helvetica",
            color="#000000"),
        "xaxis": {
            "visible": False
        },
        "yaxis": {
            "visible": False
        },
        "annotations": [
            {
                "text": "No matching data found",
                "xref": "paper",
                "yref": "paper",
                "color": "#000000",
                "showarrow": False,
                "font": {
                    "size": 28
                }
            }
        ]
    }
}
