package n_mod_m;

public class n_mod_m {
	public static void main (String[] args) {
		String line = "2,3";
		String line_array[] = line.split(",");
		int n_mod_m = Integer.parseInt(line_array[0]) % Integer.parseInt(line_array[1]);
		System.out.println(n_mod_m);
	}
}
