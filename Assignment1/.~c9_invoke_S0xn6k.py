from collections import Counter
import numpy as np

def main():
    training_data = "WSJ02-21.pos"
    test_data = "WSJ23.pos"
    predicted_test_file = "predicted-test-set.txt"
    
    print("Starting program with input:")
    print("Training data: " + training_data)
    print("Test data: " + test_data)
    print("Output file: " + predicted_test_file)
    
    print("\nParsing training data..")
    state_bigrams, state_frequencies, state_word_frequencies, word_frequencies = parse_training_data(training_data)

    state_list = [x[0] for x,y in state_frequencies.items()]
    vocabulary_size = 
    state_list.remove('<s>')

    
    n_freqs = smooth_language_model(state_bigrams, vocabulary_size)
    
    print("\nCalculating probabilities..")
    transition_probs = calc_transition_probs(False, state_bigrams, state_frequencies)
    emission_probs = calc_emission_probs(False, state_word_frequencies, state_frequencies)
    
    print("\nParsing test data..")
    test_data_word_list = parse_test_data(test_data)
    
    
    
    # print("\nCalculating accuracy of training data compared to real data from test file..")
    # accuracy, all_predicted_sets = iterate_sentences(test_data_word_list, transition_probs, emission_probs, state_list)
    
    # print("\nAccuracy: " + str(accuracy))
    
    # print("\nWriting predicted data to predicted test file" + predicted_test_file)
    # print_to_file(all_predicted_sets, predicted_test_file)
    #print(transition_probs)
    #print(len(word_frequencies))
    # define_hmm(transition_probs, emission_probs)
    # define_hmm()
    
    # most_common = Counter(state_bigrams.most_common(10))
    # for c in most_common:
    #     print("{0} : {1}".format(' '.join(c[0]), c[1]))

    # for key, value in transition_probs.items():
    #     print(key, value)

def smooth_language_model(state_bigrams, vocabulary_size):
    k = 4
    n_freqs = {}
    for key, value in state_bigrams.items():
        if(value <= k + 1):
            if(value in n_freqs):
                n_freqs[value] += 1
            else:
                n_freqs[value] = 1
                
    n0 = vocabulary_size ** 2 - len(state_bigrams)
    
    for key, value in state_bigrams.items():
        if value i

    n_freqs[0] = n0
    

    
    print("bigram frequency dict", n_freqs)
    return n_freqs

def parse_training_data(trainingData):
    state_list = ["<s>"]
    word_list = []
    state_word_list = []
    with open(trainingData, 'r') as data:
        for line in data:
            line = line.split()
            if(len(line) != 0):
                
                temp_state_list = state_bigrams(line, state_list[-1])
                state_list.extend(temp_state_list)
                
                temp_word_list, temp_state_word_list = state_word_frequencies(line)
                word_list.extend(temp_word_list)
                state_word_list.extend(temp_state_word_list)
    
    
    bigrams = Counter(list(zip(*[state_list[i:] for i in range(2)])))
    
    state_frequencies = Counter(list(zip(*[state_list[i:] for i in range(1)])))
    
    del bigrams[('</s>', '<s>')]
    return bigrams, state_frequencies, Counter(state_word_list), Counter(word_list)
    
# Creates the state bigram of the transition model    
def state_bigrams(line, prev_word):
    word_list = [] 
    
    #End of sentence found, add tags
    if(line[0].startswith("=") or line[0] == "./."):
        if(prev_word != "<s>"):
            word_list.append("</s>")
            word_list.append("<s>")
    else:
        for word in line:
            if('/' in word):
                word = word.split('/')
                if(word[-1][0].isalnum()):
                    
                    if('|' in word[-1]):
                        word_list.append(word[-1].split('|')[0])
                    else:
                        word_list.append(word[-1])
                    
    return word_list


# Counts the frequencies of words linked with certain states    
def state_word_frequencies(line):
    word_list = []
    state_word_list = []
    
    for word in line:
        if('/' in word):
            word = word.split('/')
            if(word[-1][0].isalnum()):
                state_word_list.append((''.join(word[0:-1]), word[-1]))
                word_list.append(tuple([''.join(word[0:-1])]))
    
    return word_list, state_word_list
    

# Calculates the transition probability for  the transition model   
def calc_transition_probs(smoothing,  state_bigrams, state_frequencies):
    """
    Data structure looks like this:
    {
    tag1: {'tag32': .005 ,'tag1278': .0033},
    tag2: {'tag566': 1.0, 'tag898': .05}
    }
    """
    
    transition_probs = {}
    if smoothing:
        pass
    else:
        for key, value in state_bigrams.items():
            history = key[0]
            if(history != 0):
                mle = value / state_frequencies[tuple([key[0]])]

                if(history not in transition_probs):
                    transition_probs[history] = {key[1]: mle}
                else:
                    transition_probs[history][key[1]] = mle
    return transition_probs
    
# Used to calculate the probabilities for the Emission model
def calc_emission_probs(smoothing, state_word_frequencies, state_frequencies):
    """
    Data structure looks like this:
    {
    tag1: {'word32': .005 ,'word1278': .0033},
    tag2: {'word566': 0.878, 'word898': .05, 'word9678': .065}
    }
    """
    emission_probs = {}
    if smoothing:
        pass
    else:
        for key, value in state_word_frequencies.items():
            history = key[1]
            if(state_frequencies[tuple([key[1]])] != 0):
                mle = value / state_frequencies[tuple([key[1]])]
                
                if(history not in emission_probs):
                    emission_probs[history] = {key[0]: mle}
                else:
                    emission_probs[history][key[0]] = mle
    return emission_probs
    
