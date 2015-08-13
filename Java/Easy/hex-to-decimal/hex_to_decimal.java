import java.util.HashMap;

public class hex_to_decimal {
	public static void main(String[] args) {
		String line = "3ff5";
		char[] line_array = line.toCharArray(); 
		HashMap hm = generateHashmap();
		int total = 0;
		int j = line.length()-1;
		for (int i = 0; i <= line.length()-1; i++){
			int x = (Integer)hm.get(line_array[i]);
			total +=  (x * Math.pow(16, j));
			j--;
		}
		System.out.println(total);
	}
	public static HashMap generateHashmap() {
		HashMap<Character, Integer>hm = new HashMap<Character, Integer>();
		hm.put('1', 1);
		hm.put('2', 2);
		hm.put('3', 3);
		hm.put('4', 4);
		hm.put('5', 5);
		hm.put('6', 6);
		hm.put('7', 7);
		hm.put('8', 8);
		hm.put('9', 9);
		hm.put('a', 10);
		hm.put('b', 11);
		hm.put('c', 12);
		hm.put('d', 13);
		hm.put('e', 14);
		hm.put('f', 15);
		return hm;
	}
}