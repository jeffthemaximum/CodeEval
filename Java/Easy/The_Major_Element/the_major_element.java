import java.util.HashMap;

public class the_major_element {
	public static void main (String[] args) {
		String line = "92,19,19,76,19,21,19,85,19,19,19,94,19,19,22,67,83,19,19,54,59,1,19,19";
		System.out.println(funcName(line));
	}
	
	public static String funcName(String line) {
		String[] line_array = line.split(",");
		float length = line_array.length;
		HashMap<String, Float> hm = new HashMap<String, Float>();
		boolean flag = false;
		for (String num:line_array) {
			float count = 1;
			if (hm.containsKey(num)) {
				count = hm.get(num);
				count += 1;
			}
			hm.put(num, count);
			if ((count / length) >= 0.5) {
				return num;
			}
		}
		if (flag == false) {
			return "None";
		}
		return null;
	}
}