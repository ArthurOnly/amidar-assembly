.text
main:
	addi $a0, $0, 100
	addi $a1, $0, 10
	addi $a2, $0, 100
	addi $a3, $0, 100
	addi $v0, $0, 31
	syscall
	
	addi $v0, $0, 32
	addi $a0, $0, 100
	syscall
	
	j main
