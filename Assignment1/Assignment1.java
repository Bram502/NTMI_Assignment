import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
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
    	
    	ArrayList<String> wordList = new ArrayList<String>();
    	
    	Map<String, Integer> wordMap = new HashMap<String, Integer>();
    	
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
    	System.out.println(wordList.size());
    	int countDown  = n;
    	int count = 0;
    	//ArrayList<String> sequence = new ArrayList<String>();
    	StringBuilder sb = new StringBuilder();
    	String sequence = "";
    	
    	for(int i = 0; i<wordList.size(); i++) {
    		sb.setLength(0);
    		sequence = "";
    		if(i+n > wordList.size()) {
    			break;
    		}
    		// create sequence of length n
    		for(int j = 0; j<n; j++) {
    			if(sb.length() > 0) {
    				sb.append(" ");
    			}
    			sb.append(wordList.get(i+j));
    		}
    		sequence = sb.toString();
    		
        	//insert sequence into hashmap
        	if(wordMap.containsKey(sequence)) {
        		wordMap.put(sequence, wordMap.get(sequence)+1);
        	} else {
        		wordMap.put(sequence, 1);
        	}
    	}
    	
    	System.out.println(wordMap.size());

    	int totalFreq = 0;
    	for (Entry<String, Integer> entry : wordMap.entrySet()) {
            String key = entry.getKey();
            Integer value = entry.getValue();
            totalFreq += value;
            System.out.println(key + "   " + value );
        }
    	System.out.println("Total frequencies: " + totalFreq);
    	
    	String[] wordArray = new String[m];
    	int[] countArray = new int[m];
    	
    }
}
