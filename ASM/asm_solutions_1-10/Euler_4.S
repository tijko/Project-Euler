.section .data
    message: .asciz "Answer: %d\n"
    msglen: .word 12

    fmtstub: .asciz "%d"
    fmtlen: .word 8

.section .text
    .globl main

    main:
        pushq   %rbp
        movq    %rsp, %rbp
        xor     %rdi, %rdi
        xor     %rax, %rax
        xor     %rdx, %rdx
        jmp     setup

    setup:
        xor     %r12, %r12
        xor     %r13, %r13
        movq    $100, %r12
        movq    $101, %r13
        movq    $1000, %r14
        jmp     L0

    L0:
        inc     %r12
        cmp     %r12, %r14
        je      L2 
        xor     %rax, %rax
        xor     %rbx, %rbx
        movq    %r12, %rax
        movq    %r13, %rbx
        mulq    %rbx
        jmp     L1

    L1:
        movq    $10, %r8
        movq    %rax, %r15
        movq    $0, %rsi
        movq    $3, %rdi
        jmp     L4

    L4:
        cmp     %rsi, %rdi
        je      L0 
        shr     $1, %rax
        div     %r8
        movq    %rdx, %
        #leaq    message(%rip), %rdi
        #movq    %rax, %rsi
        #callq   printf
        #jmp     L0

    L2:
        movq    %r13, %r15
        inc     %r13
        cmp     %r13, %r14
        je      L3
        movq    %r15, %r12
        jmp     L0

    L3:
        cmp     %r12, %r14
        je      exit
        movq    %r15, %r12
        jmp     L0

    exit:
        movq    $60, %rax
        movq    $1, %rdi
        syscall 
