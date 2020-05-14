#include <stdio.h>

void square(int num) {
	num = num * num;
}

void square_by_ref(int* num_ref) {
	*num_ref = *num_ref * *num_ref;
}
int main() {
	int x = 4;
	square(x);
	printf("%d\n", x); // function is pass by value!
  square_by_ref(&x);
  printf("%d\n", x);
	return 0;
}
