""" @Author: Aravind Madan Mohan
 """
import csv 
import pathlib
import time
import random
from enum import Enum
from collections import OrderedDict
from structures import ACAuto
from structures import CWAuto
from structures import PFACAuto
import json
from matplotlib import pyplot as plt
import sys 
import tracemalloc
import time
from memory_profiler import profile

TEST_FILE = "corpus/Newfolder"
CORPUS_PREFIX = "article_scraper/articles/"
SHINGLE_CONSTANT = 50
RANDOM = False
OUTFILE_PATH = "outfile.txt"

ac_match_count = 0


##### GENERAL UTILITIES #####

	
class Algorithm(Enum):
	aho_corasick = 0
	commentz_walter = 1
	pfac = 2



##### AHO CORASICK #####

@profile
def build_automaton(shingles, automaton):
	if automaton == Algorithm.aho_corasick :
		a = ACAuto()
		for shingle in shingles:
			a.add_word(shingle)
		a.create_failure_links()
	if automaton == Algorithm.commentz_walter :
		a = CWAuto()
		for shingle in shingles:
			a.add_word(shingle)
		a.create_failure_links()		
	if automaton == Algorithm.pfac :
		a = PFACAuto()
		for shingle in shingles:
			a.add_word(shingle)
		a.links()
	
	return a




	
	
def run_algos(algorithm,shingles,text,file_path):
	length = len(text)
	
	total_matches = 0
	elapsed_time = []
	file = open(file_path, 'w')
	if(algorithm == Algorithm.aho_corasick):
		#print("************************************AHO-CORASICK***********************************************")
		algo = build_automaton(shingles, algorithm)

	if(algorithm == Algorithm.commentz_walter):
		#print("************************************COMMENTZ-WALTER********************************************")
		algo = build_automaton(shingles, algorithm)
	if(algorithm == Algorithm.pfac):
		#print("*****************Parallel Failureless Aho Corasick Single Core ********************************************")
		algo = build_automaton(shingles, algorithm)
		
	for i in range(0,length):
		start_time = time.time()
		total_matches = algo.report_all_matches(str(text[i]))
		algo_sorted = OrderedDict(sorted(total_matches.items()))
		elapsed_time.append(time.time() - start_time)	
		file.write('Elapsed Time = ')
		file.write(str(elapsed_time[i]))
		file.write('\n\n')
		file.write(json.dumps(algo_sorted))
		file.write('\n\n\n')
	file.close()
	#print('Result saved to file')
	return elapsed_time

	
	
if __name__ == '__main__':

	with open('fixed_random_file.csv', newline='\n') as csvfile1:
		shingles = list(csv.reader(csvfile1))
		
	with open('dataset1.csv', newline='\n') as csvfile:
		data = list(csv.reader(csvfile))
		
	file_ac = './Results/AC.txt'
	file_cw = './Results/CW.txt'
	file_pfac = './Results/PFAC.txt'
	
	tracemalloc.start()
	elapsed_time_ac = run_algos(Algorithm.aho_corasick,shingles[0],data,file_ac)
	top_stats = snapshot.statistics('lineno')
 
	for stat in top_stats[:10]:
		print(stat)
	
	elapsed_time_cw = run_algos(Algorithm.commentz_walter,shingles[0],data,file_cw)
	

	elapsed_time_pfac = run_algos(Algorithm.pfac,shingles[0],data,file_pfac)
	
	
	# plt.plot(elapsed_time_ac,label='Aho Corasick')
	# plt.plot(elapsed_time_cw,label='Commentz-Walter')
	# plt.plot(elapsed_time_pfac,label='PFAC')
	# plt.legend()
	# plt.title('Execution time of algorithms for each string input')
	# plt.xlabel('Input Patterns')
	# plt.ylabel('Time in seconds')
	# plt.show()
