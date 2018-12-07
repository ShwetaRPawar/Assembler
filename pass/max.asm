section .data
	a dd 10,20
	msg db "enter num",10,0
	value db "%d"
	b dd 100
section .bss
	n resd 1
	array resd 100

section .text
	global main 
	extern printf,scanf

main: pusha 
	push msg
	call printf
	push n
	push value
	call scanf
	add esp,12
	popa
	xor ecx,ecx

loop:	mov ebx,array
	mov eax,4
	mul ecx
	add ebx,eax
	push ecx
	push ebx
	push value
	call scanf
	add esp,8
	pop ecx
	inc ecx
	dec esi
	cmp esi,0
	jnz loop


	xor edi,edi
	xor ecx,ecx

max:	mov ebx,array
	mov eax,4
	mul ecx
	add ebx,eax		
	jle next
	jge next1

next1:	mov edi,edi
	inc ecx
	dec esi
	cmp esi,0
	jnz max

	push edi
	push value
	call printf
	add esp,8
