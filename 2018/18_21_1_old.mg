F:=Open("input21.txt","r");
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

/*
registers:=[0:i in [1..reg_num]];
k:=0;
repeat
	registers:=exec(registers[ip]+1,registers);
	registers[ip]+:=1;
	k+:=1;
until registers[ip]+1 eq 29;

registers:=[i eq 1 select registers[5] else 0:i in [1..reg_num]];
k:=0;
repeat
	registers:=exec(registers[ip]+1,registers);
	registers[ip]+:=1;
	k+:=1;
until registers[ip] ge #prog;
*/

registers:=[0:i in [1..reg_num]];
k:=0;
list:={**};
while true do
	registers:=exec(registers[ip]+1,registers);
	registers[ip]+:=1;
	k+:=1;
	if registers[ip]+1 eq 29 then
		Include(~list,registers[5]);
	end if;
	if #MultisetToSet(list) ne #list then
		"found duplicate";
		break;
	end if;
end while;
k;



