.section .data
    answer: .asciz "Answer: %d\n"
    anslen: .word 12

.section .text
    .globl main

    main:
        pushq   %rbp
        movq    %rsp, %rbp
        xor     %rdi, %rdi
        xor     %rsi, %rsi
        jmp     setup

    setup:
        xor     %rax, %rax # Division Register (even)
        xor     %rbx, %rbx # Fibonacci (a, b)
        xor     %rcx, %rcx # Total
        xor     %rdx, %rdx # Remainder Register     

        movq    $2, %r9
        movq    $1, %rdi
        movq    $1, %rsi
        jmp     loop

    fibonacci:
        movq    %rsi, %r8
        addq    %rdi, %rsi
        movq    %r8, %rdi
        jmp     even 

    even:
        xor     %rax, %rax
        xor     %rdx, %rdx
        movq    %rsi, %rax
        div     %r9
        cmp     $0, %rdx
        je      found
        jmp     loop

    loop:
        cmp     $4000000, %rsi
        jge     finish
        jmp     fibonacci
        
    found:
        add     %rsi, %rcx
        jmp     loop

    finish:
        leaq    answer(%rip), %rdi
        movq    %rcx, %rsi
        callq   printf

        movq    $60, %rax
        movq    $1, %rdi
        syscall
