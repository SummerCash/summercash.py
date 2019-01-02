#include "../build/go_lib.h"
#include <stdio.h>

int main() {
    // Call the Hello function from the Go library
    Hello();
    
    // Call the SumFloat function from the Go library
    float result = SumFloat(4.786, 9.127);
    printf("sum: %f\n", result);
    
    return 0;
}