abstract class Animal {
    abstract void walk();
    // Constructors 
    Animal() {
        System.out.println("You are creating an animal");
    }

    public void eat() {
        System.out.println("Animal eats");
    }
}

class Horse extends Animal {
    Horse() {
        System.out.println("Created a Horse");
    }
    public void walk() {
        System.out.println("Walks on 4 legs");
    }
}

class Hen extends Animal {
    public void walk() {
        System.out.println("Walks on 2 legs");
    }
}

public class abs {
    public static void main(String[] args) {
        Horse horse = new Horse();
        // horse.walk();
        // horse.eat();
    }
}
