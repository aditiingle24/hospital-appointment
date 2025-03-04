class paracon {
    int i;
    String n;
    paracon(int id,String na)
    {
        i=id;
        n=na;
    }
    void display()
    {
        System.out.println("rollno "+i+"name "+n);
    }
    public static void main(String args[])
    {
        paracon ob= new paracon(1,"aditi");
        ob.display();
        paracon ob1= new paracon(2,"hi");
        ob1.display();
    }    
}
