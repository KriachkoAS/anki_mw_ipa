doc_struct = {
    "ahws" : {
        "type": "obj_list",
        "occur": ["doc"]
    },
    "cats" : {
        "type": "obj_list",
        "occur": ["ca"]
    },
    "ca" : {
        "type": "obj",
        "occur": ["dt"]
    },
    "dt" : {
        "type": "item_list",
        "occur": ["sense", "sdsense"]
    },
    "sense" : {
        "type": "obj",
        "occur": ["sseq", "pseq", "bs"]
    },
    "sseq" : {
        "type": "item_matr",
        "occur": ["def"]
    },
    "def" : {
        "type": "obj_list",
        "occur": ["doc", "dros"]
    },
    "dros" : {
        "type": "obj_list",
        "occur": ["doc"]
    },
    "pseq" : {
        "type": "item_list",
        "occur": ["sseq"]
    },
    "bs" : {
        "type": "obj",
        "occur": ["sseq", "pseq"]
    },
    "hwi" : {
        "type": "obj",
        "occur": ["doc"]
    },
    "ins" : {
        "type": "obj_list",
        "occur": ["doc", "sdsense", "sen", "sense", "uros"]
    },
    "sdsense" : {
        "type": "obj",
        "occur": ["sense"]
    },
    "sen" : {
        "type": "obj",
        "occur": ["sseq"]
    },
    "uros" : {
        "type": "obj_list",
        "occur": ["doc"]
    },
    "ri" : {
        "type": "item_list",
        "occur": ["dt", "et_snote", "snote", "uns"]
    },
    "et_snote" : {
        "type": "item_matr",
        "occur": ["et"]
    },
    "et" : {
        "type": "item_list",
        "occur": ["doc", "dros", "sdsense", "sen", "sense"]
    },
    "snote" : {
        "type": "item_list",
        "occur": ["dt"]
    },
    "uns" : {
        "type": "item_matr",
        "occur": ["dt", "utxt"]
    },
    "utxt" : {
        "type": "item_list",
        "occur": ["uros"]
    },
    "vrs" : {
        "type": "obj_list",
        "occur": ["doc", "dros", "ri", "sdsense", "sen", "sense", "uros"]
    },
    "doc" : {
        "type": "obj_list",
        "occur": []
    }
}