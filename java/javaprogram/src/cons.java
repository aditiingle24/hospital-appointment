class cons {
    int a;
    String n;
    void display(){
        System.out.println(a+" "+n);
    }
    public static void main(String args[])
    {
        cons ob= new cons();
        cons ob1= new cons();
        ob1.display();
        ob.display();
    }
    
}
