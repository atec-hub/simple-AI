#include <stdio.h>

char *sesli="aeiuo��";
char *sessiz="qwrtyp�sdfghjkl�zxcvbnm�";
char buffer[80];
char kod[80];

char *kodla();

main()
{

giris:
	printf(">");
	gets(buffer);
	if(!buffer[0]) goto giris;
	printf("\n--------------------------------\n");
	printf("%s -> %s -> ",buffer,kodla(buffer));
	/* printf("%s:%d\n",buffer,code3(buffer,0)); */
	hece(buffer);
	goto giris;
}

code(c)
char c;
{
	if(c==0x00)          return(0);
	if(strchr(sessiz,c)) return(1);
	if(strchr(sesli,c))  return(2);
	/* error */			 return(3);
}

code2(p)
char *p;
{
	switch(code(*p)) {
	case 0:                             return(0);
	case 1:  /* 0 */
		switch(code(*++p)) {
		case 0:                         return(0);
		case 1: /* 00 */
			switch(code(*++p)) {
			case 0: /* 00  */           return(1);
			case 1: /* 000 */           return(1);
			case 2: /* 001 */
				switch(code(*++p)) {
				case 0: /* 001  */      return(9);
				case 1: /* 0010 */
					switch(code(*++p)) {
					case 0: /* 0010  */ return(7);
					case 1: /* 00100 */ return(7);
					case 2: /* 00101 */ return(9);
					case 3: /* 00102 */ return(0);
					}
				case 2: /* 0011 */      return(0);
				case 3: /* 0012 */      return(0);
				}
			case 3: /* 002 */           return(0);
			}
		case 2: /* 01 */
			switch(code(*++p)) {
			case 0:                     return(2);
			case 1: /* 010 */
				switch(code(*++p)) {
				case 0: /* 010  */      return(3);
				case 1: /* 0100 */
					switch(code(*++p)) {
					case 0: /* 0100  */ return(8);
					case 1: /* 01000 */ return(8);
					case 2: /* 01001 */ return(3);
					case 3: /* 01002 */ return(0);
					}
				case 2: /* 0101 */      return(2);
				case 3:                 return(0);
				}
			case 2: /* 011 */           return(2);
			case 3:                     return(0);
			}
		case 3:                         return(0);
		}
	case 2:  /* 1 */
		switch(code(*++p)) {
		case 0:                         return(4);
		case 1: /* 10 */
			switch(code(*++p)) {
			case 0: /* 10  */           return(5);
			case 1: /* 100 */
				switch(code(*++p)) {
				case 0: /* 100  */      return(6);
				case 1: /* 1000 */      return(0);
				case 2: /* 1001 */      return(5);
				case 3: /* 1002 */      return(0);
				}
			case 2: /* 101 */           return(4);
			case 3:                     return(0);
			}
		case 2: /* 11 */                return(4);
		case 3:                         return(0);
		}
	case 3:                             return(0);
	}
}
code3(p,n,t)
char *p;
int n,t;
{
	int n0=0;
	if(t) printf("[");
next:
	if(t) printf("%d",code2(p));
	switch(code2(p)) {
	case 0: /* -    */
		if(t) printf("]\n");
		return(n0);
	case 1: /* 00   */
		switch(n) {
		case  0: n=1; p+=2; break;
		default: goto err;
		}
		break;
	case 2: /* 01   */
		switch(n) {
		case 0:
		case 2:
		case 3:
		case 4:
		case 5:
		case 7:
		case 8:
		case 9: n=2; p+=2; break;
		default: goto err;
		}
		break;
	case 3: /* 010  */
		switch(n) {
		case 0:
		case 2:
		case 3:
		case 4:
		case 5:
		case 7:
		case 8:
		case 9: p+=3; n=3; break;
		default: goto err;
		}
		break;
	case 4: /* 1    */
		switch(n) {
		case 0:
		case 2:
		case 4:
		case 5:	n=4; p++; break;
		default: goto err;
		}
		break;
	case 5: /* 10   */
		switch(n) {
		case 0:
		case 4:
		case 2: n=5; p+=2; break;
		case 1: n=7; p+=2; break;
		default: goto err;
		}
		break;
	case 6: /* 100  */
		switch(n) {
		case 0:
		case 2: n=6; p+=3; break;
		default: goto err;
		}
		break;
	case 7: /* 0010 */
		switch(n) {
		case  0: n=7; p+=4; break;
		default: goto err;
		}
		break;
	case 8: /* 0100 */
		switch(n) {
		case  0:
		case  2:
		case  3: n=8; p+=4; break;
		default: goto err;
		}
		break;
	case 9: /* 001 */
		switch(n) {
		case 0: n=9; p+=3; break;
		default: goto err;
		}
		break;
	default: goto err;
	}
	if(n0==0) n0=n;
	goto next;
err:
	if(t) printf("]\n");
	return(0);
}

hece(w)
char *w;
{
	int n,i,t;
	char s[80];
	for(n=0,t=1;*w;) {
		strcpy(s,w);
		n=code3(w,n,t);
		i=t=0;
		switch(n) {
		case 0: return;
		case 8:           /* XXXX */
		case 7: i++;
		case 9:
		case 6:           /* XXX  */
		case 3: i++;
		case 1:           /* XX   */
		case 2:
		case 5:	i++;
		case 4: i++;      /* X    */
		}
		*(s+i)='\0'; strcpy(w,w+i);
		printf("%s",s);
		if(*w) printf("-");
	}
	printf("\n");
}

char *kodla(s)
char *s;
{
	register int i;
	for(i=0;*s;s++,i++) {
		if(strchr(sesli,*s)) {
			kod[i]='1';
		} else if(strchr(sessiz,*s)) {
			kod[i]='0';
		} else {
			kod[i]='2';
		}
	}
	kod[i]='\0'; return kod;
}