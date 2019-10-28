int var_int1;
char var_char1;
int  array_int[100];
char array_char[100];

int fun1_printf(int a, char b) {
	const int c = 9;
	char d;
	d = b;
	printf("printf1");
	printf(-a * b + b / a);
	printf("printf3", a * a - b * b);
	printf(d);
	printf(c);
	printf(" ");
	printf("");
	return (1);
}
char fun2_scanf() {
	int a, b;
	char c, d;
	scanf(a);
	scanf(a, b);
	scanf(a, c);
	scanf(d);
	return (d);
}
void fun3_empty() {

}
void fun4_while() {
	int a;
	a = 0;
	while (a < 100) {
		array_int[a] = a;
		a = a + 1;
	}
}
void fun5_do_while() {
	int a;
	char b;
	b = 'b';
	a = 100;
	do {
		array_char[a] = b;
		a = a - 1;
	} while (a >= 0);
}
void fun6_for() {
	int a;
	for (a = 1; a < 100; a = a + 1) {
		array_int[a] = array_int[a - 1] + 1;
	}
}
int fun7_if(int b) {
	int a;
	a = 0;
	if (a != 100) {
		a = a + 1;
	}
	if (a == a) {
		a = 66;
	}
	if (1) {
		if (0) {
			a = 777;
		}
		else a = 666;
	}
	else a = 555;
	return (a);
}

void main() {
	int a;
	char b;
	a = 5;
	b = 'b';
	printf("123");
	fun1_printf(a, b);
	fun2_scanf();
	fun3_empty();
	fun4_while();
	fun5_do_while();
	fun6_for();
	printf(fun7_if(a));
}