main:
	addi $v0, $0, 42
	add $a0, $0, $0
	addi $a1, $0, 4
	syscall
	
	add $a0, $0, $a0
	addi $v0, $0, 1
	syscall
	
	addi $v0, $0, 32
	addi $a0, $0, 100
	syscall
	
	j main