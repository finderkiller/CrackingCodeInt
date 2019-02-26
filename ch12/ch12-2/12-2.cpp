#include <getopt.h>
#include <iostream>

using namespace std;

void reverse(char* str)
{
	if (str == NULL) {
		return;
	}
	char* end = str;
	char tmp;
	while(*end) {		//'\0'
		end++;
	}
	end--;
	while (end > str) {
		tmp = *str;
		*str++ = *end;
		*end-- = tmp;
	}
	return;
}

int main(int argc, char* argv[])
{
	char* str = NULL;
	int c = 0;
	while ((c = getopt_long(argc, argv, "s:", NULL, NULL)) != -1) {
		switch (c) {
			case 's':
				str = optarg;
				cout << str << endl;
				reverse(str);
				cout << str << endl;
				break;

		}
	}
}
