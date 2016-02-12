import java.util.List;

public class A1Step2 {
     public static void main(String[] args) {
    	String path = "Assignment1\\test.txt";
    	ReadCorpus reader = new ReadCorpus(path);

        List<String> wordList = reader.createWordList(path);
        for (int i = 0; i < wordList.size(); i++) {
			System.out.println(i + ": " + wordList.get(i));
        }
    }
}