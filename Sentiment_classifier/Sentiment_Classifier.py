# This is a simple sentiment classifier using fake tweets. The results obtained are saved in .\Results.csv.


punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())


def strip_punctuation(word):
    for pc in punctuation_chars:
        if pc in word:
            word = ''.join(word.split(pc))
    return word


def get_neg(sentence):
    count = 0
    lines = sentence.split()
    for words in lines:
        if strip_punctuation(words).lower() in negative_words:
            count += 1
    return count


def get_pos(sentence):
    count = 0
    lines = sentence.split()
    for words in lines:
        if strip_punctuation(words).lower() in positive_words:
            count += 1
    return count


twit_file = open("project_twitter_data.csv", "r")
lines = twit_file.readlines()[1:]

tweet_text = ''
retweet_count = 0
reply_count = 0
neg_count = 0
pos_count = 0
net_score = 0

result = ''

# ['tweet_text,retweet_count,reply_count\n']

with open('resulting_data.csv', 'w') as result_file:
    result_file.write(
        'Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score\n')
    for line in lines:
        line = line.strip().split(',')
        tweet_text = line[0]
        retweet_count = str(line[1])
        reply_count = str(line[2])
        neg_count = get_neg(tweet_text)
        pos_count = get_pos(tweet_text)
        net_score = pos_count - neg_count
# num_retweets,Num_Replies,Pos,Neg,net
        result = '{},{},{},{},{}'.format(
            retweet_count, reply_count, pos_count, neg_count, net_score)
        result_file.write(result)
        result_file.write('\n')

        #print('''tweet text: {}.\n retweet_count = {}\n reply_count = {}\n neg_count = {}\n pos_count = {}\n net_score = \n\n'''.format(tweet_text,retweet_count,reply_count,neg_count,pos_count,net_score))

twit_file.close()
