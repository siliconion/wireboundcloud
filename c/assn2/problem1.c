#include <stdio.h>

int main(int argc, char ** argv){
//    for (int i = 1; i < argc; i++) {
//        printf("%s\n", argv[i]);
//    }
//    replacing the for loop with a combination of goto and if statements.
    int i = 1;
    LOOP:
      if(i < argc){
        printf("%s\n", argv[i]);
        i++;
        goto LOOP;
      }

    return 0;
}