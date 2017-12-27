input:=[18,1,0,161,255,137,254,252,14,95,165,33,181,168,2,188];

function module(input,n)
	if input mod n eq 0 then
		return n;
	else
		return input mod n;
	end if;
end function;

list:=[i:i in [0..255]];
skip:=0;
position:=1;
for n in [1..#input] do
	length:=input[n];
	if length gt 0 then
		swap:=[];
		for i in [1..length] do
			swap[i]:=list[module(position+i-1,#list)];
		end for;
		Reverse(~swap);
		for i in [1..length] do
			list[module(position+i-1,#list)]:=swap[i];
		end for;
	end if;
	position+:=length+skip;
	skip+:=1;
end for;

list[1]*list[2];