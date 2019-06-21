#include <stdio.h>
#include <math.h>

float relu(float a) {
	if (a > 0) {
		return a;
	} else {
		return 0;
	}
}


double activation(double a) {
	return tanh(a);
}


double sigmoid(double a) {
	double out;
	out = 1/(1+(exp(-a)));
	return out;
}


double neuron(int iter, double *X, double *W, double *B) {
	int j = iter;
	double c[iter];
	double out = 0.;
	for(int i = 0; i < j; i++, X++, W++, B++) {
		*c = (*W * *X)+ *B;
	}
	for (int i = 0; i < j; i++) {
		out += c[i];
	}
	return tanh(out);
}


int main(void) {
	return 0;
}
