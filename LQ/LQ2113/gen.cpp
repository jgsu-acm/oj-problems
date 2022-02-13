#include <iostream>
#include <fstream>
#include <random>
#include <ctime>
using namespace std;
typedef uniform_int_distribution<> rnd;
typedef uniform_real_distribution<> rndf;
mt19937 egn(time(nullptr));
const int CASES = 10;
int main(int argc, char const* argv[])
{
    for(int t=1;t<=CASES;t++)
    {
        ofstream fout(to_string(t)+".in");
        // ==============================
        if(t==1) fout<<"((((("<<endl;
        else if(t==2) fout<<"()(((((((((((((((()()((((((((((((((((((((((((((((("<<endl;
        else 
        {
            int n;
            if(t<=4) n=200;
            else n=5000;
            for(int i=0;i<n;i++)
                fout<<(rnd(0,1)(egn)?'(':')');
            fout<<endl;
        }
        // ==============================
        fout.close();
    }
    return 0;
}