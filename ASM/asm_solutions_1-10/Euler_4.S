.section .data
    message: .asciz "Answer: %d\n"
    msglen: .word 12

.section .text
    .globl main

    main:
        pushq   %rbp
        movq    %rsp, %rbp
        xor     %rdi, %rdi
        jmp     setup

    setup:
        xor     %rax, %rax
        xor     %rdx, %rdx
        jmp     palindrome

    palindrome:
        movq    $100, %rax
        movq    $101, %rbx
        mulq    %rbx
        jmp     exit

    exit:
        leaq    message(%rip), %rdi
        movq    %rax, %rsi
        callq   printf

        movq    $60, %rax
        movq    $1, %rdi
        syscall 
