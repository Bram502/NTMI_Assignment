################################################################################
#   NTMI COURSE 2016 PART A STEP 3
#   16/02/2016
#   written by;
#       - Sebastiaan Joustra        10516999
#       - Bram Smit                 10666656
#       - Joeri Bes                 10358234 
#
#   Run the program by using the command line like this:
#   ./NTMI_partAstep3.py -train_corpus [path] -test_corpus [path] -n [value]
#
################################################################################

from collections import Counter
import argparse

################################################################################
# contruct a dictionary of the n-grams from the given corpus
################################################################################
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
    
################################################################################    
# returns the probabilities sentences in a test_corpus in a dictionary
################################################################################
def apply_smoothing(test_corpus, n, bigrams, unigrams, vocabulary_size, n_freqs):
    no_smoothing_prob_dict = {}
    add1_smoothing_prob_dict = {}
    first5_list_no_smoothing = []
    first5_list_add1_smoothing = []
    
    with open(test_corpus, 'r') as test_corpus_txt:
        for line in test_corpus_txt:
            sequence = line.split()
            
            prob_list_no_smoothing = []
            prob_list_add1_smoothing = []
            prob_list_turing_smoothing = []
            
            j = -100
            m = len(sequence)
            
            for i in range(1,m+2):
                bigram = []
                unigram = []
                num = 1
                if(i == m+1):
                    last_word = "</s>"
                else:
                    last_word = sequence[i-1]
            
                while(j != i-1):
                    j = i-n+num
                    # Add start tag
                    if(j==0):
                        unigram.append("<s>")           
                    if(j>0):
                        unigram.append(sequence[j-1])
                    num+=1
                bigram = tuple(unigram + [last_word])
                unigram = tuple(unigram)
                
                
                # check for out of vocabulary words
                if (unigram in unigrams and tuple([last_word]) in unigrams):
                    prob_no_smoothing = calc_no_smoothing(bigrams[bigram], unigrams[unigram])
                    prob_add1_smoothing = calc_add1_smoothing(bigrams[bigram], unigrams[unigram], vocabulary_size)
                    prob_list_no_smoothing.append(prob_no_smoothing)
                    prob_list_add1_smoothing.append(prob_add1_smoothing)
                else:
                    prob_list_no_smoothing.append(0)
                    prob_list_add1_smoothing.append(0)
               
               
                # Calculating the Good Turing smoothing probabilities does not work, so it won't be added
                # The program does calculate r*, as explained in the report
                # prob_turing_smoothing = calc_turing_smoothing(bigrams[bigram], unigram[unigram],vocabulary_size, n_freqs)
                # prob_list_turing_smoothing.append(prob_turing_smoothing)
                
            total_prob_no_smoothing = calc_total_prob(prob_list_no_smoothing)
            total_prob_add1_smoothing = calc_total_prob(prob_list_add1_smoothing)
            
            
            # total_prob_turing_smoothing = calc_total_prob(prob_list_turing_smoothing)
                
            no_smoothing_prob_dict[line] = total_prob_no_smoothing
            add1_smoothing_prob_dict[line] = total_prob_add1_smoothing
            

            if (len(first5_list_no_smoothing) < 5 and total_prob_no_smoothing == 0):
                first5_list_no_smoothing.append(line)
            if (len(first5_list_add1_smoothing) < 5 and total_prob_add1_smoothing == 0):
                first5_list_add1_smoothing.append(line)
            
    return no_smoothing_prob_dict, add1_smoothing_prob_dict, first5_list_no_smoothing, first5_list_add1_smoothing

# calculate the total probability of a list of probabilities
def calc_total_prob(prob_list):
    total_prob = 1
    for prob in prob_list:
        total_prob *= prob
    return total_prob

################################################################################
# calculate probabilities for each method
################################################################################
def calc_no_smoothing(bigram_count, unigram_count):
    if(unigram_count != 0):
        prob = (bigram_count / unigram_count)
    else:
        prob = 0
    return prob
    