def parse_test_data(test_data):
    word_list = ["<s>"]
    with open(test_data, 'r') as data:
        for line in data:
            line = line.split()
            if(len(line) != 0):
                #End of sentence found, add tag
                if(line[0].startswith("=") or line[0] == "./."):
                    if(word_list[-1] != "<s>"):
                        word_list.append("</s>")
                        word_list.append("<s>")
                else:
                    for word in line:
                        if('/' in word):
                            word = word.split('/')
                            if(word[-1][0].isalnum()):
                                word_list.append((word[0], word[-1]))
    return word_list


def iterate_sentences(word_list, transition_probs, total_emission_probs, state_list):
    sentence = []
    tag_sentence = []
    all_predicted_sets = []
    count = 0
    correct = 0
    total = 0
    for word in word_list:
        
        # if(count == 10):
        #     break
        if(word == "</s>"):
            if(len(sentence) != 0 and len(sentence) < 15):

                start_probs, emission_probs = define_hmm(state_list, sentence, transition_probs, total_emission_probs)
                best_state_sequence, predicted_set = viterbi_algorithm(state_list, sentence, start_probs, transition_probs, emission_probs)
                # print(' '.join(sentence))
                # print("Best state sequence: " + str(best_state_sequence))
                # print("Real state sequence: " + str(tag_sentence) + "\n")
                
                all_predicted_sets.append(predicted_set)
                
                for i in range(len(tag_sentence)):
                    if(best_state_sequence[i] == tag_sentence[i]):
                        correct += 1
                    total += 1
                # count+= 1
            
            sentence = []
            tag_sentence = []
            
        if(word != "<s>" and word != "</s>"):
            sentence.append(word[0])
            tag_sentence.append(word[1])
            
    return (correct/ total), all_predicted_sets
            

def define_hmm(states, observations, transition_probs, total_emission_probs):

    start_probs = transition_probs["<s>"]
    
    emission_probs = {}
    for state in states:
        if(state != "<s>" and state != "</s>"):
            emission_probs[state] = {}
            for word in observations:
                if(word in total_emission_probs[state]):
                    emission_probs[state][word] = total_emission_probs[state][word]
                else:
                    emission_probs[state][word] = 0
    return start_probs, emission_probs
    
    # dummy data from slides
    # https://en.wikipedia.org/wiki/Viterbi_algorithm
    # states = ['q1', 'q2']
    # observations = ['x', 'z', 'y']
    # start_probability = {'q1': 1, 'q2': 0}
    
    # transition_probs = {
    #     'q1': {'q1': 0.7, 'q2': 0.3}, 
    #     'q2': {'q1': 0.5, 'q2': 0.5}
    #     }
    # emission_probs = {
    #     'q1': {'x': 0.6, 'z': 0.3, 'y': 0.1}, 
    #     'q2': {'x': 0.1, 'z': 0.2, 'y': 0.7, }
    #     }
    
def viterbi_algorithm(states, observations, start_probs, transition_probs, emission_probs):
    v = np.zeros((len(states),len(observations)))
    #first column
    for i, state in enumerate(states):
        if(state in start_probs):
            v[i][0] = start_probs[state] * emission_probs[state][observations[0]]
        else:
            v[i][0] = 0
        
    
    #loop through columns v(j,t) = max^N_i=1 v(i, t-1)*a_ij*b_j(O_t)
    for t in range(1, len(observations)):
        
        #loop through rows (j) 
        for j in range(0, len(states)):
            
            max_value = 0
            #calc the max of t-1
            for i in range(0, len(states)):
                
                # if(states[i] in transition_probs):
                #     if(states[j] in transition_probs[states[i]]):'
                try:
                    value = v[i][t-1] * transition_probs[states[i]][states[j]] * emission_probs[states[j]][observations[t]]
                except KeyError:
                    value = 0
                        
                if(value > max_value):
                    max_value = value
            v[j][t] = max_value
            
    #loop through columns
    max_tag_list = []
    for column in range(v.shape[1]):
        max_val = 0
        max_tag = None
        for row in range(v.shape[0]):
            
            # print(observations[column])
            # print(states[row])
            val = v[row][column]
            if(val > max_val):
                max_val = val
                max_tag = states[row]
        max_tag_list.append(max_tag)
    
    predicted_set = []
    for i in range(len(observations)):
        predicted_set.append((observations[i], max_tag_list[i]))
        
    return max_tag_list, predicted_set
    
def print_to_file(predicted_sets, predicted_test_file):
    f = open(predicted_test_file, 'w')
    
    sentence = ""
    for sen in predicted_sets:
        for tuple_tag in sen:
            if(len(sentence) != 0):
                sentence += ' '
            if(tuple_tag[1] is None):
                sentence += (tuple_tag[0] + '/None')
            else:
                sentence += ('/'.join(tuple_tag))
        f.write(sentence+'\n')
        sentence = ""
        
    
if __name__ == "__main__":
    main()