class Student {
    String name;
    int age;

    public void printInfo() {
        System.out.println(this.name);
        System.out.println(this.age);
    }

    // Non parameterized Constructor
    // Student() {
    //     System.out.println("constructor called");
    // }

    // parameterized Constructor
    Student(String name, int age) {
        this.name = name;
        this.age = age;
    }
}

public class OOPS {
    public static void main(String[] args) {
        Student s1 = new Student("YOSHITHA", 19);
        // s1.name = "YOSHITHA";
        // s1.age = 19;

        s1.printInfo();
    }
}

