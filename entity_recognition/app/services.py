def recognize_entities(text):
    return [{"entity": text.split()[0], "label": "PRODUCT"}]
