# N-gram Counter for YouTube comments

This is the repository with programs and files used to analyse YouTube comments. The programs will allow you to count how many unique users mentions a certain n-gram within their comment.

--------------------------------------------------------

data_clear.py preprocesses data sets containing data and meta-datapresented as JSON files. The JSON files of YouTube comments can be obtained through a program written by @egbertbouman and @Daruko0 (https://github.com/egbertbouman/youtube-comment-downloader/blob/master/downloader.py). The comments within the JSON file need to be presented as such, with every comment on a different line and according to the programm of @ebertbouman and @Daruko0:
{"cid": "comment ID", "text": "Content of Comment", "time": "When Comment was Posted", "author": "Name", "votes": "Amount of Votes", "photo": "URL to image of User"}

All the unique URLs will be replaced with a numeric value, to indicate a unique user, since all commenters have a unique image URL. The content of the comment will be cleaned, this means that all non-numerical, non-alphabetical and non-space characters will be replaced with a space.

To run the program, you have to enter the following line in your terminal, followed by the JSON file. After this, the file was sorted and put into a TSV file.
python3 data_cleaner.py jsonfile.json | sort -n > tsvfile.tsv

The TSV file will look as following (these are examples and are not real comments, they show how the TSV file will look):
0	this is my comment
1	what s the deal with airplane food
1	pls like my airplane joke
2	1 55 is my favourite part
...
12303	i dislike this video

--------------------------------------------------------

comment_analysis.py takes a TSV file (see above) and counts how many unique users commented, how many unique users mentioned certain n-grams within their comment and how many unique users did not mention the n-grams within their comment. The n-gram file has to be a TXT file with every n-gram on a different line. gun_violence_related_ngrams.txt shows the ngrams used in our research.

To run the program, you have to type the following line, with tsvfile.tsv as your TSV file and ngramfile.txt as your file with n-grams:
python3 cmnt_analysis.py tsvfile.tsv ngramfile.txt
