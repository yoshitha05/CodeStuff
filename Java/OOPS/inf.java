interface Animal {
    int eyes = 2; // static since every animal has 2 eyes
    public void walk();
}

interface Herbivore {

}

class Horse implements Animal, Herbivore {
    public void walk() {
        System.out.println("walks on 4 legs");
    }
}
public class Inf {
    public static void main(String[] args) {
        Horse horse = new Horse();
        horse.walk();
    }
}
