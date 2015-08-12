package odd_numbers;

public class odd_numbers {
	public static void main(String[] args) 
	{
		for (int i = 0; i < 100; i++) {
			if (isOdd(i)) {
				System.out.println(i);
			}
		}
	}
	public static Boolean isOdd(int x) {
		if ((x % 2) == 1) {
			return true;
		}
		return false;
	}
}
