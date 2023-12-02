#include <stdio.h>
#include <string.h>
#include <stdlib.h>
int main(void){
    int i = 0;
    int input = 0;
    char* output = "Zahl: ";
    scanf("%d",&input);
    i = input;
    for (;i/100>0;){
        output = realloc(output,sizeof (char )*(2+ strlen(output)+1));
        output [strlen(output)-2] = 'C';
        i = i - 100;
    }
    printf("%s",output);

}