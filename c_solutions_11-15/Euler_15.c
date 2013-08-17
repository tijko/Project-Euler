#include <stdio.h>
#include <stdlib.h>
#include <time.h>


typedef struct {

    int trk;
    int *arr;

} Total;

void base_check(Total *tot) {
    
    int i;
    for (i=tot->trk - 1; i >= 0; i--) {
        if (tot->arr[i] > 9) {
            while (tot->arr[i] > 9) {
                tot->arr[i] -= 10;
                tot->arr[i-1] += 1;
            }
        }
    }
}

void factorial_of_number(Total *tot, int factor) {

    int factorial = 1;
    char fac_str[BUFSIZ];

    int *tmp = calloc (tot->trk, sizeof (int));

    int n, i, v;
    int pos = tot->trk - 1;
    int b_pos;
    while (factorial <= factor) {    
        n = sprintf (fac_str, "%d", factorial);
        pos -= (n - 1);
        b_pos = pos;
        for (i=0; i < n; i++) {
            for (v=tot->trk - 1; v >= 0; v--) {
                tmp[pos] += (tot->arr[v] * (fac_str[i] - '0'));
                pos--;
            }
            pos = b_pos;
            pos++;
        }
        for (i=0; i < tot->trk; i++) {
            tot->arr[i] = tmp[i];
        }

        base_check(tot);

        free (tmp);
        pos = tot->trk - 1;        
        factorial += 1;
        tmp = calloc (tot->trk, sizeof (int));
    }
}	
	
void factorial_multiply(Total *tot) {

    int *tmp = calloc (tot->trk, sizeof (int));

    int i,v;
    int cnt = 0;
    for (i=0; i < tot->trk; i++) {
        if (tot->arr[i] == 0) { 
            cnt++;
        }
        else {
            break;
        }
    }

    int pos, b_pos = tot->trk - 1;
    for (i=tot->trk-1; i >= cnt; i--) {
        for (v=tot->trk-1; v >= cnt; v--) {
            tmp[pos] += (tot->arr[v] * tot->arr[i]);
            pos--;
        }
        b_pos--;
        pos = b_pos;
    }
    for (i=0; i < tot->trk; i++) {
        tot->arr[i] = tmp[i];
    }

    base_check(tot);

    free (tmp);
}

int main(void) {

    clock_t start, stop;
    start = clock();

    Total t;
    t.trk = 50;
    t.arr = calloc (t.trk, sizeof (int));
    t.arr[t.trk - 1] = 1;
    
    Total f;
    f.trk = 50;
    f.arr = calloc (f.trk, sizeof (int));
    f.arr[f.trk - 1] = 1;

    int forty = 40;
    int twenty = 20;

    factorial_of_number(&f, twenty);
    factorial_multiply(&f);

    factorial_of_number(&t, forty);    

    int cnt = 0;
    int flag = 0;
    while (flag != 1) {
        if (t.arr[cnt] == 0) {
            cnt++;
        }

        else {
            flag = 1;
        }
    }
    
    Total bg;
    bg.trk = t.trk - cnt;
    bg.arr = calloc (bg.trk, sizeof (int));
    
    int i = 0;
    while (cnt < t.trk) {
        bg.arr[i] = t.arr[cnt];
        cnt++;
        i++;
    }
    free (t.arr);

    cnt = 0;
    flag = 0;

    while (flag != 1) {
        if (f.arr[cnt] == 0) {
            cnt++;
        }

        else {
            flag = 1;
        }
    }

    Total sm;
    sm.trk = f.trk - cnt;
    sm.arr = calloc (sm.trk, sizeof (int));

    i = 0;
    while (cnt < f.trk) { 
        sm.arr[i] = f.arr[cnt];
        cnt++;
        i++;
    }
    free (f.arr);

    Total ans;
    ans.trk = (bg.trk - sm.trk) + 1;
    ans.arr = calloc (ans.trk, sizeof (int));

    int anspos = 0;

    Total bgtmp;
    bgtmp.trk = (sm.trk + 1);
    bgtmp.arr = calloc (bgtmp.trk, sizeof (int));

    int bgpos = sm.trk;
    int pos = bgpos -  1;

    for (i=0; i <= bgtmp.trk; i++) {
        bgtmp.arr[i+1] = bg.arr[i];
    }

    flag = 0;
    cnt = 0;
    while (flag != 1) { 
        cnt++;
        for (i=pos+1; i >= 1; i--) {
            if ((bgtmp.arr[i] - sm.arr[i-1]) < 0 && i > 0) {
                bgtmp.arr[i-1] -= 1;
                bgtmp.arr[i] += 10;
            }
            if ((bgtmp.arr[i] - sm.arr[i-1]) < 0 && i <= 0) {
                break;
            }
            bgtmp.arr[i] -= sm.arr[i-1];
        }
        if (bgtmp.arr[0] < 1) {
            for (i=1; i < bgtmp.trk; i++) {
                if (bgtmp.arr[i] > sm.arr[i-1]) {
                    break;
                }
                if (bgtmp.arr[i] == sm.arr[i-1]) {
                    continue;
                }
                else {
                    ans.arr[anspos] = cnt;
                    cnt = 0;
                    anspos++;
                    for (i=0; i < bgtmp.trk - 1; i++) {
                        bgtmp.arr[i] = bgtmp.arr[i+1];
                    }
                    bgtmp.arr[bgtmp.trk-1] = bg.arr[bgpos];
                    bgpos++;
                    if (bgpos > bg.trk - 1) {
                        flag = 1;
                        break;
                    }
                } 
            } 
        } 
    }             

    free (bg.arr);
    free (sm.arr);

    stop = clock();
    printf ("Answer: ");
    for (i=0; i < ans.trk; i++) {
        printf ("%d", ans.arr[i]);
    }
    printf ("\n");

    printf ("Time: %f\n", ((float)stop - (float)start) / CLOCKS_PER_SEC);
    return 0;
}

