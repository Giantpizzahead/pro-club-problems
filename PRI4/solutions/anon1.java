import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.Scanner;

public class anon1 {
	static class Pair {
		int x;
		int y;
		
		public Pair(int x, int y) {
			this.x = x;
			this.y = y;
		}
	}
	
	static class Cow {
		int cowID;
		double dist;
		
		public Cow(int id, double d) {
			cowID = id;
			dist = d;
		}
	}
	
	static class PairSorter implements Comparator<Cow> {

		@Override
		public int compare(Cow o1, Cow o2) {
			if (o1.dist < o2.dist) {
				return -1;
			} else if (o1.dist > o2.dist) {
				return 1;
			} else {
				return 0;
			}
		}
		
	}
	
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int numCows = in.nextInt();
		List<Pair> locations = new ArrayList<>();
		
		for (int i = 0; i < numCows; i++) {
			int xcoord = in.nextInt();
			int ycoord = in.nextInt();
			locations.add(new Pair(xcoord, ycoord));
		}
		anon1 p = new anon1();
		System.out.println(p.removeCow(locations));
		in.close();
	}
	
	public int removeCow(List<Pair> locs) {
		List<List<Cow>> distSeparationMap = new ArrayList<>();
		
		for (int i = 0; i < locs.size(); i++) {
			List<Cow> distances = new ArrayList<>();
			Pair p1 = locs.get(i);
			
			for (int j = 0; j < locs.size(); j++) {
				if (j != i) {
					Pair p2 = locs.get(j);
					double distance = Math.sqrt(Math.pow((p1.x - p2.x), 2) + Math.pow((p1.y - p2.y), 2));
					distances.add(new Cow(j+1, distance));
				}
			}
			Collections.sort(distances, new PairSorter());
			distSeparationMap.add(distances);
		}
		int smallestCow = -1;
		double maxMinDistance = Double.MIN_VALUE;
		
		for (int i = 1; i <= locs.size(); i++) {
			double minDist = Double.MAX_VALUE;
			
			for (int j = 0; j < distSeparationMap.size(); j++) {
				if ((j+1) != i) {
					List<Cow> dists = distSeparationMap.get(j);
					
					if (dists.get(0).cowID == i) {
						if (minDist > dists.get(1).dist) {
							minDist = dists.get(1).dist;
						}
					} else {
						if (minDist > dists.get(0).dist) {
							minDist = dists.get(0).dist;
						}
					}
				}
			}
			if (maxMinDistance < minDist) {
				maxMinDistance = minDist;
				smallestCow = i;
			}
		}
		return smallestCow;
	}
}