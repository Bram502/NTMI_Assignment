import itertools

if __name__ == "__main__":
	a = ["know", "I", "opinion", "do", "be", "your", "not", "may", "what"]
	b = ["I", "do", "not", "know"]

	a_perm = list(itertools.permutations(a))
	b_perm = list(itertools.permutations(b))
	
