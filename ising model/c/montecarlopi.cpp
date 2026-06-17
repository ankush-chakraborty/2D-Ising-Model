#include <iostream>
#include <cstdlib>
#include <time.h>

int main(){
    int i, c = 0, t = 1000;
    double rx, ry, res;
    
    srand(static_cast<unsigned int>(time(0)));
    for(i = 0; i < t; i++){
        rx = rand() / (double) RAND_MAX;
        ry = rand() / (double) RAND_MAX;

        if (rx*rx + ry*ry <= 1){
            c++;
        }
    }
    int x = 4.0*c/t;
    std::cout << x;
    return 0;
}