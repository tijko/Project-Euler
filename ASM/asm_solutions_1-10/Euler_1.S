.section .data
 
.section .text
  .globl main 

  main:
    pushq    %rbp
    movq     %rsp, %rbp
    xor      %rdi, %rdi
    xor      %rsi, %rsi
    jmp      factor

  found:
    mov     $total, %eax
    add     $count, %eax
    jmp     factor

  factor:
    mov      $count, %ecx
    cmp      $0x3e8, %ecx
    je       end 
    mov      $count, %ax
    mov      $5, %bl
    div      %bl 
    cmp      $0, %ah
    je       found
    jmp      factor       

  count: .word 0
  total: .word 0
        
  end:
    mov      $1, %rax
    mov      $1, %rdi
    mov      $10,%rdx
    mov      $answer, %rsi
    syscall 
    movq     $60, %rax
    movq     $0,  %rdi
    syscall

  answer:
   .asciz "Answer: \n"
