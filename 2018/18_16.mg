F:=Open("input16.txt","r");
before:=[];
opcode:=[];
after:=[];
prog:=[];
while true do
	b:=Gets(F);
	if IsEof(b) then
		break;
	end if;
	if #b lt 2 then
		while true do
			o:=Gets(F);
			if IsEof(o) then
				break;
			end if;
			if #o gt 2 then
				o:="[" cat &*[o[i] eq " " select "," else o[i]:i in [1..#o]] cat "]";
				Append(~prog, eval o);
			end if;
		end while;
	end if;
	o:=Gets(F);
	a:=Gets(F);
	x:=Gets(F);
	_,_,b:=Regexp("(\\[[0-9 ,]+\\])",b);
	_,_,a:=Regexp("(\\[[0-9 ,]+\\])",a);
	Append(~before,eval b[1]);
	Append(~after,eval a[1]);
	o:="[" cat &*[o[i] eq " " select "," else o[i]:i in [1..#o]] cat "]";
	Append(~opcode,eval o);
end while;

bti:=func<b|b select 1 else 0>;

addr:=func<reg,op|[i eq op[4]+1 select reg[op[2]+1]+reg[op[3]+1] else reg[i]:i in [1..4]]>;
addi:=func<reg,op|[i eq op[4]+1 select reg[op[2]+1]+op[3] else reg[i]:i in [1..4]]>;
mulr:=func<reg,op|[i eq op[4]+1 select reg[op[2]+1]*reg[op[3]+1] else reg[i]:i in [1..4]]>;
muli:=func<reg,op|[i eq op[4]+1 select reg[op[2]+1]*op[3] else reg[i]:i in [1..4]]>;
banr:=func<reg,op|[i eq op[4]+1 select BitwiseAnd(reg[op[2]+1],reg[op[3]+1]) else reg[i]:i in [1..4]]>;
bani:=func<reg,op|[i eq op[4]+1 select BitwiseAnd(reg[op[2]+1],op[3]) else reg[i]:i in [1..4]]>;
borr:=func<reg,op|[i eq op[4]+1 select BitwiseOr(reg[op[2]+1],reg[op[3]+1]) else reg[i]:i in [1..4]]>;
bori:=func<reg,op|[i eq op[4]+1 select BitwiseOr(reg[op[2]+1],op[3]) else reg[i]:i in [1..4]]>;
setr:=func<reg,op|[i eq op[4]+1 select reg[op[2]+1] else reg[i]:i in [1..4]]>;
seti:=func<reg,op|[i eq op[4]+1 select op[2] else reg[i]:i in [1..4]]>;
gtir:=func<reg,op|[i eq op[4]+1 select bti(op[2] gt reg[op[3]+1]) else reg[i]:i in [1..4]]>;
gtri:=func<reg,op|[i eq op[4]+1 select bti(reg[op[2]+1] gt op[3]) else reg[i]:i in [1..4]]>;
gtrr:=func<reg,op|[i eq op[4]+1 select bti(reg[op[2]+1] gt reg[op[3]+1]) else reg[i]:i in [1..4]]>;
eqir:=func<reg,op|[i eq op[4]+1 select bti(op[2] eq reg[op[3]+1]) else reg[i]:i in [1..4]]>;
eqri:=func<reg,op|[i eq op[4]+1 select bti(reg[op[2]+1] eq op[3]) else reg[i]:i in [1..4]]>;
eqrr:=func<reg,op|[i eq op[4]+1 select bti(reg[op[2]+1] eq reg[op[3]+1]) else reg[i]:i in [1..4]]>;

codes:=[addr,addi,mulr,muli,banr,bani,borr,bori,setr,seti,gtir,gtri,gtrr,eqir,eqri,eqrr];
codes_num:=[{0..15}:c in codes];

count:=0;
for i in [1..#before] do
	if Multiplicity({*f(before[i],opcode[i]) eq after[i]:f in codes*},true) ge 3 then
		count+:=1;
	end if;
end for;

count;


for i in [1..#before] do
	for j in [1..#codes] do
		if codes[j](before[i],opcode[i]) ne after[i] then
			Exclude(~codes_num[j],opcode[i][1]);
			if #codes_num[j] eq 1 then
				for k in [1..#codes] do
					if k ne j then
						Exclude(~codes_num[k],Representative(codes_num[j]));
					end if;
				end for;
			end if;
		end if;
	end for;
	if {#c:c in codes_num} eq {1} then
		break;
	end if;
end for;

codes_num:=[Representative(c):c in codes_num];

registers:=[0,0,0,0];
for o in prog do
	registers:=codes[Index(codes_num,o[1])](registers,o);
end for;

registers[1];
