#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(void) {
    int input;
    char* output = (char*) malloc(1);
    char* lookup = "CLXVI";
    int values [] = {100,50,10,5,1};
    int i = 0;
    *output = '\0';

    scanf("%d", &input);
    printf("%d\n", input);
    for(;i< strlen(lookup);i++) {
        for (; input >= values[i]; input -= values[i]) {
            output = (char *) realloc(output, strlen(output) + 2);
            strncat(output, &lookup[i],1);
        }
    }


    printf("%s\n", output);
    free(output);

    return 0;
}
