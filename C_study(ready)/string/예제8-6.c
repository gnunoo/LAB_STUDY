#include <stdio.h>

int main(void)
{
	char str[80];

	printf("���ڿ� �Է� : ");  // �Է� �ȳ� �޽��� ���
	gets(str);            // ��ĭ�� ������ ���ڿ� �Է�
	puts("���ڿ� �Է� : ");  // ���ڿ� ��� ���
	puts("%s",str);          // �迭�� ����� ���ڿ� ���

	return 0;
}