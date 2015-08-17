package shortest_repetition;

public class shortest_repetition {

	public static void main(String[] args) {
		String line = "adcdefg";
		String[] line_array = line.split("");
		System.out.println(find_repeat(line_array));
	}
	public static Integer find_repeat(String[] test_array) {
		String first_char = test_array[0];
		int array_len = test_array.length;
		for (int i = 1; i < array_len; i++) {
			String test_char = test_array[i];
			if (test_char.equals(first_char)) {
				int repeat_idx = i;
				return repeat_idx;
			}
		}
		return array_len;
	}

}
