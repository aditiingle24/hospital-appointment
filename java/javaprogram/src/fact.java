class rec {
    int fact(int n){
        if(n==1){
            return 1;
        }
        else{
            return fact(n-1)*n;
        }
    }
}
class fact{
    public static void main(String args[]){
        rec r= new rec();
        System.out.println("fact "+r.fact(4));
    }
}