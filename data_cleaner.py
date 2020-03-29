import json
import re
import argparse


def text_user_extract(jsonfile):
    with open(jsonfile) as jf:
        text_photo_list = []
        for cmt in jf:
            text = json.loads(cmt)['text'].lower()
            text = re.sub('[^a-zA-Z0-9 ]', ' ', text)
            text = ' '.join(text.split())
            photo = json.loads(cmt)['photo']
            text_photo_list.append([photo, text])
        user_list = list({text_photo[0] for text_photo in text_photo_list})
        for text_photo in text_photo_list:
            text_photo[0] = text_photo[0].replace(text_photo[0], str(user_list.index(text_photo[0])))
        return text_photo_list


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("commentfile", help="The JSON file with comments "
                        "you want to preprocess and turn into a TSV "
                        "file.", type=str)
    args = parser.parse_args()

    text_user_list = text_user_extract(args.commentfile)
    for text_user in text_user_list:
        print(text_user[0] + '\t' + text_user[1])


if __name__ == "__main__":
    main()
