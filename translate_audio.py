import speech_recognition as sr

rec = sr.Recognizer()

def audio_to_text(audio_file_path, lang):
    if(lang == 'ta'):
        wit_api_key = 'E2AIXOVFBHQRPR4Z4RIDTWIEAE37BF2K'
    elif(lang == 'tel'):
        wit_api_key = '4JYU3IBX24YGGUWXHCIZPXX44XWYIBX7'
    elif(lang == 'ch-zh'):
        wit_api_key = '222ZKD5XMBUICCDQ5V6LXHUPPPP6SCPK'
    with sr.AudioFile(audio_file_path) as source:
        audio_data = rec.record(source)
    user_input_raw = rec.recognize_wit(audio_data, key=wit_api_key)
    return user_input_raw
