package swap_case;

public class swap_case {
	public static void main (String[] args)
	{
		String CorrectLine;
		StringBuilder sb = new StringBuilder();
		String line = "hELLO wORLD!";
		for (int I = 0; I < line.length(); I++){
			char c = line.charAt(I);
			if (c == Character.toUpperCase(c)){
				c = Character.toLowerCase(c);
			}
			else if (c == Character.toLowerCase(c)){
				c = Character.toUpperCase(c);
			}
			else {
				c = c;
			}
		sb.append(c);		
		}
	CorrectLine = sb.toString();
	System.out.println(CorrectLine);
	}
}
