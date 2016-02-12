# Part A - Step 2
# Names: 
# - Sebastiaan Joustra (10516999)
# - Joeri Bes (10358234)
# - Bram Smit (10666656)

from __future__ import division
from collections import Counter
import argparse
import pprint
import itertools
from heapq import nsmallest

# Make a dictionary of ngrams based on the corpus and value n
def make_ngrams(corpus, n):
    with open(corpus, 'r') as corpus_txt:
        word_list = ['<s>']
        for line in corpus_txt:
            line = line.split()
            if line == [] and word_list[-1] != "<s>":
                line = ['</s>', '<s>']
            word_list.extend(line)

    ngrams = list(zip(*[word_list[i:] for i in range(n)]))

    # Make a new list filtering out the start/end tags and only looking at the sentences.
    ngrams_filtered = [item for item in ngrams if '<s>' not in item[1:] and '</s>' not in item[0:-2]]

    return Counter(ngrams_filtered)

# Calculate the probabilities of the sentences in an additional given file
def prob_conditional(conditional_prob_file, n, ngrams, ngrams_min1,count):
    prob_dict = {}
    with open(conditional_prob_file, 'r') as prob_txt:
        for line in prob_txt:
            sequence = line.split()
            if len(sequence) == n:
                sequence_min1 = tuple(sequence[0:-1])
                sequence = tuple(sequence)
                last_word = sequence[-1]

                prob_n = ngrams[sequence] / count 
                prob_n_min1 = ngrams_min1[sequence_min1] / count
                if(prob_n_min1 != 0):
                    prob = prob_n / prob_n_min1
                else:
                    prob = 0

                prob_dict[sequence] = prob
    return prob_dict

# Prints the probabilities of a given sequence file, for every line in that file
def prob_sequence(sequence_prob_file, n, ngrams, count, corpus):
    ngrams_collection = []

    for x in range(1,n):
        ngrams_collection.append(make_ngrams(corpus, x))
    ngrams_collection.append(ngrams)

    with open(sequence_prob_file, 'r') as prob_txt:
        for line in prob_txt:
            sequence = line.split()
            prob = calc_sentence_prob(corpus, ngrams_collection, sequence, n)
            
            print("{0} : {1}".format(' '.join(sequence), prob))

# Calculates and returns the probability of a given sequence with n
def calc_sentence_prob(corpus, ngrams_collection, sequence, n):
    j = -100
    m = len(sequence)
    prob_list = []
    for i in range(1,m+2):
        tail = []
        part_sequence = []
        num = 1
        # Add stop tag
        if(i == m+1):
            last_word = "</s>"
        else:
            last_word = sequence[i-1]
        
        while(j != i-1):
            j = i-n+num
            # Add start tag
            if(j==0):
                tail.append("<s>")
            if(j>0):
                tail.append(sequence[j-1])
            num+=1
        part_sequence = tuple(tail + [last_word])

        # Calculate
        ngrams_part_seq = ngrams_collection[len(part_sequence)-1]
        ngrams_tail = ngrams_collection[len(tail)-1]

        prob_seq = ngrams_part_seq[part_sequence] / count                

        prob_tail = ngrams_tail[tuple(tail)] / count

        # Prevent division by zero
        if(prob_tail != 0):            
            prob = prob_seq / prob_tail
            prob_list.append(prob)
        else:
            prob = 0
    total = 1
    for prob in prob_list:
        total *= prob

    return total

# Returns the permutation with the highest probability
def calc_perm(perm_list, n, corpus):
    ngrams_collection = []
    perm_prob_dict = {}

    for x in range(1,n):
        ngrams_collection.append(make_ngrams(corpus, x))
    ngrams_collection.append(ngrams)

    for perm in perm_list:
        prob = calc_sentence_prob(corpus, ngrams_collection, perm, n)
        perm_prob_dict[perm] = prob

    perm_prob_counter = Counter(perm_prob_dict)
    most_common = perm_prob_counter.most_common(2)
    return most_common
    


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-corpus", type=str, help="Corpus used for making n-grams", default = "austen.txt")
    parser.add_argument("-n", type=int, help="Length of n-grams", default = 2)
    parser.add_argument("-m", type=int, help="Return m most common n-grams", default = 10)
    parser.add_argument("-conditional_prob_file", type=str, help="additional conditional file", default="test.txt")
    parser.add_argument("-sequence_prob_file", type=str, help="additional sequence file", default="test.txt")
    args = parser.parse_args()

    ngrams = make_ngrams(args.corpus, args.n)
    count = len(ngrams)
    ngrams_min1 = make_ngrams(args.corpus, args.n-1)
    count_min1 = len(ngrams_min1)
    most_common = ngrams.most_common(args.m)
    most_common_min1 = ngrams_min1.most_common(args.m)

    prob_cond = prob_conditional(args.conditional_prob_file, args.n, ngrams, ngrams_min1, count)
    
    # Print input arguments
    print("--Input-----------")
    print("corpus = {0}".format(args.corpus))
    print("n = {0}".format(args.n))
    print("Additional confitional prob file = {0}".format(args.conditional_prob_file))
    print("Additional sequence prob file = {0}".format(args.sequence_prob_file))
    print("\n--Results---------")

    # Print results of step 2.1
    print("\nStep 2.1")
    print("amount of n-grams = {0}".format(count))
    print("{0} most common:".format(args.m))
    for c in most_common:
        print("{0} : {1}".format(' '.join(c[0]), c[1]))

    print("\n--(n-1)-grams-----")
    print("amount of (n-1)-grams = {0}".format(count_min1))
    print("{0} most common:".format(args.m))
    for c in most_common_min1:
        print("{0} : {1}".format(' '.join(c[0]), c[1]))

    # Print results of step 2.2
    print("\n\n--Step 2.2------")
    print("\n--Probabilities of sequences---")
    for key, value in prob_cond.items():
        key = list(key)
        print("P({0}|{1}) : {2}".format(key[-1], ' '.join(key[0:-1]), value))

    # Print results of step 2.3
    print("\n\n--Step 2.3-----")
    print("--Sentences : probability----")    
    prob_seq = prob_sequence(args.sequence_prob_file, args.n, ngrams, count, args.corpus)

    a = ["know", "I", "opinion", "do", "be", "your", "not", "may", "what"]
    b = ["I", "do", "not", "know"]

    a_perm = list(itertools.permutations(a))
    b_perm = list(itertools.permutations(b))
    most_common_a = calc_perm(a_perm, 2, args.corpus)
    most_common_b = calc_perm(b_perm, 2, args.corpus)

    # Print results of step 2.4
    print("\n\n--Step 2.4-----")
    print("--Highest probabilities of the sets:")
    print("\nset a:")
    for c in most_common_a:
        print("{0} : {1}".format(' '.join(c[0]), c[1]))

    print("\nset b:")
    for c in most_common_b:
        print("{0} : {1}".format(' '.join(c[0]), c[1]))