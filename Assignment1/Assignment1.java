import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
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

        Map<String, Integer> wordMap = fetchHashMap(path, n, m);
    }

    private static Map<String, Integer> fetchHashMap(String path, int n, int m){
        List<String> wordList = new ArrayList<String>();        
        Map<String, Integer> wordMap = null;
        
        try {
            Scanner sc = new Scanner(new File(path));
            wordMap = new HashMap<String, Integer>();
            
            while(sc.hasNext()) {
                String word = sc.next();
                wordList.add(word);
            }
            sc.close();
            System.out.println(wordMap.size());

        } catch(IOException e) {
            e.printStackTrace();
        }


        return wordMap;
    }
}
