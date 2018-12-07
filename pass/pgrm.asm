%macro write 2
      mov   eax, 4
      mov   ebx, 1
      mov   ecx, %1
      mov   edx, %2
      int   80h
%endmacro
%macro read 2
      mov   eax, 4
      mov   ebx, 1
      mov   ecx, %1
      mov   edx, %2
      int   80h
%endmacro
section .data
	;s dd 10,20,30,40
	;y dd 50,60,70,80
	str1 db "this is a string",10,0
	len1 equ $ - str1
	str2 db "this another string",0
	msg db "hello",0,102
	len2 equ $ - msg
	;q dd 10,20,30,40
	;e dd 50,60,70,80
	t db "abcdef ghijklmn",10,0
	o db "hello sid",0
	sf db "here the output",0
section .bss
	;str resd 1
section .text
	global main
main:
	write str1,len1
	write msg,len2
	sub eax,str1
	mov ebx,edx
	mov ecx,edx
	mov esi,edi
	mul eax
	mov edi,esp
	xor eax,20
	xor eax,30
	xor eax,str1
abc:
	xor ebx,ebx
	jmp bcf
bcf:	
