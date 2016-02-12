

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Iterator;
import java.util.List;

public class ReadCorpus {
    private String path;
    private BufferedReader br;

    public ReadCorpus(String path) {
        this.path = path;
    }

    public List<String> createWordList(String path ) {
        List<String> wordList = new ArrayList<String>(1);

        try {
            br = new BufferedReader(new FileReader(path));
			String line = null;
            Boolean multiple;
            Boolean previousLine = false;
            while((line = br.readLine()) != null) {
             
                    // remove double spaces inside sentence and add to wordList
    	            String[] words = line.split(" ");
                    List<String> tempList = new ArrayList<String>(Arrays.asList(words));
                    Iterator<String> it = tempList.iterator();
                    while (it.hasNext()) {
                        if (it.next().length() == 0) {
                            it.remove();
                        }
                    }
                    // Here it will prevent the error ocurring when multiple blank line cause to many Start|Stop symbols
                    if (tempList.size() == 0 && !previousLine) {                     
                        wordList.add("</s>");
                        wordList.add("<s>");                   
                        previousLine = true;
                    } else if (tempList.size() != 0){
                        previousLine = false;
                    }
    	            wordList.addAll(tempList);
                       
            }
            br.close();
        } catch(IOException e) {
            e.printStackTrace();
        }
        return wordList;
    }
    
}
