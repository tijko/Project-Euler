.section .data
    answer: .asciz "Answer: %d\n"
    anslen: .word 12

.section .text
    .globl main

    main:
        pushq    %rbp
        movq     %rsp, %rbp
        xor      %rdi, %rdi
        xor      %rsi, %rsi
        jmp      setup

    setup:
        movq    $3, %rbx # count
        movq    $0, %rcx # total
        mov     $3, %rsi
        mov     $5, %rdi
        jmp     loop

    loop:
        cmp     $1000, %rbx
        je      exit

        movq    %rbx, %rax
        xor     %rdx, %rdx

        div     %rsi
        cmp     $0, %rdx
        je      found

        movq    %rbx, %rax
        xor     %rdx, %rdx

        div     %rdi
        cmp     $0, %rdx
        je      found

        inc     %rbx
        jmp     loop

    found:
        add     %rbx, %rcx
        inc     %rbx
        jmp     loop

    exit:
        leaq    answer(%rip), %rdi
        movq    %rcx, %rsi
        callq   printf

        movq    $60, %rax
        movq    $1, %rdi
        syscall
