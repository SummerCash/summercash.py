#include "../build/go_lib.h"
#include <stdio.h>

int main() {
    // Call the Hello function from the Go library
    Hello();
    
    // Call the SumFloat function from the Go library
    float result = SumFloat(4.786, 9.127);
    printf("sum: %f\n", result);
    

    char *dowland = NewPersonTestStructAsJSON(
        "dowland",
        66.5,
        14
    );

    char *matt = NewPersonTestStructAsJSON(
        "matt",
        68.0,
        15
    );
    // printf("matt: %s\n", matt);

    printf("matt: %s\n\ndowland: %s\n\n", matt, dowland);

    return 0;
}