#include <iostream>
#include <a.h>
#include <c/c.h>
#include <d.h>
using namespace std;

int main(int argc, const char * argv[])
{
    int i = 0;
    std::cout << "test cmake and vscode!!!" << std::endl;
    std::cout << "test vscode and git!!!" << std::endl;
    
    printf("%s\n", func_a().c_str());
    printf("%s\n", func_c().c_str());
    printf("%s\n", func_d().c_str());    

    return 0;
}