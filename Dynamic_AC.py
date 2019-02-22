import math
from collections import defaultdict
import numpy as np 

class Dynamic_AC:
    # initialize class variables
    def __init__(self, patterns, text):
        self.patterns = patterns 	#input patterns
        self.text = text			#input text
        self.g = defaultdict(tuple)	#alpha string
        self.f = defaultdict(tuple)	#omega string
        self.output = {}	
        self.occurences = {}	# No. of occurances of pattern
        self.comparisons = 0 	#Comparision COunter
        self.skipcount = 0		#Skip Counter
		P0 = [len(pattern) for pattern in self.patterns] # array of keyword lengths

    def run(self):
        self._goto(self.patterns)
        self._failure()
        self._match()
        return

    def _match(self):
        state = 0
		Set = [] # set of P
		P = [] # array of pattens
		n = len(self.text) # integer representing text length
		
		m = len(self.patterns) # number of patterns
        for i in range(n):
			P = P0 # init pointer like variable
			Set = Set.append(P)
			
            if ((state, self.text[i]) in self.g) and (Pj in Set):
                state = self.f[state]
                self.comparisons += 1 
                self.skipcount += 1   

            state = self.g[state, self.text[i]]
            if state in self.output:
                l = list(self.output[state])
                for p in l:
                    self.occurences[p] += 1 # updating the occurrence counter

            self.comparisons += 1 # updating the comparison counter
        return
			

    def _goto(self, patterns):
        newstate = 0
		level = dict()
		num_patterns = len(self.patterns)
		n_index = 0 # string index
		first_loop = 1 # first loop
		index_pattern = dict() # index of patterns
        for i in range(1,max(P0):
			a = str(i)
			level[a] = [pattern[i] for pattern in patterns]
			unq, unq_idx, unq_cnt = np.unique(level[a], return_inverse=True, return_counts=True)
			cnt_mask = unq_cnt > 1
			dup_ids = unq[cnt_mask]
			dup =[]
			for index in range(len(level[a])):#traversing thro length of the list
				for j in range(len(dup_ids)):
					if level[a][index] == dup_ids[j]:
						dup.append(index)
						for duplicates in range(len(dup)):
		for i,j in range(1,len(patterns)):
				
		return

    # builds the failure transitions
	
	def level(self,pattern):
		
    
    def getPatternOccurences(self):
        return self.occurences

    def getComparisons(self):
        return self.comparisons
		
    def printResults(self):
        print('\n')
        print('Patterns inputed   : ' + str(self.patterns))
        print('Text inputed       : ' + str(self.text))
        print('\n\t ---------------------- \n')
        print('Comparisons counted: ' + str(self.comparisons))
        print('Pattern occurrences : ' + str(self.occurences))
        print('\n')


