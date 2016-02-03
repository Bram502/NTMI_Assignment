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
    	
    	Map<ArrayList<String>, Integer> wordMap = new HashMap<ArrayList<String>, Integer>();
    	
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
    	System.out.println(wordList.get(0));
    	int countDown  = n;
    	int count = 0;
    	ArrayList<String> sequence = new ArrayList<String>();
    	
    	for(int i = 0; i<wordList.size(); i++) {
    		sequence.clear();
    		count = 0;
    		if(i+n > wordList.size()) {
    			break;
    		}
    		// create sequence of length n
    		for(int j = 0; j<n; j++) {
    			sequence.add(wordList.get(i+j));
    		}
    		
        	//insert sequence into hashmap
        	if(wordMap.containsKey(sequence)) {
        		wordMap.put(sequence, wordMap.get(sequence)+1);
        		System.out.println(sequence);
        	} else {
        		wordMap.put(sequence, 1);
        	}
    	}
    	
    	System.out.println(wordMap.size());
    	//System.out.println(wordList);
    	
    	/*for (List<String> name: wordMap.keySet()){

            String key =name.toString();
            String value = wordMap.get(name).toString();  
            System.out.println(name + " " + value);
    	}*/
    	
    	for (Entry<ArrayList<String>, Integer> entry : wordMap.entrySet()) {
            ArrayList<String> key = entry.getKey();
            Integer value = entry.getValue();
            //System.out.println(key.size());
            System.out.println("key, " + key + " value " + value );
        }
    	
    	String[] wordArray = new String[m];
    	int[] countArray = new int[m];
    	
    }
}
