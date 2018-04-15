import jieba
import jieba.posseg as pseg

class Word:
    def __init__(self, token, pos):
        self.token = token
        self.pos = pos


class Tagger:
    def __init__(self, dict_paths):
        """load external dict
        :param dict_paths: paths where user dict stored
        """
        for p in dict_paths:
            jieba.load_userdict(p)
        
        # manually adjust frequency to guarentee two words joint
        jieba.suggest_freq(("喜剧", "电影"), True)
        jieba.suggest_freq(('恐怖', '电影'), True)
        jieba.suggest_freq(('科幻', '电影'), True)
        jieba.suggest_freq(('喜剧', '演员'), True)
        jieba.suggest_freq(('出生', '日期'), True)
        jieba.suggest_freq(('英文', '名字'), True)

    @staticmethod
    def get_word_objects(sentence):
        """convert natural language to list of Word object
        :param sentence: string type natural language sentence
        :return: list of Word object
        """
        return [Word(word, tag) for word, tag in pseg.cut(sentence)]


# test
if __name__ == '__main__':
    tagger = Tagger(['./external_dict/movie_title.txt', './external_dict/person_name.txt'])
    while True:
        s = input("Please type in your question: ")
        for i in tagger.get_word_objects(s):
            print (i.token, i.pos)