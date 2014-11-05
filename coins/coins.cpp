#include <stdio.h>

void check_denomination(int n, int target){
    int T[90001][3];
    int i, j, x, y, X, Y, tmp;
    target = target*target;
    for(i = 0; i <= target; i++){
        T[i][0] = 90001;
        T[i][1] = 0;
        T[i][2] = 0;
    }
    T[0][0] = 0;
    for(i = 0; i < n; i++){
        scanf("%d %d\n", &X, &Y);
        for(j = 0; j <= target; j++){
            x = X + T[j][1];
            y = Y + T[j][2];
            tmp = x*x + y*y;
            if(tmp <= target && T[j][0] + 1 < T[tmp][0]){
                T[tmp][0] = T[j][0] + 1;
                T[tmp][1] = x;
                T[tmp][2] = y;
            }
        }
    }
    if(T[target][0] == 90001)
        printf("not possible\n");
    else
        printf("%d\n", T[target][0]);
}

int main(int argc, char** argv){
    int i, t, n, target;
    scanf("%d\n", &t);
    for(i = 0; i < t; i++){
        while(!scanf("%d %d\n", &n, &target));
        check_denomination(n, target);
    }
    return 0;
}

