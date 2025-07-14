import com.steve.banking.Accounts;
import com.steve.banking.OffShoreAccounts;

public class Banking {
    public static void main(String[] args) {
        Accounts steve = new Accounts("Steve");
        steve.setBalance(20.00);
        steve.addInterest();
        System.out.println("Steve Balance: "+steve.getBalance());

        Accounts nick = new Accounts("Nick",100.00);
        nick.withdraw(20.00);
        System.out.println("Nick Balance: "+nick.getBalance());

        System.out.println("Interest rate is currently: "+Accounts.getInterestRate());
        System.out.println("Number of active accounts: "+Accounts.getAccountsTotal());

        OffShoreAccounts david = new OffShoreAccounts("David",300.00,"EU","432L");
        System.out.println(david.getTaxCode()); // From itself
//        System.out.println(david.getBalance()); // Called from parent class Accounts
        david.addInterest();
        System.out.println("David Balance: "+david.getBalance());

        System.out.println(steve.toString());

        Accounts pat = new OffShoreAccounts("Pat",50.00);
        System.out.println(pat.toString()); // Calls Accounts method
        System.out.println("Pat Interest start");
        pat.addInterest();
        System.out.println("Pat Interest end");
        pat.getBalance();
        nick.getBalance();
//        System.out.println(pat.getTaxCode());  // Can't call as Accounts does not have getTaxCode()

        System.out.println("Pat is OffShore "+(pat instanceof OffShoreAccounts));
        System.out.println("Pat is Account "+(pat instanceof Accounts));
        System.out.println("Nick is OffShore "+(nick instanceof OffShoreAccounts));
        System.out.println("Nick is Account "+(nick instanceof Accounts));

        System.out.println("David your final balance is: "+david.close());
    }
}
