package week2;

/**
 * Simplified version of java.util.Date
 * 
 * 
 */
public class SimpleDate implements Comparable<SimpleDate>{

	private final int month, day, year;
	
	public SimpleDate(int m, int d, int y){
		month = m;
		day = d;
		year = y;
	}

	@Override
	public int compareTo(SimpleDate that) {
		if (this.year < that.year) return -1;
		if (this.year > that.year) return +1;
		if (this.month < that.month) return -1;
		if (this.month > that.month) return +1;
		if (this.day < that.day) return -1;
		if (this.day > that.day) return +1;
		return 0;
	}
	
}
