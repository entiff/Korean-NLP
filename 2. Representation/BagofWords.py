import konlpy.tag


class BagOfWords:

        def __init__(self, sentences, tag_package='Komoran', unk=True):
            self.sentences = sentences
            self.tag_package = tag_package
            self.word2idx = {}
            self.idx2word = {}
            self.unk = unk

            if self.tag_package == 'Hannanum':
                self.tagger = konlpy.tag.Hannanum()
            elif self.tag_package == 'Kkma':
                self.tagger = konlpy.tag.Kkma()
            elif self.tag_package == 'Mecab':
                self.tagger = konlpy.tag.Mecab()
            elif self.tag_package == 'Okt':
                self.tagger = konlpy.tag.Okt()
            else:
                self.tagger = konlpy.tag.Komoran()

        def make_dict(self):
            if self.unk:
                self.word2idx['[UNK]'] = 0
                self.idx2word[0] = '[UNK]'

            for sentence in self.sentences:
                temp_morph_list = self.tagger.morphs(sentence)
                for morph in temp_morph_list:
                    if morph not in self.word2idx:
                        self.word2idx[morph] = len(self.word2idx)
                        self.idx2word[len(self.word2idx)-1] = morph
            return self.word2idx, self.idx2word

        def word_count(self, sentence):
            sentence_morphs = self.tagger.morphs(sentence)
            if self.unk:
                word_count = [0]*len(self.idx2word)
                for morph in sentence_morphs:
                    if morph in self.word2idx.keys():
                        word_count[self.word2idx[morph]] += 1
                    else:
                        word_count[0] += 1
            else:
                for morph in sentence_morphs:
                    if morph not in self.word2idx:
                        self.word2idx[morph] = len(self.word2idx)
                        self.idx2word[len(self.word2idx)-1] = morph
                word_count = [0] * len(self.idx2word)
                for morph in sentence_morphs:
                        word_count[self.word2idx[morph]] += 1

            return word_count



