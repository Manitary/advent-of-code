input:="stpzcrnm";

function module(input,n)
	if input mod n eq 0 then
		return n;
	else
		return input mod n;
	end if;
end function;

function binary(n,range)
	b:="";
	for i in [-range+1..0] do
		if 2^-i le n then
			b*:="1";
			n-:=2^-i;
		else
			b*:="0";
		end if;
	end for;
	boolseq:=[b[i] eq "1" : i in [1..#b]];
return boolseq;
end function;

function decimal(input)
	n:=0;
	for i in [1..#input] do
		if input[i] then
			n+:=2^(#input - i);
		end if;
	end for;
	return n;
end function;

forward hex;
function convert(d)
	if d eq 10 then
		return "a";
	elif d eq 11 then
		return "b";
	elif d eq 12 then
		return "c";
	elif d eq 13 then
		return "d";
	elif d eq 14 then
		return "e";
	elif d eq 15 then
		return "f";
	elif d gt 15 then
		return hex(d);
	else
		return IntegerToString(d);
	end if;
end function;

function hex(n)
	h:="";
	i:=-1;
	repeat
		i+:=1;
	until 16^i gt n;
	for k in [-i+1..0] do
		h*:=convert(n div 16^-k);
		n:=n mod 16^-k;
	end for;
	if #h eq 0 then
		h:="0";
	end if;
	return h;
end function;

function HexToBinary(hash)
	n:=[];
	for l in [1..#hash] do
		for digit in [0..15] do
			if hex(digit) eq hash[l] then
				Append(~n,binary(digit,4));
				break;
			end if;
		end for;
	end for;
	return n;				
end function;

function generate_knot_hash(input)
	input:=[BinaryString(input[i]):i in [1..#input]];
	input2:=[];
	for i in [1..#input] do
		Append(~input2,input[i][1]);
	end for;
	input2 cat:= [17,31,73,47,23];
	list:=[i:i in [0..255]];
	skip:=0;
	position:=1;
	for round in [1..64] do
		for n in [1..#input2] do
			length:=input2[n];
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
		position:=module(position+length+skip,#list);
		skip+:=1;
		end for;
	end for;

	list_bool:=[binary(list[i],16):i in [1..#list]];
	dense_hash:=[];
	for i in [1..16] do
		x:=[false:i in [1..16]];
		for j in [1..16] do
			Xor(~x,list_bool[16*(i-1)+j]);
		end for;
		dense_hash[i]:=x;
	end for;
			
	dense_hash:=[decimal(dense_hash[i]): i in [1..#dense_hash]];
	dense_hash:=[hex(dense_hash[i]): i in [1..#dense_hash]];
	for i in [1..#dense_hash] do
		if #dense_hash[i] eq 1 then
			dense_hash[i]:="0" cat dense_hash[i];
		end if;
	end for;

	knot_hash:="";
	for i in [1..#dense_hash] do
		knot_hash*:=dense_hash[i];
	end for;
	
	return knot_hash;
end function;

lines:=[];
for line in [0..127] do
	lines[line+1]:=generate_knot_hash(input cat "-" cat IntegerToString(line));
end for;

squares:=[];
for line in [1..128] do
	squares[line]:=HexToBinary(lines[line]);
end for;

used:=0;
for line in [1..128] do
	for column in [1..32] do
		for item in [1..4] do
			if squares[line][column][item] then
				used+:=1;
			end if;
		end for;
	end for;
end for;
used;