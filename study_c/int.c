#include<stdio.h>
#include <limits.h>
#include <stdint.h>
/*
정수형 자료형 : char : 1바이트, 8비트
               int : 4바이트, 32비트
부호 키워드 :signed : 부호o, 따라서 주로 생략한다. (signed) char :-128~128
            unsigned : 부호x, 0부터 시작 unsigned char :0 ~255
크기 :  short : %2 short (int) -> 2바이트,
        long : x2 long int -> 8바이트

    %u : 부호없는 10진수
    %d : 부호 있는 10진수
*/

int main()
{
    char num1=-10;
    unsigned int num11=200;
    unsigned char num12=256; //255범위 초과 => 오버플로우
    unsigned char num13=257; //255범위 초과 => 오버플로우
    int num2=200;
    long int num3=300;

    printf("%d, %d, %ld\n",num1,num2,num3);
    printf("%u, overflow:%u, %u\n",num11,num12,num13); //unsigned char은 %d가 가능하지만, unsigned int는 %u를 해줘야된다.
    
    int size;
    size = sizeof num1;
    size = sizeof(num2);

    printf("sizeof num1,2,long : %d,%d,%d\n",num1,num2,sizeof(long));

    char min1 = CHAR_MIN;
    short min2 = SHRT_MIN;
    int max1 = INT_MAX;

    printf("1:%d, 2:%d, 3:%d\n",min1,min2,max1);

    //overflow
    char over_min1=CHAR_MIN -1;
    unsigned int over_min2= 0 -1;
    unsigned int over_max1=INT_MAX+1;
    
    printf("1:%d, 2:%u, 2-1:%d, 3:%d\n",over_min1,over_min2,over_min2,over_max1);
    
    int16_t new1 = 32767;
    uint8_t new2 = 255;
    
    printf("16bit:%d, u8bit:%u\n",new1,new2);
    return 0;
}
