public class conoverload {
    int id;
    String name;
    int age;
    conoverload(int i, String n){
        id=i;
        name=n;
    }
    conoverload(int i, String n, int a){
        id=i;
        name=n;
        age=a;
    }
    void display()
    {
        System.out.println(id+" "+name+" "+age);
    }
    public static void main(String args[]){
        conoverload ob=new conoverload(1,"aditi",20);
        conoverload ob1=new conoverload(2,"adi");
        ob.display();
        ob1.display();
    }
}
