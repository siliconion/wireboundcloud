#include <stdio.h>

void get_triangular_num(int i){
 for(int j = 0; j < i; j++){
    printf("The %d-th triangular number is %d\n", j, j*(j+1)/2);
 }
}

int main(int argc, char *argv[]){
  get_triangular_num(100);
}