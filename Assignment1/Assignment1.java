

public class Assignment1 {

    public static void main(String[] args) {
    	int n = Integer.parseInt(args[0]);
    	// int m = Integer.parseInt(args[1]);

    	try {
    		BufferedReader br = new BufferedReader(new InputStreamReader(new FileInputStrean("Assignment1\\austen.txt")));
    		String line = null;    		
    		HashMap map = new HashMap();
    		ArrayList<String> list = new ArrayList<String>();

	   		while ((line = br.readLine()) != null) {
	   			String[] tokens = line.split(" ");
	   			List<String> tokenList = Arrays.asList(tokens);
	   			list.addAll(tokenList);
    		}
    		
    	} catch(FileNotFoundExceptions e) { 
    		e.printStackTrace();
    	}
    }
}