#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct le{
    int anzahl; char name[25]; struct le *next;
}ListEle;

ListEle *hinzufuege(ListEle *liste, char* name){
    ListEle *vorheriges;
    ListEle *aktuell;

    if (liste == NULL){
        ListEle *neu = (ListEle*) malloc(sizeof (ListEle));
        strcpy(neu->name,name);
        neu->anzahl = 1;
        neu->next = NULL;
        return neu;
    } else {
        aktuell = liste;
        for (;aktuell != NULL;aktuell = aktuell->next){
            if(strcmp(aktuell->name,name)==0){
                aktuell->anzahl += 1;
                return liste;
            }else {
                vorheriges = aktuell;
            }
        }
        if(aktuell == NULL) {
            ListEle *neu = (ListEle *) malloc(sizeof(ListEle));
            strcpy(neu->name, name);
            neu->anzahl = 1;
            neu->next = NULL;
            vorheriges->next = neu;
            return liste;
        }
    }
}

ListEle *korrigiere(ListEle *liste, char* altname, char* neuname){
    ListEle *aktuell;
    if(liste==NULL){
        return liste;
    }
    aktuell = liste;
    for(;aktuell!=NULL;aktuell = aktuell->next){
        if(strcmp(aktuell->name,altname)==0){
            strcpy(aktuell->name,neuname);
            return liste;
        }
    }
    return liste;
}

ListEle *suche(ListEle *liste, char* name){
    ListEle *aktuell;
    if(liste==NULL){
        return NULL;
    }
    aktuell = liste;
    for(;aktuell!=NULL;aktuell = aktuell->next){
        if(strcmp(aktuell->name,name)==0){
            return aktuell;
        }
    }
    return NULL;
}

int main(void){
    ListEle *beispiel;
    beispiel = hinzufuege(NULL, "Enis");
    beispiel = hinzufuege(beispiel, "Alina");
    beispiel = hinzufuege(beispiel, "Angelos");
    beispiel = hinzufuege(beispiel, "Enis");
    beispiel = hinzufuege(beispiel, "Angelos");
    beispiel = korrigiere(beispiel,"Angelos","Angi");
    beispiel = suche(beispiel, "Alina");
    beispiel = suche(beispiel, "fedfe");
    printf("%d %s",beispiel->anzahl,beispiel->name);


}
