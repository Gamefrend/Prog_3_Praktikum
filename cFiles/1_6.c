#include <stdio.h>
#include <string.h>
int main(int argc, char* argv[]){
    int i;
    int j;
    for (i=1;i<argc;i++){
        for (j=0; j<strlen(argv[i]);j++){
            if(40<argv[i][j] && argv[i][j]<91){
                if(argv[i][j]+13>90){
                    printf("%c",argv[i][j]+13-25);
                }else{
                    printf("%c",argv[i][j]+13);
                }
            }
            else if(96<argv[i][j] && argv[i][j]<123) {
                if (argv[i][j] + 13 > 123) {
                    printf("%c", argv[i][j] + 13 - 25);
                } else {
                    printf("%c", argv[i][j] + 13);
                }
            } else{
                printf("%c", argv[i][j]);
            }
        }
        printf(" ");
    }
    printf("\n\n%c",argv[1][0]); /*C*/
    printf("\n\n%c",argv[2][0]); /*i*/
    printf("\n\n%c",argv[2][1]); /*t*/

    return 0;
}
