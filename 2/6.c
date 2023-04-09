#include<stdio.h>
#include<string.h>
int i = 0, f = 0;
char str[30];

void E();
void EPrime();
void T();
void Tprime();
void F();

void E()
{
    printf("\nE->TE'");
    T();
    EPrime();
}

void EPrime()
{
    if (str[i] == '+')
    {
        printf("\nE'->+TE'");
        i++;
        T();
        EPrime();
    }
    else if ((str[i] == ')') || (str[i] == '$'))
        printf("\nE'->^");
}

void T()
{
    printf("\nT->FT'");
    F();
    Tprime();
}

void Tprime()
{
    if (str[i] == '*')
    {
        printf("\nT'->*FT'");

        i++;
        F();
        Tprime();
    }

    else if ((str[i] == ')') || (str[i] == '+') || (str[i] == '$'))
        printf("\nT'->^");
}

void F()
{
    if (str[i] == 'a')
    {
        printf("\nF->a");
        i++;
    }

    else if (str[i] == '(')
    {
        printf("\nF->(E)");
        i++;
        E();
        if (str[i] == ')')
            i++;
    }
    else
        f = 1;
}

void main()
{
    int len;
    printf("Enter the string: ");
    scanf("%s", str);
    len = strlen(str);
    str[len] = '$';
    E();
    if ((str[i] == '$') && (f == 0))
        printf("\nString successfully parsed!");
    else
        printf("\nSyntax Error!");
    getch();
}
