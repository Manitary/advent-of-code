F:=Open("input16.txt","r");
original_input:=[StringToInteger(c):c in Eltseq(Gets(F))];
base_pattern:=[0,1,0,-1];

input:=original_input;
patterns:=[];
for i in [1..#input] do
	new_pattern:=&cat[[c:j in [1..i]]:c in base_pattern];
	pattern:=[];
	repeat
		pattern cat:=new_pattern;
	until #pattern gt #input;
	Remove(~pattern,1);
	Append(~patterns,pattern);
end for;

output:=[];
for phase in [1..100] do
	for i in [1..#input] do
		output[i]:=Abs(&+[input[j]*patterns[i,j]:j in [1..#input]|patterns[i,j] ne 0]) mod 10;
	end for;
	input:=output;
end for;

PrintFile("day16.txt",Seqint([output[i]:i in [8..1 by -1]]));

offset:=Seqint([original_input[i]:i in [7..1 by -1]]);
input:=&cat[original_input:i in [1..10000]];

for phase in [1..100] do
	for i in [#input-1..offset+1 by -1] do
		input[i]:=(input[i]+input[i+1]) mod 10;
	end for;
end for;

PrintFile("day16.txt",Seqint([input[i]:i in [offset+8..offset+1 by -1]]));
