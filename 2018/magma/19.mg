F:=Open("input19.txt","r");
prog:=[];
while true do
	s:=Gets(F);
	if IsEof(s) then
		break;
	end if;
	b,_,id:=Regexp("#ip ([0-9]+)",s);
	_,_,o:=Regexp("([a-z]+) ([0-9]+) ([0-9]+) ([0-9]+)",s);
	if b then
		ip:=StringToInteger(id[1])+1;
	else
		Append(~prog,<o[1],StringToInteger(o[2]),StringToInteger(o[3]),StringToInteger(o[4])>);
	end if;
end while;

reg_num:=6;

bti:=func<b|b select 1 else 0>;

addr:=func<reg,op|[i eq op[4]+1 select reg[op[2]+1]+reg[op[3]+1] else reg[i]:i in [1..reg_num]]>;
addi:=func<reg,op|[i eq op[4]+1 select reg[op[2]+1]+op[3] else reg[i]:i in [1..reg_num]]>;
mulr:=func<reg,op|[i eq op[4]+1 select reg[op[2]+1]*reg[op[3]+1] else reg[i]:i in [1..reg_num]]>;
muli:=func<reg,op|[i eq op[4]+1 select reg[op[2]+1]*op[3] else reg[i]:i in [1..reg_num]]>;
banr:=func<reg,op|[i eq op[4]+1 select BitwiseAnd(reg[op[2]+1],reg[op[3]+1]) else reg[i]:i in [1..reg_num]]>;
bani:=func<reg,op|[i eq op[4]+1 select BitwiseAnd(reg[op[2]+1],op[3]) else reg[i]:i in [1..reg_num]]>;
borr:=func<reg,op|[i eq op[4]+1 select BitwiseOr(reg[op[2]+1],reg[op[3]+1]) else reg[i]:i in [1..reg_num]]>;
bori:=func<reg,op|[i eq op[4]+1 select BitwiseOr(reg[op[2]+1],op[3]) else reg[i]:i in [1..reg_num]]>;
setr:=func<reg,op|[i eq op[4]+1 select reg[op[2]+1] else reg[i]:i in [1..reg_num]]>;
seti:=func<reg,op|[i eq op[4]+1 select op[2] else reg[i]:i in [1..reg_num]]>;
gtir:=func<reg,op|[i eq op[4]+1 select bti(op[2] gt reg[op[3]+1]) else reg[i]:i in [1..reg_num]]>;
gtri:=func<reg,op|[i eq op[4]+1 select bti(reg[op[2]+1] gt op[3]) else reg[i]:i in [1..reg_num]]>;
gtrr:=func<reg,op|[i eq op[4]+1 select bti(reg[op[2]+1] gt reg[op[3]+1]) else reg[i]:i in [1..reg_num]]>;
eqir:=func<reg,op|[i eq op[4]+1 select bti(op[2] eq reg[op[3]+1]) else reg[i]:i in [1..reg_num]]>;
eqri:=func<reg,op|[i eq op[4]+1 select bti(reg[op[2]+1] eq op[3]) else reg[i]:i in [1..reg_num]]>;
eqrr:=func<reg,op|[i eq op[4]+1 select bti(reg[op[2]+1] eq reg[op[3]+1]) else reg[i]:i in [1..reg_num]]>;

exec:=func<n,reg|(eval prog[n,1])(reg,prog[n])>;

//This would be the brute force normal solution (works for part 1, immensely slow for part 2)
/*
registers:=[0:i in [1..reg_num]];
repeat
	registers:=exec(registers[ip]+1,registers);
	registers[ip]+:=1;
until registers[ip] ge #prog;
PrintFile("day19.txt",registers[1]);
*/

//After reading the input file we can now hardcode
function solve(p)
	registers:=[i eq 1 select (p eq 1 select 0 else 1) else 0:i in [1..reg_num]];
	repeat
		registers:=exec(registers[ip]+1,registers);
		registers[ip]+:=1;
	until registers[ip] eq 1;
	return SumOfDivisors(registers[#registers]);
end function;

PrintFile("day19.txt",solve(1));
PrintFile("day19.txt",solve(2));
