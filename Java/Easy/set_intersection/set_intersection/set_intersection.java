package set_intersection;
import java.util.Arrays;
import java.util.Iterator;

public class set_intersection {
	public static void main (String[] args)
	{	
		String line = "78,79,80,81,82,83,84,85,86,87,88;83,84,85,86,87,88,89,90";
		String[] output = new String[0];
		int total_common_elements = 0;
		String[] lines = line.split(";");
		String[] first_new_string_array = lines[0].split(",");
		String[] second_new_string_array = lines[1].split(",");
		for (int i = 0; i < first_new_string_array.length; i++) {
			for (int j = 0; j < second_new_string_array.length; j++) {
				if (first_new_string_array[i].equals(second_new_string_array[j])){
					if (total_common_elements == 0) {
						total_common_elements += 1;
						String[] new_total_common_elements = new String[total_common_elements];
						new_total_common_elements[0] = first_new_string_array[i];
						output = new_total_common_elements;
					}
					else {
						total_common_elements += 1;
						String[] new_total_common_elements = new String[total_common_elements];
						System.arraycopy(output, 0, new_total_common_elements, 0, total_common_elements-1);
						new_total_common_elements[total_common_elements-1] = first_new_string_array[i];
						output = new_total_common_elements;
					}
				}
			}
		}
		if (output.length == 0) {
			System.out.println("");
		}
		else{
			System.out.println(ToLine(output));
		}
	}
	public static StringBuilder ToLine(String[] output){
		StringBuilder builder = new StringBuilder();
		for (int i = 0; i < output.length; i++) {
			builder.append(output[i]);
			if (i != (output.length-1) ){
				builder.append(",");
			}
		}
		return builder;
	}
}
