#include <ctype.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <stdio.h>
void komprimiere(const char *ein,char *aus){
    if (isalpha(ein[0])){
        aus[0] = ein[0];
        if(strlen(ein)<12 && strlen(ein)>=3){
            sprintf(&aus[1],"%d", strlen(ein)-2);
            aus[2] = ein[strlen(ein)-1];
            aus[3] = '\0';
        } else if(strlen(ein)>=12) {
            sprintf(&aus[1], "%d", strlen(ein)-2 / 10);
            sprintf(&aus[2], "%d", strlen(ein)-2 % 10);
            aus[3] = ein[strlen(ein)-1];
            aus[4] = '\0';
        } else{
            strcpy(aus,ein);
        }
        printf("%s\n",ein);
        printf("%s",aus);
    } else{
        strcpy(aus,ein);
    }
}

void entprelle(const char *ein,char *aus){
    char vorherigerbuchstabe = ein[0];
    int i = 1;
    int hinzugefuegt = 1;
    aus[0] = ein[0];
    for(;i< strlen(ein);i++){
        if(ein[i] != vorherigerbuchstabe){
            aus[hinzugefuegt] = ein[i];
            hinzugefuegt++;
            vorherigerbuchstabe = ein[i];
        }
    }
    aus[hinzugefuegt] = '\0';
    printf("%s",aus);
}

void expandieren(const char *ein,char *aus){
    int zaehler = 1;
    int welcheZahl;
    aus[0] = ein[0];
    if(isdigit(ein[1]) && isdigit(ein[2]) && isalpha(ein[strlen(ein)-1])){
        welcheZahl = (ein[1] - '0') * 10;
        welcheZahl += ein[2] - '0';
        for(;zaehler < welcheZahl+1;zaehler++){
            if(zaehler%3==1){
                aus[zaehler]='b';
            }if(zaehler%3==2){
                aus[zaehler]='l';
            }if(zaehler%3==0){
                aus[zaehler]='a';
            }
        }
        aus[zaehler] = ein[strlen(ein)-1];
        aus[zaehler + 1] = '\0';
    }else if(isdigit(ein[1]) && isalpha(ein[strlen(ein)-1])){
        welcheZahl = ein[1] - '0';
        for(;zaehler < welcheZahl+1;zaehler++){
            if(zaehler%3==1){
                aus[zaehler]='b';
            }if(zaehler%3==2){
                aus[zaehler]='l';
            }if(zaehler%3==0){
                aus[zaehler]='a';
            }
        }
        aus[zaehler] = ein[strlen(ein)-1];
        aus[zaehler + 1] = '\0';

    }else{
        strcpy(aus,ein);

    }
}


int main(void){
    char* ein = "L10n";
    char aus[100];
    expandieren(ein,aus);
    printf("%s",aus);
}
