import java.util.*;

// Custom class representing a Person
class Person {
    String name;
    int score;
    Person(String name, int score) {
        this.name = name;
        this.score = score;
    }
}

public class PRB4 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // Create an array of people
        int N = sc.nextInt();
        Person[] people = new Person[N];
        for (int i = 0; i < N; i++) {
            people[i] = new Person(sc.next(), sc.nextInt());
        }
        // Sort the array using a custom Comparator
        Arrays.sort(people, new Comparator<Person>() {
            @Override
            public int compare(Person a, Person b) {
                // Sort by increasing score
                return a.score - b.score;
            }
        });
        // Print out the array
        for (int i = 0; i < N; i++) {
            System.out.printf("%s %d\n", people[i].name, people[i].score);
        }
    }
}