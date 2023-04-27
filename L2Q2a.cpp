using namespace std;

int power(int a,int b):
    if (b==0):
        return 1
    if(b>0):
        return (a*power(a,b-1))
    else:
        return (1/(a*power(1/a,b+1)))

int main()
{
int a= input("Enter base number ");
int b= input("Enter power number");
cout<<(power(a,b))
}
