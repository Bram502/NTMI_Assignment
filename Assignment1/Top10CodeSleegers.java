import static java.nio.file.StandardOpenOption.*;
import java.nio.file.*;
import java.io.*;
import java.lang.Object.*;
import java.util.*;

public class A1Step1 {
	
	public static void main(String[] args) {
		String[] topTenWords = new String[10];
		HashMap<String, Integer> wordCountTable = new HashMap<String, Integer>();
    	String thisLine = null;
      		try{
         	// open input stream test.txt for reading purpose.
        BufferedReader br = new BufferedReader(new FileReader("austen.txt"));
        while ((thisLine = br.readLine()) != null) {
        	if (thisLine.trim().equals("")) {
        		// emptyline
        	} else {
        	String[] words = thisLine.split("\\s+");
        	for(int j = 0; j < words.length; j++) {
        		if (wordCountTable.containsKey(words[j])) {
        			wordCountTable.put(words[j], wordCountTable.get(words[j])+1);
        			//System.out.println("vis");
        		} else {
        			wordCountTable.put(words[j], 1);
        		}
    		}	
    		}	
    	}

    	for (String key : wordCountTable.keySet()) {
   			/*System.out.println("------------------------------------------------");
   			System.out.println("Iterating or looping map using java5 foreach loop");
   			System.out.println("key: " + key + " value: " + wordCountTable.get(key));*/
   			for (int i = 0; i < topTenWords.length; i++) {
   				if(topTenWords[i] == null) {
   					topTenWords[i] = key;
   					break;
   				}
   				if (wordCountTable.get(topTenWords[i]) < wordCountTable.get(key) ) {
   					System.out.println(i);
   					String[] tempTopTenWords = new String[topTenWords.length];
   					tempTopTenWords = topTenWords.clone();
   					tempTopTenWords[i] = key;
   					for (int j = i+1; j < topTenWords.length; j++) {
   						tempTopTenWords[j] = topTenWords[j-1];	
   					}
   					topTenWords = tempTopTenWords;
   					for (int k = 0; k < tempTopTenWords.length; k++){
   						//System.out.println(tempTopTenWords[k]);
   						//System.out.println(topTenWords[k]);
   					}
				break;
   				}

   				
   			}
   	 }
		for (int i = 0; i < topTenWords.length; i++) {
			System.out.println(topTenWords[i]);
		}
		//System.out.println(thisLine);   
		}catch(Exception e){
         	e.printStackTrace();
      	}
    }
} 