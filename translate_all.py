import boto3
import argparse

# command line arguments
parser = argparse.ArgumentParser(description='Translate text to all possible languages supported by Amazon Translate')
parser.add_argument('text_to_translate', default='Xin chร o buแปi sรกng', nargs='?', help='Text to translate (default=\"Hello, World\")')
args = parser.parse_args()
#print(args)

translate = boto3.client("translate")
lang_flag_pairs = [("he", "๐ฎ๐ฑ"), ("fr", "๐ซ๐ท"), ("de", "๐ฉ๐ช"),
                   ("es", "๐ช๐ธ"), ("pt", "๐ต๐น"), ("zh", "๐จ๐ณ"),
                   ("ja", "๐ฏ๐ต"), ("ru", "๐ท๐บ"), ("it", "๐ฎ๐น"),
                   ("zh-TW", "๐น๐ผ"), ("tr", "๐น๐ท"), ("cs", "๐จ๐ฟ")]
for lang, flag in lang_flag_pairs:
    print(flag)
    print(translate.translate_text(
        Text=args.text_to_translate,
        SourceLanguageCode="vi",
        TargetLanguageCode=lang
    )['TranslatedText'])
