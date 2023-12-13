import spacy


def recognize_entities(text):
    # Load the spaCy English NER model
    nlp = spacy.load("en_core_web_sm")

    # Process the text with spaCy NER
    doc = nlp(text)

    # Extract entities and their labels
    entities = [{"entity": ent.text, "label": ent.label_} for ent in doc.ents]

    return entities


# Example usage:
text_to_analyze = "Apple is a technology company, and iPhone is a popular product."
result = recognize_entities(text_to_analyze)

print(result)
