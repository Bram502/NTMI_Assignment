


/*
 * NTMI COURSE 2016 Part A Step 1
 * 04/02/2016
 * Sebastiaan Joustra, 10616999   
 * Bram Smit, 10666656 
 * Joeri Bes, 10358234
 *
 *
 * run file with arguments: -corpus [path] -n [value] -m [value]
 *
 * We sadly didn't find out double spaces functioned as full stop until we calculated the total frequencies.
 * So these are not accurate.
 *
 * Top 10 most frequencies of n-length;
 * n(1) = (the, to, and, of, a, her, I, was, in, in)                                       
 * n(2) = (of the, to be, in the, I am, of her, to the, it was, had been, she had, to her) 
 * n(3) = (I do not, I am sure, in the world, she could not, would have been, I dare say,
 *         a great deal, as soon as, it would be, could not be) 
 *
 * n(1) = total frequencies: 617091
 * n(2) = total frequencies: 617090
 * n(3) = total frequencies: 617089                           
*/

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Scanner;

public class A1Step1 {

	public static void main(String[] args) {
		String path = null;
		int n = 0;
		int m = 0;
    	
    	for (int i = 0; i<args.length; i++){
    		if(args[i].equals("-corpus")) {
    			path = args[i+1];
    		} else if(args[i].equals("-n")) {
    			n = Integer.parseInt(args[i+1]);
    		} else if(args[i].equals("-m")) {
    			m = Integer.parseInt(args[i+1]);
    		}
    	}
    	if(path == null || n ==0 || m==0) {
    		System.out.println("Correct usage to run: -corpus [path] -n [value] -m [value]");
    		System.exit(0);
    	}
    	
        System.out.println("n: " + n);
        System.out.println("m: " + m);

    	ArrayList<String> wordList = createWordList(path);
    	Map<String, Integer> wordMap = createWordMap(wordList, n);


        // Retrieve the top m most frequent sequences and print
        String[] top = getTopFrequenties(wordMap, m);
        for (String s : top) {
            System.out.println(s);
        }

        // Print all sequences with their frequencies and count the 
        // total amount of frequencies
        int totalFreq = 0;
    	for (Entry<String, Integer> entry : wordMap.entrySet()) {
            String key = entry.getKey();
            Integer value = entry.getValue();
            totalFreq += value;
        }    	
    	System.out.println("Total frequencies: " + totalFreq);    	
    }


	private static ArrayList<String> createWordList(String path) {
		ArrayList<String> wordList = new ArrayList<String>();
    	
    	try {
    		Scanner sc = new Scanner(new File(path));
	    	while(sc.hasNext()) {
	    		String word = sc.next();
	    		wordList.add(word);
	    	}
	    	sc.close();
    	} catch(IOException e) {
    		e.printStackTrace();
    	}

		return wordList;
	}
	
    
	private static Map<String, Integer> createWordMap(ArrayList<String> wordList, int n) {

		Map<String, Integer> wordMap = new HashMap<String, Integer>();		
		StringBuilder sb = new StringBuilder();
    	String sequence = "";
    	
    	for(int i = 0; i<wordList.size(); i++) {
    		sb.setLength(0);
    		// End of word list reached
    		if(i+n > wordList.size()) {
    			break;
    		}    		
    		// Create sequence of length n
    		for(int j = 0; j<n; j++) {
    			if(sb.length() > 0) {
    				sb.append(" ");
    			}
    			sb.append(wordList.get(i+j));
    		}
    		sequence = sb.toString();
    		
        	// Insert sequence into hashmap
        	if(wordMap.containsKey(sequence)) {
        		wordMap.put(sequence, wordMap.get(sequence)+1);
        	} else {
        		wordMap.put(sequence, 1);
        	}
    	}
    	
		return wordMap;
	}

    private static String[] getTopFrequenties(Map<String, Integer> wordMap, int m) {

        String[] top = new String[m];

        for (String key : wordMap.keySet()) {

            for (int i = 0; i < top.length; i++) {
                if (top[i] == null) {
                    top[i] = key;
                    break;
                } else if (wordMap.get(top[i]) < wordMap.get(key) ) {
     
                    String[] temp = new String[top.length];
                    temp = top.clone();
                    temp[i] = key;
                    for (int j = i+1; j < top.length; j++) {
                        temp[j] = top[j-1];  
                    }
                    top = temp;
                    break;
                }                
            }
        }

        return top;
    }
}
