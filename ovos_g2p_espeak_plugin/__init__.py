from espeak_phonemizer import Phonemizer
from ovos_plugin_manager.g2p import Grapheme2PhonemePlugin
from ovos_utils import flatten_list


class EspeakPhonemesPlugin(Grapheme2PhonemePlugin):

    def __init__(self, config=None):
        super().__init__(config)
        self.pho = Phonemizer()

    def get_ipa(self, word, lang, ignore_oov=False):
        if lang not in self.get_languages():
            lang = lang.split("-")[0]
        phones = self.pho.phonemize(word, phoneme_separator="_", voice=lang)
        words = phones.split(" ")
        return flatten_list([w.split("_") + ["."] for w in words])[:-1]

    @staticmethod
    def get_languages():
        return {'af', 'am', 'an', 'ar', 'as', 'az', 'ba', 'be', 'bg', 'bn', 'bpy',
                'bs', 'ca', 'chr-US-Qaaa-x-west', 'cmn', 'cmn-latn-pinyin', 'cs',
                'cv', 'cy', 'da', 'de', 'el', 'en-029', 'en-gb', 'en-gb-scotland',
                'en-gb-x-gbclan', 'en-gb-x-gbcwmd', 'en-gb-x-rp', 'en-us', 'en-us-nyc',
                'eo', 'es', 'es-419', 'et', 'eu', 'fa', 'fa-latn', 'fi', 'fr-be', 'fr-ch',
                'fr-fr', 'ga', 'gd', 'gn', 'grc', 'gu', 'hak', 'haw', 'he', 'hi', 'hr',
                'ht', 'hu', 'hy', 'hyw', 'ia', 'id', 'io', 'is', 'it', 'ja', 'jbo', 'ka',
                'kk', 'kl', 'kn', 'ko', 'kok', 'ku', 'ky', 'la', 'lb', 'lfn', 'lt', 'ltg',
                'lv', 'mi', 'mk', 'ml', 'mr', 'ms', 'mt', 'my', 'nb', 'nci', 'ne', 'nl',
                'nog', 'om', 'or', 'pa', 'pap', 'piqd', 'pl', 'pt', 'pt-br', 'py', 'qdb',
                'qu', 'quc', 'qya', 'ro', 'ru', 'ru-lv', 'sd', 'shn', 'si', 'sjn',
                'sk', 'sl', 'smj', 'sq', 'sr', 'sv', 'sw', 'ta', 'te', 'th', 'tk', 'tn',
                'tr', 'tt', 'ug', 'uk', 'ur', 'uz', 'vi', 'vi-vn-x-central',
                'vi-vn-x-south', 'yue'}

    @property
    def available_languages(self):
        """Return languages supported by this G2P implementation in this state
        This property should be overridden by the derived class to advertise
        what languages that engine supports.
        Returns:
            set: supported languages
        """
        return self.get_languages()


# sample valid configurations per language
# "display_name" and "offline" provide metadata for UI
# "priority" is used to calculate position in selection dropdown
#       0 - top, 100-bottom
# all keys represent an example valid config for the plugin
EspeakG2PConfig = {
    l: [
        {"lang": l,
         "display_name": f"Espeak G2P",
         "priority": 60,
         "native_alphabet": "IPA",
         "durations": False,
         "offline": True}
    ] for l in EspeakPhonemesPlugin.get_languages()
}

if __name__ == "__main__":
    from pprint import pprint

    pprint(EspeakG2PConfig)
