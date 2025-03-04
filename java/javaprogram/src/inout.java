class outer{
    int x=100;
    void test(){
        inner i =new inner();
        i.display();
    }
    class inner{
        void display(){
            System.out.println(x);
        }
    }
}
class inout{
    public static void main(String args[]){
        outer o=new outer();
        o.test();
    }
}