import boto3
import argparse

# command line arguments
parser = argparse.ArgumentParser(description='Translate text to all possible languages supported by Amazon Translate')
parser.add_argument('text_to_translate', default='Xin chào buổi sáng', nargs='?', help='Text to translate (default=\"Hello, World\")')
args = parser.parse_args()
#print(args)

translate = boto3.client("translate")
lang_flag_pairs = [("he", "🇮🇱"), ("fr", "🇫🇷"), ("de", "🇩🇪"),
                   ("es", "🇪🇸"), ("pt", "🇵🇹"), ("zh", "🇨🇳"),
                   ("ja", "🇯🇵"), ("ru", "🇷🇺"), ("it", "🇮🇹"),
                   ("zh-TW", "🇹🇼"), ("tr", "🇹🇷"), ("cs", "🇨🇿")]
for lang, flag in lang_flag_pairs:
    print(flag)
    print(translate.translate_text(
        Text=args.text_to_translate,
        SourceLanguageCode="vi",
        TargetLanguageCode=lang
    )['TranslatedText'])
