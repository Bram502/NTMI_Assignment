import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Scanner;


public class Assignment1 {
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
    	
    	ArrayList<String> wordList = createWordList(path);
    	Map<String, Integer> wordMap = createWordMap(wordList, n);

    	int totalFreq = 0;
    	// Print all sequences with their frequencies and count the 
    	// total amount of frequencies
    	for (Entry<String, Integer> entry : wordMap.entrySet()) {
            String key = entry.getKey();
            Integer value = entry.getValue();
            totalFreq += value;
            System.out.println(key + "   " + value );
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
    		sequence = "";
    		
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
}
