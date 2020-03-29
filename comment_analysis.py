import json
import sys
import re
import argparse


def user_count_tsv(yt_cmt_tsv):
    with open(yt_cmt_tsv) as tsv:
        user_numbers = {int(re.sub('\t.*\n', '', line)) for line in tsv}
        return len(user_numbers)


def user_count_ngram(yt_cmt_tsv, txtfile):
    with open(yt_cmt_tsv) as tsv, open(txtfile) as txt:
        ngram_set = {re.sub('[^a-zA-z }]', ' ', ngram.rstrip())
                     for ngram in txt}
        line_set = {line for line in tsv}
        ngram_cmt_set = {line for ngram in ngram_set
                         for line in line_set if ngram in line}
        unique_ngram_user_count = len({re.sub('\t.*\n', '', ngram_cmt)
                                       for ngram_cmt in ngram_cmt_set})
        return unique_ngram_user_count


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("tsvfile", help="The TSV file of which you "
                        "want the amount of unique users who mentioned"
                        "certain n-grams", type=str)
    parser.add_argument("ngramfile", help="The TXT file which contains "
                        "n-grams about a certain subject", type=str)

    args = parser.parse_args()
    unique_user_count = user_count_tsv(args.tsvfile)
    unique_ngram_user_count = user_count_ngram(args.tsvfile, args.ngramfile)
    print("Amount of unique users: {0}".format(unique_user_count))
    print("Amount of unique users talking about n-grams in "
          "'{0}': {1}".format(args.ngramfile, unique_ngram_user_count))
    print("Amount of unique users not talking about n-grams in "
          "'{0}': {1}".format(args.ngramfile,
                              unique_user_count - unique_ngram_user_count))


if __name__ == "__main__":
    main()
