package bank;

class Account {
    public String name;
    protected String email;
    private String pwd;

    // getters and setters
    public String getPwd() {
        setPassword(randomPass);
        return this.pwd;
    }

    public void setPwd(String pass) {
        this.pwd = pass;
    }

}
public class Bank {
    public static void main(String args[]) {
        Account acc1 = new Account();
        acc1.name = "Apna College";
        acc1.email = "Apna College@gmail.com";
        // Here we couldn't access password that we created in private class so we use getters that is defining a different function again and defining, calling the variable
        // acc1.pwd = "abcd";
        acc1.setPwd("abcd");
        System.out.println(acc1.getPwd());
    }
}
