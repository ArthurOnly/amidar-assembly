main:
	addi $v0, $0, 30
	syscall
	
	#and $a0, $a0, 00000000000000000001111111111111
	and $a0, $a0, 4095
	addi $t1, $0, 100
	div $a0, $t1
	mflo $a0
	addi $a0, $a0, 1
	addi $a1, $0, 2		
	div $a0, $a1 #ver se é par
	mfhi $a0

	addi $v0, $0, 36
	add $a0, $0, $a0
	syscall
	
	addi $v0, $0, 11
	addi $a0, $0, '\n'
	syscall
	
	addi $v0, $0, 32
	addi $a0, $0, 100
	syscall 
	
	j main
