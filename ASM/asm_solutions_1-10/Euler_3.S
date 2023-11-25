.section .data
    answer: .asciz "Answer: %d\n"
    anslen: .word 12

.section .text
    .globl main

    # Layout:
    #   r8  -> BigInt
    #   r9  -> Start of Canidates
    #   r10 -> Half of Current-Canidate
    #   r11 -> Range (2..r10/2)
    main:
        pushq   %rbp
        movq    %rsp, %rbp
        xor     %rdx, %rdx
        jmp     setup

    setup:
        xor       %r8,           %r8
        movq      $600851475143, %r8
        cvtsi2sdq %r8,           %xmm0
        sqrtsd    %xmm0,         %xmm0
        cvttsd2si %xmm0,         %r9
        jmp       next

    next:
        dec       %r9
        movq      %r9,           %rax
        cvtsi2sdq %r9,           %xmm1
        sqrtsd    %xmm1,         %xmm1
        cvttsd2si %xmm1,         %r10
        movq      $2,            %r11
        movq      %r9,           %rax
        jmp       factor

    factor:
        xor     %rdx, %rdx
        div     %r11
        test    %rdx, %rdx
        jz      next 
        cmp     %r11, %r10
        je      prime
        inc     %r11
        movq    %r9, %rax
        xor     %rdx, %rdx
        jmp     factor

    prime:
        movq    %r8,  %rax
        xor     %rdx, %rdx
        div     %r9
        test    %rdx, %rdx
        jz      exit
        jmp     next 
            
    exit:
        leaq    answer(%rip), %rdi
        movq    %r9,          %rsi
        callq   printf

        movq    $60, %rax
        movq    $1,  %rdi
        syscall
