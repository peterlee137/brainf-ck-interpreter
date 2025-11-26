code=""",>,>48+[-<-<-2>]<[-<+>]<:[-]10+."""
textin="99"
textptr=0
tapelen=30000
tape=[0]*tapelen
ptr=0
loop_stack=[]
copied=0
i=0
depth=1
howmany=1
#variable to know how many times to move pointer or add value
while i<len(code):
    cmd=code[i]
    if cmd==">": ptr = (ptr+howmany) % tapelen
    elif cmd=="<": ptr = (ptr-howmany) % tapelen
    elif cmd=="+": tape[ptr] = (tape[ptr]+howmany) % 256
    elif cmd=="-": tape[ptr] = (tape[ptr]-howmany) % 256
    elif cmd==":": print(tape[ptr],end="")
    elif cmd==".": print(chr(tape[ptr]),end="")
    elif cmd=="c": copied=tape[ptr]
    elif cmd=="p": tape[ptr]=copied
    elif cmd==",": 
        tape[ptr] = ord(textin[textptr])
        textptr += 1
    elif cmd.isdigit(): 
        howmany=0
        while i<len(code) and code[i].isdigit():
            howmany= howmany*10 + int(code[i])
            i+=1
        continue
    elif cmd=="[":
        if tape[ptr]==0:
            depth=1
            while depth:
                i+=1
                if code[i]=="[": depth+=1
                elif code[i]=="]": depth-=1
        else:
            loop_stack.append(i)
    elif cmd=="]":
        if tape[ptr]==0:
            loop_stack.pop()
        else:
            i=loop_stack[-1]
    howmany=1
    i+=1
            
