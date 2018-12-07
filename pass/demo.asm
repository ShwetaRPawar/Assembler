section .data
	a dd 10,20,30
	b db "shweta pawar"

section .text
	global main

main: 
	mov eax,10
	mov ebx,20
	add eax,ebx

