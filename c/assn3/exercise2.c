#include <stdio.h>

void copy(char* str, char* in_str){
  printf("%s\n", in_str);
  printf("%s\n", str);
}
void main() {
	char str[];
	copy(*str, "hakuna matata!"); // this line should copy "hakuna matata!"
	                         // into our char array
	printf("%s\n", str);
	// Anything else?

	return 0;
}