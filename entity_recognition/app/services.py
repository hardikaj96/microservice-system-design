def recognize_entities(text):
    return [{"entity": text.split()[0] if text else "NULL", "label": "PRODUCT"}]
