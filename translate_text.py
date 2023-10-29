from googletrans import Translator

translator = Translator()

def translate_to_en(text):
    lang = translator.detect(text).lang
    translated = translator.translate(text, src=lang, dest='en')
    return translated.text

def translate_to_lang(text):
    lang = translator.detect(text).lang
    translated = translator.translate(text, src='en', dest=lang)
    return translated.text
