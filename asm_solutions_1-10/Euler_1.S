.globl main

.data

answer:
    .asciz "Answer: "

.text

main:

    push    %rbp
    mov    %rsp, %rbp

    xor     %rdi, %rdi
    xor     %rsi, %rsi

factor:
    mod     $5, %rdi
    jnz     loop
    mod     $3, %rdi
    jnz     loop
    inc     %rsi

loop:
    cmp     $1000, %rdi
    jz      complete
    inc     %rdi

print_answer:

    movl    $1, %rax
    movl    answer, %rdi
    movl    $8, %rsi
    syscall 
    
done:
    movl    $60, %rax
    movl    $0,  %rax
    syscall
    
