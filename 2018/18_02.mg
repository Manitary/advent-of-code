F:=Open("input2.txt","r");
input:=[];
while true do
	s:=Gets(F);
	if IsEof(s) then
		break;
	end if;
	Append(~input,Eltseq(s));
end while;

ms:=[SequenceToMultiset(c): c in input];

two:=0;
three:=0;
for s in ms do
	if 2 in Multiplicities(s) then
		two+:=1;
	end if;
	if 3 in Multiplicities(s) then
		three+:=1;
	end if;
end for;

PrintFile("day02.txt",two*three);

len:=#input[1];
for i in [1..#input-1], j in [i..#input] do
	if #(ms[i] meet ms[j]) ge len-2 then
		d:={};
		for k in [1..len] do
			if input[i][k] ne input[j][k] then
				Include(~d,k);
				if #d gt 1 then
					break;
				end if;
			end if;
		end for;
		if #d eq 1 then
			PrintFile("day02.txt",&*Remove(input[i],Random(d)));
			break;
		end if;
	end if;
end for;
