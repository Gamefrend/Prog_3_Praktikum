int main(void){
    int input = 129;
    int rest = input;
    for(;rest/100>0;rest = rest-100){
    }
    for(;rest/50>0;rest = rest-50){
        printf("%c",'L');
    }
    for(;rest/10>0;rest = rest-10){
        printf("%c",'X');
    }
    for(;rest/5>0;rest = rest-5){
        printf("%c",'V');
    }
    for(;rest/1>0;rest = rest-1){
        printf("%c",'I');
    }
    printf("\n");

}