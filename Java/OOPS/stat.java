class Student {
    String name;
    // All the objects will have same name(In general, it's common for all the objects)
    static String school;

    public static void changeSchool() {
        school = "newschool";
    }
}

public class stat {
    public static void main(String args[]) {
        Student.school = "Narayana"; 
        Student stu1 = new Student();
        stu1.name = "YOSHITHA";
        System.out.println(stu1.school);
    }
}
