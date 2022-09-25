	la $t0, b
	Label:
	lw $s1, 0 ($t0)
	la $t0, c
	lw $s2, 0 ($t0)
	la $t0, a
	Label1:
	lw $s3, 0 ($t0)
	sub $t0, $s1, 3
	add $s3, $t0, $s2
	add $a0, $zero, $s3
	addi $v0, $zero, 1
	syscall