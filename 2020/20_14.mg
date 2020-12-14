F:=Open("input14.txt","r");

input:=[];
while true do
	s:=Gets(F);
	if IsEof(s) then
		break;
	end if;
	Append(~input,s);
end while;
val:=AssociativeArray(Integers());

for s in input do
	b, _, m:=Regexp("mask = ([10X]+)", s);
	if b then
		mask:=Reverse(Eltseq(m[1]));
	else
		_, _, i:=Regexp("mem.([0-9]+)", s);
		_, _, v:=Regexp("= ([0-9]+)", s);
		i:=StringToInteger(i[1]);
		v:=Intseq(StringToInteger(v[1]),2);
		for j in [1..#mask] do
			if mask[j] eq "X" then
				v[j]:=IsDefined(v,j) select v[j] else 0;
			else
				v[j]:=StringToInteger(mask[j]);
			end if;
		end for;
		val[i]:=Seqint(v,2);
	end if;
end for;
PrintFile("day14.txt",&+[val[x]:x in Keys(val)]);

function GetList(input)
	output:={};
	i:=Index(input,"X");
	if i eq 0 then
		return {input};
	else
		temp:=input;
		for b in ["0","1"] do
			temp[i]:=b;
			output join:=GetList(temp);
		end for;
	end if;
	return output;
end function;

val:=AssociativeArray(Integers());
for s in input do
	b, _, m:=Regexp("mask = ([10X]+)", s);
	if b then
		mask:=Reverse(Eltseq(m[1]));
	else
		_, _, i:=Regexp("mem.([0-9]+)", s);
		_, _, v:=Regexp("= ([0-9]+)", s);
		i:=Intseq(StringToInteger(i[1]),2);
		v:=StringToInteger(v[1]);
		a:=[mask[j] ne "0" select mask[j] else IsDefined(i,j) select IntegerToString(i[j]) else "0":j in [1..#mask]];
		for add in GetList(a) do
			val[Seqint([StringToInteger(x):x in add],2)]:=v;
		end for;
	end if;
end for;
PrintFile("day14.txt",&+[val[x]:x in Keys(val)]);
