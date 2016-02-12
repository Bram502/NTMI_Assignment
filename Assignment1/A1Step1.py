"""
file: a11.py
author: Eelco van der Wel
date: 05-02-2016
 
Assignment 1 step A for the NTMI 2016 course.
A script to generate ngrams from a corpus of text.
 
This script works for both python 2.7 and python 3.
"""
 
from collections import Counter
import argparse
 
def make_ngrams(corpus, n):
    """
    Return a Counter of ngrams <ngram>:<frequency> where an ngram is
    a tuple of n words, and the total number of ngrams in the corpus.
 
    corpus  --  The path to the txt file containing the corpus.
    n       --  length of the n-grams.
    """
 
    # Split corpus into a list of words.
    with open(corpus, 'r') as corpus_txt:
        word_list = [word for line in corpus_txt for word in line.split()]
 
    # Python magic: * operator unpacks each element of the list as argument
    # for zip, for loop generates n lists each starting on the next word.
    # Note: in python 2.7 the list() does nothing, but it is required in
    # python 3 as zip returns an iterator instead of list.
    ngrams = list(zip(*[word_list[i:] for i in range(n)]))
 
    # Counter is a high performance dictionary made for
    # counting and analyzing frequencies
    return Counter(ngrams), len(ngrams)
 
if __name__ == "__main__":
 
    # Argument parsing
    # Default: n=2, m=10, corpus="austen.txt"
    parser = argparse.ArgumentParser()
    parser.add_argument("-corpus", type=str,
                        help="Corpus used for making n-grams",
                        default = "austen.txt")
    parser.add_argument("-n", type=int, help="Length of n-grams", default = 2)
    parser.add_argument("-m", type=int, help="Return m most common n-grams",
                        default = 10)
    args = parser.parse_args()
 
    # Make n-grams and get m most common n-grams
    ngrams, count = make_ngrams(args.corpus, args.n)
    most_common = ngrams.most_common(args.m)
 
    # Print results
    print("--Input-----------")
    print("corpus = {0}".format(args.corpus))
    print("n = {0}".format(args.n))
    print("--Results---------")
    print("amount of n-grams = {0}".format(count))
    print("{0} most common:".format(args.m))
    for c in most_common:
        print("{0} : {1}".format(' '.join(c[0]), c[1]))