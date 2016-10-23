class Genes():
    def __init__(self, status):
        self.status = status
        self.similar = 0
        self.what_similar()


    def what_similar(self):
        '''
            111111 6자리
        '''
        for i in str(self.status):
            if i == '1':
                self.similar += 1

    def __del__(self):
        print(self.status, '사망')
