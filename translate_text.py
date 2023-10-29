from googletrans import Translator

translator = Translator()

def translate_to_en(lang, text):
    translated = translator.translate(text, src=lang, dest='en')
    return translated.text

def translate_to_lang(lang, text):
    translated = translator.translate(text, src='en', dest=lang)
    return translated.text
