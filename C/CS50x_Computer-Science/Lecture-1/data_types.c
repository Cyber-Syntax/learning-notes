#include <stdio.h>
#include <stdlib.h>

// calculator

int main(void)
{
    // TODO: learn int, float, double, long, long long, short, char, unsigned, signed, differents
    // Let we give the numbers to saw the difference between int, float, double, long, long long, short, char, unsigned, signed
    int x = 1;
    int y = 2;
    float f = 1.0;
    float g = 2.0;
    double d = 1.0;
    double e = 2.0;
    long l = 1;
    long m = 2;
    long long ll = 1;
    long long mm = 2;
    short s = 1;
    short t = 2;
    unsigned u = 1;
    unsigned uu = 2;
    signed si = 1;
    signed sii = 2;
    

    // Sum of above variables
    printf("x + y(int) = %i + %i = %i \n", x, y, x + y);
    printf("f + g(float) = %f + %f = %f \n", f, g, f + g);
    printf("d + e(double) = %f + %f = %f \n", d, e, d + e);
    printf("l + m(long) = %li + %li = %li \n", l, m, l + m);
    printf("ll + mm(long long) = %lli + %lli = %lli \n", ll, mm, ll + mm);
    printf("s + t(short) = %hi + %hi = %hi \n", s, t, s + t);
    printf("u + uu(unsigned) = %u + %u = %u \n", u, uu, u + uu);
    printf("si + sii(signed) = %i + %i = %i \n", si, sii, si + sii);
            
    // %.20f = 20 decimal places learn more about printf
    printf("This is the same as above but with 20 decimal places, floating-point imprecision  \n");
    printf("x + y(int) = %.20i + %.20i = %.20i \n", x, y, x + y);
    printf("f + g(float) = %.20f + %.20f = %.20f \n", f, g, f + g);
    printf("d + e(double) = %.20f + %.20f = %.20f \n", d, e, d + e);
    printf("l + m(long) = %.20li + %.20li = %.20li \n", l, m, l + m);
    printf("ll + mm(long long) = %.20lli + %.20lli = %.20lli \n", ll, mm, ll + mm);
    printf("s + t(short) = %.20hi + %.20hi = %.20hi \n", s, t, s + t);
    printf("u + uu(unsigned) = %.20u + %.20u = %.20u \n", u, uu, u + uu);
    printf("si + sii(signed) = %.20i + %.20i = %.20i \n", si, sii, si + sii);

    printf("\n");


    // add new line
    printf("\n");

    return 0;

}

