import xml.etree.ElementTree as ET
import json, codecs
import datetime
import pprint

def parseXML(xmlfile):

    # create element tree object
    tree = ET.parse(xmlfile)

    # get root element
    root = tree.getroot()

    # create empty list for entries items
    entries = []
    id = {}
    lemma = {}
    pos = {}
    gloss = {}

    # iterate entries item
    for entry in root.findall('./ENTRY'):
        id = clean_str_data(entry.find("ID").text)
        lemma = clean_str_data(entry.find("LEMMA").text)

        # empty senses dictionary
        senses = []

        # iterate child elements of senses
        for sense in entry.findall('./SENSES/SENSE'):
            sub_lemmas = []
            for sub_lemma_ex in sense.findall('./SUB-LEMMAS/SL-E'):
                sl_e = clean_str_data(sub_lemma_ex.text)
                if len(sl_e) > 0:
                    sub_lemmas.append(sl_e)

            sense_examples = []
            for sense_example in sense.findall('./EXAMPLES/EXAMPLE-E'):

                example_e_ceb = clean_str_data(sense_example.find("CEB").text,"capitalize")
                example_e_eng = clean_str_data(sense_example.find("ENG").text,"capitalize")

                json_lst = {}
                if len(example_e_ceb) > 0:
                    json_lst["ceb"] = example_e_ceb
                    # sense_examples.append({"ceb": example_e_ceb})
                if len(example_e_eng) > 0:
                    json_lst["eng"] = example_e_eng
                    # sense_examples.append({"eng": example_e_eng})
                sense_examples.append(json_lst)

            gloss = clean_str_data(sense.find("GLOSS").text)
            senses.append({"gloss": gloss, "pos": clean_str_data(sense.get("POS"), "upper"), "sub_lemmas": sub_lemmas, "sense_examples": sense_examples})

        entries.append({"id": id, "lemma": lemma, "senses": senses})
    return entries

def clean_str_data(data, sty="lower"):
    if isinstance(data, str):
        data = data.strip()
    else:
        return data

    if sty == "lower":
        data = data.lower()
    elif sty == "capitalize":
        data = data.capitalize()
    else:
        data = data.upper()
    return data

def saveto_json_file(json_data, filename):
    filename = filename + datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
    with open(filename, 'wb') as handle:
        json.dump(json_data, codecs.getwriter('utf-8')(handle), indent=4, ensure_ascii=False)

def main():
    # parse xml file
    entries = parseXML('ceb_lexicon_304949.xml')
    saveto_json_file(entries, "ceb_lexicon_")

if __name__ == "__main__":

    # calling main function
    main()
