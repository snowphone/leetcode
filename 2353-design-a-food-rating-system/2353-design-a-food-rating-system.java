import java.util.HashMap;
import java.util.Map;
import java.util.TreeSet;

class FoodRatings {
	public record Entry(Integer rating, String food) implements Comparable<Entry> {

		@Override
		public int compareTo(Entry other) {
			if (this.rating.equals(other.rating)) {
				return food.compareTo(other.food);
			}
			return -(this.rating - other.rating);
		}
	}
	public record LookupVal(String cuisine, Entry entry) {
	}

	private Map<String, TreeSet<Entry>> q = new HashMap();
	private Map<String, LookupVal> lookup = new HashMap();

	public FoodRatings(String[] foods, String[] cuisines, int[] ratings) {
		int n = foods.length;

		for (int i = 0; i < n; i++) {
			var cuisine = cuisines[i];
			var food = foods[i];
			var rating = ratings[i];

			var entry = new Entry(rating, food);

			q.putIfAbsent(cuisine, new TreeSet<>());
			q.get(cuisine).add(entry);
			lookup.put(food, new LookupVal(cuisine, entry));
		}
	}

	public void changeRating(String food, int newRating) {
		var lookupval = lookup.get(food);
		q.get(lookupval.cuisine()).remove(lookupval.entry());

		var newEntry = new Entry(newRating, food);
		q.get(lookupval.cuisine()).add(newEntry);
		lookup.put(food, new LookupVal(lookupval.cuisine, newEntry));
	}

	public String highestRated(String cuisine) {
		return this.q.get(cuisine).first().food();
	}
}

/**
 * Your FoodRatings object will be instantiated and called as such: FoodRatings obj = new
 * FoodRatings(foods, cuisines, ratings); obj.changeRating(food,newRating); String param_2 =
 * obj.highestRated(cuisine);
 */