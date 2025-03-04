class sample {
    static int a,b;
    void getdata(int a, int b){
        this.a=a;
        this.b=b;
    }
    static void display(){
        System.out.println(a+b);
        System.out.println((a+b)/2);
    }
    public static void main(String args[])
    {
        sample ob= new sample();
        ob.getdata(5,5);
        sample.display();
    }
    }    
