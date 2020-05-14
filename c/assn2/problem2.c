#include <stdio.h>

void amazeWOW1() {
	int i;
	printf("%s:\t", __FUNCTION__);
	for (i = 0; i <= 10; i++) {
		if (i % 2 == 1) {
			printf("%d ", i);
		}
	}
	printf("\n");
}

void amazeWOW2() {
	int i = 1;
	printf("%s:\t", __FUNCTION__);
  while(i <= 10){
    if(i  % 2 == 1) {
      printf("%d ", i);
    }
    i++;
  }
	printf("\n");
}

void amazeWOW3() {
	int i = 1;
	printf("%s:\t", __FUNCTION__);
	do{
      if(i%2 == 1){
        printf("%d ", i);
      }
      i++;
	} while (i<=10);

	printf("\n");
}

int main(int argc, char* argv[]){
  amazeWOW1();
  amazeWOW2();
  amazeWOW3();
}