package clean_up_words;


public class clean_up_the_words {
	public static void man(String[] args) {
		String line = "(--9Hello----World...--)";
		for (int i = 0; i < line.length(); i++){
			char c = line.charAt(i);
			StringBuilder sb = new StringBuilder();
			if (Character.isLetter(c)) {
				if (i > 0) {
					if (Character.isLetter(sb.charAt(i-1))) {
						sb.append(c);
					}
					else {
						sb.append(" ");
					}
				}
			}
			System.out.println(sb);
		}
	}
}
