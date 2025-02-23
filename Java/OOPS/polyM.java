class Student {
    String name;
    int age;

    // Here, these different functions that perform different tasks under same function name is referred as Function Overloading
    public void printInfo(String name) {
        System.out.println(name);
    }

    public void printInfo(int age) {
        System.out.println(age);
    }

    public void printInfo(String name, int age) {
        System.out.println(name+ " " + age);
    }
}


public class polyM {
    public static void main(String[] args) {
        Student s1 = new Student();
        s1.name = "YOSHITHA";
        s1.age = 19;

        s1.printInfo(s1.name, s1.age);
    }
}