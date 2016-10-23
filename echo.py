from gene import Genes as G
from random import random
import math

class Ecosystem:
    def __init__(self, option):
        self.generation = 0
        self.parent_count = 2
        self.gene_count   = option["gene_count"]
        self.gene_length  = option["gene_length"]
        self.mutation_probability  = option["mutation_probability"]
        self.gene_list = self.initialize_gene()
        self.parents = []
        self.who_parents()
        self.none_parents_delete()

    #유전자 생성
    def initialize_gene(self):
        gene_list = []
        for i in range(self.gene_count):
            while True:
                temp = int(random()* math.pow(10 ,self.gene_length))
                if len(str(temp)) == self.gene_length:
                    g = G(temp)
                    gene_list.append(g)
                    break

        return gene_list


    #부모 유전자 선택
    def who_parents(self):
        self.parents = []
        for i in range(self.parent_count):
            temp = G(0)
            for j in range(self.gene_count):
                try:
                    if int(temp.similar) < int(self.gene_list[j].similar) and not self.gene_list[j] in self.parents and len(self.gene_list[j].status) ==self.gene_length:
                        temp = self.gene_list[j]
                except:
                        temp = self.gene_list[j]

            self.parents.append(temp)


    #부모 유전자를 제외하고 제거
    def none_parents_delete(self):
        success_gene_count = 0

        for index, item in enumerate(self.gene_list):
            if item.similar == 6:
                success_gene_count += 1
            else :
                del item
                self.gene_list[index] = None

        self.gene_list = [i for i in self.gene_list if i is not None]


    #다음 세대
    def next_generation(self):
        self.match()
        self.show()
        self.who_parents()
        self.none_parents_delete()
        self.generation += 1


    def show(self):
        for i in self.gene_list:
            print(i.status, i.similar)


    #상위 유전자 교배
    def match(self):
        temp = ''
        for o in range(len(self.gene_list), self.gene_count):
            for i in range(self.gene_length):
                r =random()
                mutation = random()
                if mutation < self.mutation_probability :
                    try:
                        temp += str(int(mutation * 100)%10)
                    except :
                        temp += 1
                else :
                    if r > 0.5 :
                        temp += str(self.parents[0].status)[i]
                    else:
                        temp += str(self.parents[1].status)[i]
            g = G(int(temp))

            temp = ''
            self.gene_list.append(g)



    # 다음 세대로 갈지 말지 결정
    def is_continue(self):
        s = True

        if len(self.gene_list ) ==30 :
            s  = False

        return s