def calc_add1_smoothing(bigram_count, unigram_count, vocabulary_size):
    return (bigram_count + 1) / (unigram_count + vocabulary_size)

def calc_turing_smoothing(bigram_count, unigram_count, vocabulary_size, n_freqs): 
    
    if(bigram_count == 0):
        prob = n_freqs[1] / total_words
    else:
        if(bigram_count > 0 and bigram_count <= k):
            c_star = calc_c_star(bigram_count, n_freqs)
        else:
            # if c > 5, c* = c
            c_star = bigram_count
        prob = c_star # Formula from remark 2 should be here.
    
    return prob
    
def calc_c_star(count, n_freqs, vocabulary_size, total_words):
    k = 5
    x = (count + 1) * (n_freqs[count+1]/n_freqs[count])
    y = count * (((k+1)*n_freqs[k+1])/n_freqs[1])
    z = 1 - (((k+1)*n_freqs[k+1])/n_freqs[1])
    c_star = (x - y) / z

    return c_star

################################################################################
# calculates N_c, the number of bigrams that occur c times
################################################################################
def frequency_of_frequencies(bigrams, vocabulary_size):
    k = 5
    n_freqs = {}
    for key, value in bigrams.items():
        if(value <= k + 1):
            if(value in n_freqs):
                n_freqs[value] += 1
            else:
                n_freqs[value] = 1
                
    n0 = vocabulary_size ** 2 - len(bigrams)
    n_freqs[0] = n0
    
    print("bigram frequency dict", n_freqs)
    return n_freqs

################################################################################
# calculate the percentage of sentences which are assigned probability zero
################################################################################
def calc_zero_prob_percentage(sentence_probs):
    zero_prob_count = 0
    for key, value in sentence_probs.items():
        if value == 0:
            zero_prob_count+=1
    return zero_prob_count/len(sentence_probs)
    
    
################################################################################
# main function, runs the program and prints results
################################################################################
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-train_corpus", type=str, help="Corpus used for making n-grams", default = "austen.txt")
    parser.add_argument("-n", type=int, help="Length of n-grams", default = 2)
    parser.add_argument("-test_corpus", type=str, help="Test corpus file", default="ja-pers-clean.txt")
    parser.add_argument("-smoothing", type=str, help="Smoothing method used no/add1/gt", default = "no")
    args = parser.parse_args()

    bigrams = make_ngrams(args.train_corpus, args.n)
    unigrams = make_ngrams(args.train_corpus, args.n-1)
    
    vocabulary_size = len(unigrams)
    total_words = len(list(unigrams.elements()))
    
    n_freqs = frequency_of_frequencies(bigrams, vocabulary_size)
    
    no_smoothing_prob_dict, add1_smoothing_prob_dict, first5_list_no_smoothing, first5_list_add1_smoothing = apply_smoothing(args.test_corpus, args.n, bigrams, unigrams, vocabulary_size, n_freqs)
    
    
    zero_prob_no_smoothing = calc_zero_prob_percentage(no_smoothing_prob_dict)
    zero_prob_add1_smoothing = calc_zero_prob_percentage(add1_smoothing_prob_dict)
    
    print("Percentage of sentences with zero probablity for each model:")
    print("No smoothing: " + str(zero_prob_no_smoothing))
    print("Add 1 smoothing: " + str(zero_prob_add1_smoothing))
    
    
    print("first 5 no smoothing:")
    for i in first5_list_no_smoothing:
        print(i)
    
    print("first 5 add1 smoothing:")
    for i in first5_list_add1_smoothing:
        print(i)
    
    # for key, value in no_smoothing_prob_dict.items():
    #     print("{0} : {1}".format(key, value))
    
    # for key, value in add1_smoothing_prob_dict.items():
    #     print("{0} : {1}".format(key, value))
    
    # for key, value in good_turing_smoothing_prob_dict.items():
    #     print("{0} : {1}".format(key, value))

if __name__ == "__main__":
    main()