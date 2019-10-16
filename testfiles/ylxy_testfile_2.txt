const int const_int_0_1 = 0, const_int_0_2 = +0, const_int_0_3 = -0;
const int Const_int_1 = 295, const_int_2 = +3, const_int_3 = -15;
const char const_char_1 = '_', const_char_2 = '+', const_char_3 = '*';
const char Const_char_4 = 'a', const_char_5 = 'B', const_char_6 = '9', const_char_7 = '0';

int var_int1;
char var_char1;
int  array_int[1];
char array_char[1];

int fun1(int a, char b) {
	const int c = 9;
	const char d = 'd';
	int e;
	char f;
	var_int1 = const_int_0_1 * const_int_0_1 - (const_int_0_2 / const_int_2) * const_int_0_3 + const_int_3;
	var_char1 = 'a';
	var_char1 = const_char_1;
	printf("printf1");
	printf(-a * b + b / a);
	printf("printf3", a * a - b * b);
	printf(d);
	printf(c);
	printf(" ");
	printf("");
	return (1);
}
char fun2() {
	return ('a');
}

void main() {
	int a;
	char b;
	a = 5;
	b = 'b';
	printf("123");
	fun1(a, b);
}