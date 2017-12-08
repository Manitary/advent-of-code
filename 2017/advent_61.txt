input:=[4,1,15,12,0,9,9,5,5,8,7,3,14,5,12,3];

old:=[input];
counter:=0;
check:=false;

repeat
	counter+:=1;
	max,index:=Maximum(input);
	input[index]:=0;
	for i in [1..max] do
		cell:=(index+i) mod #input;
		if cell eq 0 then
			cell:=#input;
		end if;
		input[cell]+:=1;
	end for;
	old[counter+1]:=input;
	for i in [1..#old-1] do
		if old[i] eq old[#old] then
			check:=true;
			break;
		end if;
	end for;
until check eq true;
counter;